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

## Project Structure

```text
encryption/
├── crypto/
│   └── crypto.py
├── decrypt.py
├── decypt_received_message.py
├── encrypt.py
├── LICENSE
├── message/
│   ├── create.py
│   ├── created_message.txt
│   ├── decrypted_message.txt
│   └── encrypted_message.txt
├── private_key.pem
├── public_key.pem
├── README.md
├── received_message.txt
├── requirements.txt
├── server/
│   ├── listener.py
│   └── send.py
└── utils/
    └── grab_os.py
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

## 3. Configure the Listener

On the receiver's computer, open:

```text
server/listener.py
```

Set:

```python
HOST = "0.0.0.0"
PORT = 9003
```

`0.0.0.0` allows the listener to accept incoming connections.

### Find the Public IP

Run:

```bash
python grab_ip.py
```

This displays the public IP address of the receiver.

Example:

```text
Public IP: 203.0.113.42
```

Remember this IP address.

## 4. Configure the Sender

On the sender's computer, open:

```text
server/send.py
```

Set the receiver's public IP:

```python
HOST = "203.0.113.42"
PORT = 9003
```

Replace `203.0.113.42` with the public IP shown by `grab_ip.py`.

The port must be the same on both computers.

> **Note:** When using a public IP, the receiver's router/firewall must allow incoming TCP connections on port `9003`. Port forwarding may be required.

### 5. Start the Listener

The recipient starts the listener **before** the message is sent:

```bash
python server/listener.py
```

The listener waits for the incoming connection.

### 6. Send the Message

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
