#!/usr/bin/env python3
"""
Crestron System Simulator

A UDP server that simulates the Crestron control system for testing the
house control panel. This simulator handles the following command types:

ZONES (individual lights/circuits):
    Input:  /zone/[zone_id]/[dimmer_level]     (dimmer_level: 0-65535)
    Output: /zone/[zone_id]/level/[dimmer_level]

BUTTONS (scenes):
    Input:  /button/[button_id]/press
    Output: /button/[button_id]/fb             (when scene is active)
            (no response when scene is off)

SHADES:
    Input:  /shade/[shade_id]/[position_level] (position_level: 0-65535)
    Output: /shade/[shade_id]/level/[position_level]

Usage:
    python crestron_simulator.py [--host HOST] [--port PORT]

Example:
    python crestron_simulator.py --host 172.16.31.201 --port 50000
"""

import argparse
import logging
import re
import socket
import sys
from datetime import datetime

from devices import BUTTONS, SHADES, ZONES

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)


class CrestronSimulator:
    """UDP server that simulates a Crestron control system."""

    def __init__(self, host: str = "0.0.0.0", port: int = 50000):
        """
        Initialize the Crestron simulator.

        Args:
            host: IP address to bind to (default: 0.0.0.0 for all interfaces)
            port: UDP port to listen on (default: 50000)
        """
        self.host = host
        self.port = port
        self.socket = None

        # Device state (copied from devices.py with mutable state)
        self.zones = {k: dict(v) for k, v in ZONES.items()}
        self.buttons = {k: dict(v) for k, v in BUTTONS.items()}
        self.shades = {k: dict(v) for k, v in SHADES.items()}

        # Command patterns
        self.zone_pattern = re.compile(r'^/zone/(\d+)/(\d+)$')
        self.button_pattern = re.compile(r'^/button/(\d+)/press$')
        self.shade_pattern = re.compile(r'^/shade/(\d+)/(\d+)$')

    def start(self):
        """Start the UDP server."""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        try:
            self.socket.bind((self.host, self.port))
            logger.info(f"Crestron Simulator started on {self.host}:{self.port}")
            logger.info(f"Loaded {len(self.zones)} zones, {len(self.buttons)} buttons, {len(self.shades)} shades")
            logger.info("Waiting for commands...")

            self._run_loop()

        except socket.error as e:
            logger.error(f"Failed to start server: {e}")
            sys.exit(1)
        except KeyboardInterrupt:
            logger.info("Shutting down...")
        finally:
            if self.socket:
                self.socket.close()

    def _run_loop(self):
        """Main server loop - receive and process commands."""
        while True:
            try:
                data, addr = self.socket.recvfrom(1024)
                command = data.decode('utf-8').strip()
                logger.info(f"Received from {addr[0]}:{addr[1]}: {command}")

                response = self._process_command(command)

                if response:
                    self.socket.sendto(response.encode('utf-8'), addr)
                    logger.info(f"Sent to {addr[0]}:{addr[1]}: {response}")

            except socket.error as e:
                logger.error(f"Socket error: {e}")
            except UnicodeDecodeError as e:
                logger.error(f"Failed to decode message: {e}")

    def _process_command(self, command: str) -> str | None:
        """
        Process an incoming command and return the appropriate response.

        Args:
            command: The command string received from the client

        Returns:
            Response string to send back, or None if no response needed
        """
        # Try zone command: /zone/[id]/[level]
        match = self.zone_pattern.match(command)
        if match:
            zone_id = int(match.group(1))
            level = int(match.group(2))
            return self._handle_zone(zone_id, level)

        # Try button command: /button/[id]/press
        match = self.button_pattern.match(command)
        if match:
            button_id = int(match.group(1))
            return self._handle_button(button_id)

        # Try shade command: /shade/[id]/[position]
        match = self.shade_pattern.match(command)
        if match:
            shade_id = int(match.group(1))
            position = int(match.group(2))
            return self._handle_shade(shade_id, position)

        logger.warning(f"Unknown command format: {command}")
        return None

    def _handle_zone(self, zone_id: int, level: int) -> str:
        """
        Handle a zone (dimmer) command.

        Args:
            zone_id: The zone/circuit ID
            level: Dimmer level (0-65535)

        Returns:
            Response string: /zone/[id]/level/[level]
        """
        # Clamp level to valid range
        level = max(0, min(65535, level))

        if zone_id in self.zones:
            self.zones[zone_id]["level"] = level
            zone_name = self.zones[zone_id]["name"]
            percent = round(level / 65535 * 100, 1)
            logger.info(f"  Zone '{zone_name}' set to {percent}% ({level})")
        else:
            logger.warning(f"  Unknown zone ID: {zone_id} (level={level})")

        # Always respond with level confirmation
        return f"/zone/{zone_id}/level/{level}"

    def _handle_button(self, button_id: int) -> str | None:
        """
        Handle a button (scene) press command.

        Args:
            button_id: The button/scene ID

        Returns:
            Response string: /button/[id]/fb if scene becomes active, None otherwise
        """
        if button_id in self.buttons:
            # Toggle the button state
            self.buttons[button_id]["active"] = not self.buttons[button_id]["active"]
            button_name = self.buttons[button_id]["name"]
            is_active = self.buttons[button_id]["active"]

            logger.info(f"  Button '{button_name}' {'activated' if is_active else 'deactivated'}")

            # Only send feedback if the scene is now active
            if is_active:
                return f"/button/{button_id}/fb"
            return None
        else:
            logger.warning(f"  Unknown button ID: {button_id}")
            # Still respond with feedback for unknown buttons (they might be valid)
            return f"/button/{button_id}/fb"

    def _handle_shade(self, shade_id: int, position: int) -> str:
        """
        Handle a shade position command.

        Args:
            shade_id: The shade/shade group ID
            position: Shade position (0-65535, where 0=closed, 65535=open)

        Returns:
            Response string: /shade/[id]/level/[position]
        """
        # Clamp position to valid range
        position = max(0, min(65535, position))

        if shade_id in self.shades:
            self.shades[shade_id]["position"] = position
            shade_name = self.shades[shade_id]["name"]
            percent = round(position / 65535 * 100, 1)
            logger.info(f"  Shade '{shade_name}' set to {percent}% ({position})")
        else:
            logger.warning(f"  Unknown shade ID: {shade_id} (position={position})")

        # Always respond with position confirmation
        return f"/shade/{shade_id}/level/{position}"

    def get_status(self) -> dict:
        """
        Get current status of all devices.

        Returns:
            Dictionary with zones, buttons, and shades status
        """
        return {
            "zones": self.zones,
            "buttons": self.buttons,
            "shades": self.shades
        }


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Crestron Control System Simulator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Protocol:
  ZONES:   /zone/[id]/[level]   -> /zone/[id]/level/[level]
  BUTTONS: /button/[id]/press   -> /button/[id]/fb (when active)
  SHADES:  /shade/[id]/[pos]    -> /shade/[id]/level/[pos]

  Levels and positions are analog values from 0 to 65535.
        """
    )
    parser.add_argument(
        "--host",
        default="0.0.0.0",
        help="Host IP to bind to (default: 0.0.0.0 for all interfaces)"
    )
    parser.add_argument(
        "--port",
        type=int,
        default=50000,
        help="UDP port to listen on (default: 50000)"
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Enable verbose/debug logging"
    )

    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    print("=" * 60)
    print("  Crestron Control System Simulator")
    print("  Orient House - Control Panel Testing")
    print("=" * 60)
    print()

    simulator = CrestronSimulator(host=args.host, port=args.port)
    simulator.start()


if __name__ == "__main__":
    main()
