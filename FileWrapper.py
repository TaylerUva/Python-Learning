import time
import os
import subprocess
import platform
__creator = "Tayler Uva"
__dash = "============================="


def __printKey(msg, fileName):
    print("\n%s" % __dash,
          msg, "- %s" % os.path.basename(fileName),
          "- Created by %s" % __creator,
          "%s\n" % __dash)


def hello(fileName, clear=True):  # Adds a default value for clear if one is not passed
    # Documentation Formatting
    """
    Clears the console and adds a header message.
    """
    if clear:
        clearConsole()
    __printKey("START", fileName)


def goodbye(fileName):
    # Documentation Formatting
    """
    Adds footer message
    """
    __printKey("END", fileName)


def clearConsole():
    # Documentation Formatting
    """
    Clears the terminal screen.
    """

    # Clear command as function of OS
    command = "cls" if platform.system().lower() == "windows" else "clear"

    # Action
    return subprocess.call(command) == 0
