import sys
from subprocess import check_call

from colorama import Fore, Style


def lint():
    args = sys.argv[1:]
    black_args = ["black", ".", "--exclude", ".venv"]
    isort_args = [
        "isort",
        ".",
        "--profile",
        "black",
        "--skip",
        ".venv",
    ]

    if "check" in args:
        black_args.append("--check")
        isort_args.append("--check-only")

    print(Fore.BLUE + "Lint imports with isort")
    check_call(isort_args)
    print(Fore.GREEN + "\nLint with Black")
    check_call(black_args)
    print(Fore.RED + "\nLint with flake8")
    # stop the build if there are Python syntax errors or undefined names
    check_call(
        [
            "flake8",
            ".",
            "--count",
            "--extend-exclude=.venv",
            "--select=E9,F63,F7,F82",
            "--show-source",
            "--statistics",
        ]
    )
    # exit-zero treats all errors as warnings.
    # add compatibility with black
    # https://black.readthedocs.io/en/stable/compatible_configs.html#flake8
    check_call(
        [
            "flake8",
            ".",
            "--count",
            "--exit-zero",
            "--extend-exclude=.venv",
            "--extend-ignore=E203,W503",
            "--max-line-length=88",
            "--statistics",
        ]
    )
    print(Fore.MAGENTA + "\nSecurity check with Bandit")
    check_call(["bandit", "-r", ".", "-x", "./scripts,./tests,./.venv"])
    print(Style.RESET_ALL)
