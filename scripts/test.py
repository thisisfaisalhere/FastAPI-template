import sys
from subprocess import check_call

from colorama import Fore, Style


def test():
    print(Fore.CYAN + "Test with pytest")
    pytest_args = [
        "pytest",
        "-vv",
        "--cov-report=xml",
        "--cov-fail-under=80",
        "--cov=src",
        "--cov-config=.coveragerc",
        "tests/",
    ]

    args = sys.argv[1:]
    if "html" in args:
        pytest_args = [
            "pytest",
            "-vv",
            "--cov-report=html",
            "--cov-fail-under=80",
            "--cov=src",
            "--cov-config=.coveragerc",
            "tests/",
        ]
    if "nofail" in args:
        print("Running tests without failing if under coverage")
        pytest_args = [
            "pytest",
            "--cov-report=xml",
            "--cov=src",
            "tests/",
        ]

    check_call(pytest_args)
    print(Style.RESET_ALL)
