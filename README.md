# Encrypted Message Transfer

Simple Python project for encrypting and sending messages between two systems.

The project uses AES and RSA for hybrid encryption.

## Setup

Clone the repository:

```bash
git clone https://github.com/permission-bit/encryption
cd encryption
```

Create a Python 3.11 virtual environment:

```bash
python3.11 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

Install the requirements:

```bash
pip install -r requirements.txt
```

## How it works

There are three main parts:

```text
decrypt.py
encrypt.py
server/
├── send.py
└── listener.py
```

### 1. Get the Public Key

The person receiving the message provides their:

```text
publickey.pem
```

The sender puts this file in the main project directory.

The public key can be sent to the sender by email or another suitable method.

The private key must stay with the recipient.

### 2. Write and encrypt a message

Run:

```bash
python encrypt.py
```

This creates the encrypted message:

```text
message/encrypted_message.txt
```

### 3. Start the Listener

The recipient starts the listener **before** the message is sent:

```bash
python server/listener.py
```

The listener waits for the incoming connection.

### 4. Send the Message

The sender runs:

```bash
python server/send.py
```

The encrypted message is then transferred to the listener.

## Files

```text
decrypted.py
encrypt.py
requirements.txt
received_message.txt   <---

server/
├── send.py
└── listener.py

message/
└── encrypted_message.txt

publickey.pem
```

## Encrypt received message

```bash
python decrypt_received_message.py
```

The recipient keeps their private key and should never send it to anyone.

## Requirements

Python 3.11+

Install dependencies with:

```bash
pip install -r requirements.txt
```
