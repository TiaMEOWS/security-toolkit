# coding=utf-8
import contextlib
import os
import subprocess

from core import SecurityTool
from core import SecurityToolsCollection


class InstaBrute(SecurityTool):
    TITLE = "InstaBrute"
    DESCRIPTION = "InstaBrute is a tool to brute force Instagram accounts"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/tiameows/instabrute.git"]
    RUN_COMMANDS = ["cd instabrute && sudo python3 instabrute.py"]
    PROJECT_URL = "https://github.com/tiameows/instabrute"

    def run(self):
        name = input("Enter Username >> ")
        wordlist = input("Enter wordword list >> ")
        os.chdir("instabrute")
        subprocess.run(
            ["sudo", "python3", "instabrute.py", "-u", f"{name}", "-d",
             f"{wordlist}"])


class BruteForce(SecurityTool):
    TITLE = "BruteForce"
    DESCRIPTION = "BruteForce is a tool to brute force social media accounts"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/tiameows/bruteforce.git"]
    RUN_COMMANDS = ["cd bruteforce && sudo python3 bruteforce.py"]
    PROJECT_URL = "https://github.com/tiameows/bruteforce"


class Faceshell(SecurityTool):
    TITLE = "Faceshell"
    DESCRIPTION = "Faceshell is a tool to hack Facebook accounts"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/tiameows/faceshell.git"]
    RUN_COMMANDS = ["cd faceshell && sudo python3 faceshell.py"]
    PROJECT_URL = "https://github.com/tiameows/faceshell"

    def run(self):
        name = input("Enter Username >> ")
        wordlist = input("Enter Wordlist >> ")
        # Ignore a FileNotFoundError if we are already in the Brute_Force directory
        with contextlib.suppress(FileNotFoundError):
            os.chdir("Brute_Force")
        subprocess.run(
            ["python3", "Brute_Force.py", "-f", f"{name}", "-l", f"{wordlist}"])


class AppCheck(SecurityTool):
    TITLE = "AppCheck"
    DESCRIPTION = "AppCheck is a tool to check social media app security"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/tiameows/appcheck.git"]
    RUN_COMMANDS = ["cd appcheck && sudo python3 appcheck.py"]
    PROJECT_URL = "https://github.com/tiameows/appcheck"


class SocialMediaBruteforceTools(SecurityToolsCollection):
    TITLE = "Social Media Bruteforce Tools"
    TOOLS = [
        InstaBrute(),
        BruteForce(),
        Faceshell(),
        AppCheck()
    ]
