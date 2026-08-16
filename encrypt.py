import os
from pathlib import Path

from generate_keys.crypto import (
    generate_rsa_keys,
    encrypt_file
)


BASE_DIR = Path(__file__).resolve().parent


private_key = BASE_DIR / "private_key.pem"
message_dir = BASE_DIR / "message" / "created_message.txt"

encrypted_message_dir = BASE_DIR / "message" / "encrypted_message.txt"


def main():

    if not os.path.exists(private_key):
        generate_rsa_keys()

    encrypt_file(
        message_dir,
        encrypted_message_dir
    )

    print("encryptedt.")

    


if __name__ == "__main__":
    main()