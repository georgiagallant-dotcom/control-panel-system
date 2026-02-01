#!/usr/bin/env python3
"""
Test client for the Crestron Simulator.

This script sends test commands to the simulator and displays the responses.
Useful for verifying the simulator is working correctly.

Usage:
    python test_client.py [--host HOST] [--port PORT]
"""

import argparse
import socket
import time


def send_command(sock: socket.socket, host: str, port: int, command: str, timeout: float = 2.0) -> str | None:
    """
    Send a command and wait for response.

    Args:
        sock: UDP socket
        host: Server host
        port: Server port
        command: Command string to send
        timeout: Response timeout in seconds

    Returns:
        Response string or None if timeout
    """
    sock.settimeout(timeout)
    sock.sendto(command.encode('utf-8'), (host, port))
    print(f"  Sent:     {command}")

    try:
        data, addr = sock.recvfrom(1024)
        response = data.decode('utf-8').strip()
        print(f"  Received: {response}")
        return response
    except socket.timeout:
        print(f"  Received: (no response - timeout)")
        return None


def main():
    parser = argparse.ArgumentParser(description="Test client for Crestron Simulator")
    parser.add_argument("--host", default="127.0.0.1", help="Simulator host (default: 127.0.0.1)")
    parser.add_argument("--port", type=int, default=50000, help="Simulator port (default: 50000)")
    args = parser.parse_args()

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    print("=" * 60)
    print("  Crestron Simulator Test Client")
    print(f"  Target: {args.host}:{args.port}")
    print("=" * 60)
    print()

    # Test Zone Commands
    print("Testing ZONE commands:")
    print("-" * 40)

    # Set zone 2707 (Lower Level Stor 003 ZB-001) to 50%
    send_command(sock, args.host, args.port, "/zone/2707/32768")
    time.sleep(0.5)

    # Set zone 2707 to 100%
    send_command(sock, args.host, args.port, "/zone/2707/65535")
    time.sleep(0.5)

    # Set zone 2707 to 0% (off)
    send_command(sock, args.host, args.port, "/zone/2707/0")
    time.sleep(0.5)

    # Test unknown zone
    send_command(sock, args.host, args.port, "/zone/99999/32000")
    print()

    # Test Button Commands
    print("Testing BUTTON commands:")
    print("-" * 40)

    # Press button 2392 (Lower Level Stor 003 ST-003.2 Button 1)
    send_command(sock, args.host, args.port, "/button/2392/press")
    time.sleep(0.5)

    # Press again to toggle off (should get no response)
    send_command(sock, args.host, args.port, "/button/2392/press")
    time.sleep(0.5)

    # Press again to toggle on (should get fb response)
    send_command(sock, args.host, args.port, "/button/2392/press")
    print()

    # Test Shade Commands
    print("Testing SHADE commands:")
    print("-" * 40)

    # Set shade 8112 (Game Room Solar Shades) to 50% open
    send_command(sock, args.host, args.port, "/shade/8112/32768")
    time.sleep(0.5)

    # Set shade to fully open
    send_command(sock, args.host, args.port, "/shade/8112/65535")
    time.sleep(0.5)

    # Set shade to fully closed
    send_command(sock, args.host, args.port, "/shade/8112/0")
    print()

    # Test Invalid Commands
    print("Testing INVALID commands:")
    print("-" * 40)

    send_command(sock, args.host, args.port, "/invalid/command")
    send_command(sock, args.host, args.port, "hello")
    print()

    print("=" * 60)
    print("  Test complete!")
    print("=" * 60)

    sock.close()


if __name__ == "__main__":
    main()
