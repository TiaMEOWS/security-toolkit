# coding=utf-8
import os
import subprocess

from core import SecurityTool
from core import SecurityToolsCollection


class FacialFind(SecurityTool):
    TITLE = "FacialFind"
    DESCRIPTION = "FacialFind is a tool to find social media accounts using facial recognition"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/tiameows/facialfind.git"]
    RUN_COMMANDS = ["cd facialfind && sudo python3 facialfind.py"]
    PROJECT_URL = "https://github.com/tiameows/facialfind"


class FindUser(SecurityTool):
    TITLE = "FindUser"
    DESCRIPTION = "FindUser is a tool to find social media accounts"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/tiameows/finduser.git"]
    RUN_COMMANDS = ["cd finduser && sudo python3 finduser.py"]
    PROJECT_URL = "https://github.com/tiameows/finduser"


class Sherlock(SecurityTool):
    TITLE = "Sherlock"
    DESCRIPTION = "Sherlock is a tool to find usernames across social networks"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/tiameows/sherlock.git"]
    RUN_COMMANDS = ["cd sherlock && sudo python3 sherlock.py"]
    PROJECT_URL = "https://github.com/tiameows/sherlock"


class SocialScan(SecurityTool):
    TITLE = "SocialScan"
    DESCRIPTION = "SocialScan is a tool to scan social media accounts"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/tiameows/socialscan.git"]
    RUN_COMMANDS = ["cd socialscan && sudo python3 socialscan.py"]
    PROJECT_URL = "https://github.com/tiameows/socialscan"


class SocialMediaFinderTools(SecurityToolsCollection):
    TITLE = "Social Media Finder Tools"
    TOOLS = [
        FacialFind(),
        FindUser(),
        Sherlock(),
        SocialScan()
    ]
