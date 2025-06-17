# coding=utf-8
from core import SecurityTool
from core import SecurityToolsCollection


class HashBuster(SecurityTool):
    TITLE = "HashBuster"
    DESCRIPTION = "HashBuster is a tool to crack hashes"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/tiameows/hashbuster.git"]
    RUN_COMMANDS = ["cd hashbuster && sudo python3 hashbuster.py"]
    PROJECT_URL = "https://github.com/tiameows/hashbuster"


class HashCrackingTools(SecurityToolsCollection):
    TITLE = "Hash Cracking Tools"
    TOOLS = [
        HashBuster()
    ]
