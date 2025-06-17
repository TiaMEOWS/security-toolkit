# coding=utf-8
import os
import sys
from time import sleep

from core import SecurityTool
from core import SecurityToolsCollection


class UpdateTool(SecurityTool):
    TITLE = "Update Security Toolkit"
    DESCRIPTION = "Update Security Toolkit"
    RUN_COMMANDS = [
        "sudo rm -rf /usr/share/doc/security-toolkit/;",
        "sudo rm -rf /etc/security-toolkit/;",
        "mkdir security-toolkit;",
        "cd security-toolkit;",
        "git clone https://github.com/tiameows/security-toolkit.git;",
        "cd security-toolkit;",
        "sudo chmod +x install.sh;",
        "sudo bash install.sh;"
    ]


class UninstallTool(SecurityTool):
    TITLE = "Uninstall Security Toolkit"
    DESCRIPTION = "Uninstall Security Toolkit"
    RUN_COMMANDS = [
        "sudo rm -rf /usr/share/doc/security-toolkit/;",
        "sudo rm -rf /etc/security-toolkit/;"
    ]

    def run(self):
        print("security-toolkit started to uninstall..\n")
        super().run()
        print("\nSecurity Toolkit Successfully Uninstalled... Goodbye.")


class ToolManager(SecurityTool):
    TITLE = "Tool Manager"
    DESCRIPTION = "Tool Manager is a tool to manage security tools"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/tiameows/security-toolkit.git"]
    RUN_COMMANDS = ["cd security-toolkit && sudo python3 tool_manager.py"]
    PROJECT_URL = "https://github.com/tiameows/security-toolkit"


class ToolManagerTools(SecurityToolsCollection):
    TITLE = "Tool Manager Tools"
    TOOLS = [
        ToolManager()
    ]
