from subprocess import check_call

from colorama import Fore, Style


def start():
    print(Fore.LIGHTCYAN_EX + "Starting src")
    check_call(
        [
            "uvicorn",
            "src.main:app",
            "--reload",
        ],
    )
    print(Style.RESET_ALL)
