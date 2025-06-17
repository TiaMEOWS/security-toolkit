# coding=utf-8
from core import SecurityTool
from core import SecurityToolsCollection


class KnockMail(SecurityTool):
    TITLE = "KnockMail"
    DESCRIPTION = "KnockMail is a tool to verify email addresses"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/tiameows/knockmail.git"]
    RUN_COMMANDS = ["cd knockmail && sudo python3 knockmail.py"]
    PROJECT_URL = "https://github.com/tiameows/knockmail"


class EmailVerifyTools(SecurityToolsCollection):
    TITLE = "Email Verification Tools"
    TOOLS = [
        KnockMail()
    ]
    
