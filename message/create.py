from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
MESSAGE_DIR = BASE_DIR / "created_message.txt"

def write_message():
    created_message = input("Create your message: ")

    return created_message

message = write_message()


def make_message():
    try:
        with open(MESSAGE_DIR, "w") as message_file:
            message_file.write(message)
    except Exception as e:
        print(e)

make_message()