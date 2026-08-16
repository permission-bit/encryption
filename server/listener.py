import socket
import struct

HOST = "127.0.0.1"
PORT = 9003

OUTPUT_FILE = "received_message.txt"


def receive_file(conn):

    header = b""

    while len(header) < 8:
        chunk = conn.recv(8 - len(header))

        if not chunk:
            raise ConnectionError("Verbindung während Header abgebrochen")

        header += chunk

    file_size = struct.unpack("!Q", header)[0]

    print(f"Erwarte {file_size} Bytes")

    received = 0

    with open(OUTPUT_FILE, "wb") as f:
        while received < file_size:
            chunk = conn.recv(
                min(4096, file_size - received)
            )

            if not chunk:
                raise ConnectionError(
                    "Verbindung während Dateiübertragung abgebrochen"
                )

            f.write(chunk)
            received += len(chunk)

    print(f"Datei vollständig empfangen: {received} Bytes")


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:

    server.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_REUSEADDR,
        1
    )

    server.bind((HOST, PORT))
    server.listen(5)

    print(f"Server läuft auf {HOST}:{PORT}")

    while True:
        conn, addr = server.accept()

        print(f"Verbindung von {addr}")

        with conn:
            receive_file(conn)