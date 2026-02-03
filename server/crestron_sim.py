#!/usr/bin/env python3
"""
Crestron simulator - responds with brightness level
"""

import socket

UDP_IP = "0.0.0.0"
UDP_PORT = 50000

# Brightness level (0-65535)
BRIGHTNESS = 32767  # 50% - change this to test different levels

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print(f"Crestron simulator listening on port {UDP_PORT}")
print(f"Brightness: {BRIGHTNESS} ({BRIGHTNESS*100//65535}%)")
print("Waiting for messages...")

while True:
    data, addr = sock.recvfrom(1024)
    message = data.decode('utf-8')
    print(f"RX from {addr}: {message}")

    if message.startswith("/button/"):
        # Format: /button/[id]/on or /button/[id]/level/[value]
        parts = message.split("/")
        if len(parts) >= 4:
            button_id = parts[2]
            action = parts[3]
            if action == "on":
                level = BRIGHTNESS
            elif action == "level" and len(parts) >= 5:
                level = int(parts[4])
            else:
                level = 0
            response = f"/zone/{button_id}/level/{level}"
            sock.sendto(response.encode(), addr)
            print(f"TX to {addr}: {response}")
    elif message.startswith("/slider/"):
        # Slider adjusted - echo back the brightness to update the LED
        # Format: /slider/[button_id]/level/[brightness]
        parts = message.split("/")
        if len(parts) >= 5:
            button_id = parts[2]
            brightness = parts[4]
            response = f"/zone/{button_id}/level/{brightness}"
            sock.sendto(response.encode(), addr)
            print(f"TX to {addr}: {response}")
    else:
        sock.sendto(data, addr)
        print(f"TX to {addr}: {message}")
