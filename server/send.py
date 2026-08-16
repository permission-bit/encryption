import socket
from pathlib import Path
import struct 


BASE_DIR = Path(__file__).resolve().parent.parent

encrypted_message_dir = BASE_DIR / "message" / "encrypted_message.txt"

HOST = "127.0.0.1"
PORT = 9003


def send_file(file_path):
    file_size = file_path.stat().st_size

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        s.sendall(struct.pack("!Q", file_size))

        with open(file_path, "rb") as f:
            while chunk := f.read(4096):
                s.sendall(chunk)

    print(f"Sent: {file_path}")
    print(f"Size: {file_size} bytes")


send_file(encrypted_message_dir)