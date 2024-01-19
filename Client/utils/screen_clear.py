from sys import platform
import os


def screen_clear():
    if platform == "linux" or platform == "linux2":
        # linux
        os.system("clear")
    elif platform == "darwin":
        # OSX
        os.system("clear")
    elif platform == "win32":
        # windows
        os.system("cls")
    else:  # OS niet herkend!
        print("Operating System not regconized!")
