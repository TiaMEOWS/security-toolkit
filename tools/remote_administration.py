# coding=utf-8
from core import SecurityTool
from core import SecurityToolsCollection


class SSH(SecurityTool):
    TITLE = "SSH"
    DESCRIPTION = "SSH is a secure shell client for remote administration"
    INSTALL_COMMANDS = ["sudo apt-get install openssh-client"]
    RUN_COMMANDS = ["ssh"]
    PROJECT_URL = "https://www.openssh.com/"


class RDP(SecurityTool):
    TITLE = "RDP"
    DESCRIPTION = "RDP is a remote desktop protocol client"
    INSTALL_COMMANDS = ["sudo apt-get install rdesktop"]
    RUN_COMMANDS = ["rdesktop"]
    PROJECT_URL = "https://www.rdesktop.org/"


class RemoteAdministrationTools(SecurityToolsCollection):
    TITLE = "Remote Administration Tools"
    TOOLS = [
        SSH(),
        RDP()
    ]
