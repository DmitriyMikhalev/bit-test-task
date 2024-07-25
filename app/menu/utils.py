import os


def read_int(
    message: str,
    error_message: str,
    min_value: int = 0,
    max_value: int = 0
) -> int:
    print(message, end="")
    while True:
        val = input()
        if val.isdigit() and min_value <= (res := int(val)) <= max_value:
            return res
        print(error_message, end="")


def clear_console():
    os.system("cls" if os.name == "nt" else "clear")
