# coding=utf-8
import subprocess

from core import SecurityTool
from core import SecurityToolsCollection


class Web2Attack(SecurityTool):
    TITLE = "Web2Attack"
    DESCRIPTION = "Web2Attack is a tool for Web Attack"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/santatic/web2attack.git"]
    RUN_COMMANDS = ["cd web2attack && sudo python3 web2attack.py"]
    PROJECT_URL = "https://github.com/santatic/web2attack"


class Skipfish(SecurityTool):
    TITLE = "Skipfish"
    DESCRIPTION = "Skipfish is an active web application security reconnaissance tool"
    INSTALL_COMMANDS = ["sudo apt-get install skipfish"]
    RUN_COMMANDS = ["skipfish"]
    PROJECT_URL = "https://github.com/spinkham/skipfish"


class SubDomainFinder(SecurityTool):
    TITLE = "SubDomain Finder"
    DESCRIPTION = "Sublist3r is a python tool designed to enumerate subdomains of websites"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/aboul3la/Sublist3r.git"]
    RUN_COMMANDS = ["cd Sublist3r && sudo python3 sublist3r.py"]
    PROJECT_URL = "https://github.com/aboul3la/Sublist3r"


class CheckURL(SecurityTool):
    TITLE = "CheckURL"
    DESCRIPTION = "CheckURL is a tool to check URL status"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/UndeadSec/checkURL.git"]
    RUN_COMMANDS = ["cd checkURL && sudo python3 checkurl.py"]
    PROJECT_URL = "https://github.com/UndeadSec/checkURL"


class Blazy(SecurityTool):
    TITLE = "Blazy"
    DESCRIPTION = "Blazy is a tool to find clickjacking and XSS vulnerabilities"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/UltimateHackers/Blazy.git"]
    RUN_COMMANDS = ["cd Blazy && sudo python3 blazy.py"]
    PROJECT_URL = "https://github.com/UltimateHackers/Blazy"


class SubDomainTakeOver(SecurityTool):
    TITLE = "Sub-Domain TakeOver"
    DESCRIPTION = "Sub-Domain TakeOver is a tool to check subdomain takeover"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/edoardottt/takeover.git"]
    RUN_COMMANDS = ["cd takeover && sudo python3 takeover.py"]
    PROJECT_URL = "https://github.com/edoardottt/takeover"


class Dirb(SecurityTool):
    TITLE = "Dirb"
    DESCRIPTION = "Dirb is a Web Content Scanner"
    INSTALL_COMMANDS = ["sudo apt-get install dirb"]
    RUN_COMMANDS = ["dirb"]
    PROJECT_URL = "https://gitlab.com/kalilinux/packages/dirb"


class WebAttackTools(SecurityToolsCollection):
    TITLE = "Web Attack Tools"
    TOOLS = [
        Web2Attack(),
        Skipfish(),
        SubDomainFinder(),
        CheckURL(),
        Blazy(),
        SubDomainTakeOver(),
        Dirb()
    ]
