from crypto.crypto import decrypt_file

import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


private_key = BASE_DIR / "private_key.pem"
message_dir = BASE_DIR / "message" / "created_message.txt"

encrypted_message_dir = BASE_DIR / "received_message.txt"

decrypted_file_dir = BASE_DIR / "encrypted_received_message.txt"


def main():
    decrypt_file(
        encrypted_message_dir,
        decrypted_file_dir
    )

    print(70 * "=")
    print(f"[*] Encrypted message: {decrypted_file_dir}.")
    print(70 * "=")

if __name__ == "__main__":
    main()