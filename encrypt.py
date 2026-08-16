import os
from pathlib import Path

from crypto.crypto import (
    generate_rsa_keys,
    encrypt_file
)

from message.create import write_message

BASE_DIR = Path(__file__).resolve().parent


private_key = BASE_DIR / "private_key.pem"
message_dir = BASE_DIR / "message" / "created_message.txt"

encrypted_message_dir = BASE_DIR / "message" / "encrypted_message.txt"


def main():
    print(70 * "=")
    write_message()

    if not os.path.exists(private_key):
        generate_rsa_keys()

    encrypt_file(
        message_dir,
        encrypted_message_dir
    )

    print(70 * "=")
    print(f"[*] Encrypted message: {encrypted_message_dir}.")
    print(70 * "=")

    


if __name__ == "__main__":
    main()