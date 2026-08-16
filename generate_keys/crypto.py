from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
import os


PRIVATE_KEY_FILE = "private_key.pem"
PUBLIC_KEY_FILE = "public_key.pem"


def generate_rsa_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=4096
    )

    public_key = private_key.public_key()

    with open(PRIVATE_KEY_FILE, "wb") as f:
        f.write(
            private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption()
            )
        )

    with open(PUBLIC_KEY_FILE, "wb") as f:
        f.write(
            public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            )
        )


def load_public_key():
    with open(PUBLIC_KEY_FILE, "rb") as f:
        return serialization.load_pem_public_key(f.read())


def load_private_key():
    with open(PRIVATE_KEY_FILE, "rb") as f:
        return serialization.load_pem_private_key(
            f.read(),
            password=None
        )


def encrypt_file(input_file, output_file):
    public_key = load_public_key()

    aes_key = AESGCM.generate_key(bit_length=256)

    aes = AESGCM(aes_key)

    nonce = os.urandom(12)

    with open(input_file, "rb") as f:
        data = f.read()

    encrypted_data = aes.encrypt(
        nonce,
        data,
        None
    )

    encrypted_aes_key = public_key.encrypt(
        aes_key,
        padding.OAEP(
            mgf=padding.MGF1(
                algorithm=hashes.SHA256()
            ),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    with open(output_file, "wb") as f:

        f.write(
            len(encrypted_aes_key).to_bytes(4, "big")
        )

        f.write(encrypted_aes_key)

        f.write(nonce)

        f.write(encrypted_data)


def decrypt_file(input_file, output_file):
    private_key = load_private_key()

    with open(input_file, "rb") as f:

        key_length = int.from_bytes(
            f.read(4),
            "big"
        )

        encrypted_aes_key = f.read(key_length)

        nonce = f.read(12)

        encrypted_data = f.read()

    aes_key = private_key.decrypt(
        encrypted_aes_key,
        padding.OAEP(
            mgf=padding.MGF1(
                algorithm=hashes.SHA256()
            ),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    aes = AESGCM(aes_key)

    decrypted_data = aes.decrypt(
        nonce,
        encrypted_data,
        None
    )

    with open(output_file, "wb") as f:
        f.write(decrypted_data)