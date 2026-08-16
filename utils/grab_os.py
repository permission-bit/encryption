import platform

def get_os_name():
    name = platform.system().lower()

    if name == "darwin":
        name = "macos"

    return name

def full_arch():

    full = platform.platform().lower()

    return full


print(get_os_name())
print(full_arch())