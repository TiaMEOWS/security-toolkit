# coding=utf-8
from core import SecurityTool
from core import SecurityToolsCollection


class EvilURL(SecurityTool):
    TITLE = "EvilURL"
    DESCRIPTION = "EvilURL is a tool to generate homograph attack URLs"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/tiameows/evilurl.git"]
    RUN_COMMANDS = ["cd evilurl && sudo python3 evilurl.py"]
    PROJECT_URL = "https://github.com/tiameows/evilurl"


class IDNHomographAttackTools(SecurityToolsCollection):
    TITLE = "IDN Homograph Attack Tools"
    TOOLS = [
        EvilURL()
    ]
