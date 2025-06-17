# coding=utf-8
import os
import subprocess

from core import SecurityTool
from core import SecurityToolsCollection


class Dalfox(SecurityTool):
    TITLE = "DalFox(Finder of XSS)"
    DESCRIPTION = "DalFox is a powerful open-source XSS scanner and parameter analyzer"
    INSTALL_COMMANDS = ["sudo go install github.com/hahwul/dalfox/v2@latest"]
    RUN_COMMANDS = ["dalfox"]
    PROJECT_URL = "https://github.com/hahwul/dalfox"


class XSSPayloadGenerator(SecurityTool):
    TITLE = "XSS Payload Generator"
    DESCRIPTION = "XSS Payload Generator"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/capture0x/XSS-LOADER.git"]
    RUN_COMMANDS = ["cd XSS-LOADER && sudo python3 xssloader.py"]
    PROJECT_URL = "https://github.com/capture0x/XSS-LOADER.git"


class XSSFinder(SecurityTool):
    TITLE = "Extended XSS Searcher and Finder"
    DESCRIPTION = "Cross-Site Scripting (XSS) Scanner"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/Damian89/extended-xss-search.git"]
    RUN_COMMANDS = ["cd extended-xss-search && sudo python3 extended-xss-search.py"]
    PROJECT_URL = "https://github.com/Damian89/extended-xss-search"

    def after_install(self):
        print("""\033[96m 
        Follow This Steps After Installation:-
            \033[31m [*] Go To extended-xss-search directory,
                and Rename the example.app-settings.conf to app-settings.conf
        """)
        input("Press ENTER to continue")

    def run(self):
        print("""\033[96m 
        You have To Add Links to scan
        \033[31m[!] Go to extended-xss-search
            [*] config/urls-to-test.txt
            [!] python3 extended-xss-search.py
        """)


class XSSFreak(SecurityTool):
    TITLE = "XSS-Freak"
    DESCRIPTION = "XSS-Freak is an XSS scanner"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/PR0PH3CY33/XSS-Freak.git"]
    RUN_COMMANDS = ["cd XSS-Freak && sudo python3 XSS-Freak.py"]
    PROJECT_URL = "https://github.com/PR0PH3CY33/XSS-Freak"


class XSpear(SecurityTool):
    TITLE = "XSpear"
    DESCRIPTION = "XSpear is a powerful XSS Scanning and Parameter analysis tool"
    INSTALL_COMMANDS = ["sudo gem install XSpear"]
    RUN_COMMANDS = ["XSpear"]
    PROJECT_URL = "https://github.com/hahwul/XSpear"


class XSSCon(SecurityTool):
    TITLE = "XSSCon"
    DESCRIPTION = "XSSCon is a simple XSS scanner tool"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/menkrep1337/XSSCon.git"]
    RUN_COMMANDS = ["cd XSSCon && sudo python3 xsscon.py"]
    PROJECT_URL = "https://github.com/menkrep1337/XSSCon"


class XanXSS(SecurityTool):
    TITLE = "XanXSS"
    DESCRIPTION = "XanXSS is a reflected XSS searching tool"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/Ekultek/XanXSS.git"]
    RUN_COMMANDS = ["cd XanXSS && sudo python3 xanxss.py"]
    PROJECT_URL = "https://github.com/Ekultek/XanXSS"


class XSSStrike(SecurityTool):
    TITLE = "Advanced XSS Detection Suite"
    DESCRIPTION = "XSStrike is a Cross Site Scripting detection suite"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/UltimateHackers/XSStrike.git"]
    RUN_COMMANDS = ["cd XSStrike && sudo python3 xsstrike"]
    PROJECT_URL = "https://github.com/UltimateHackers/XSStrike"


class RVuln(SecurityTool):
    TITLE = "RVuln"
    DESCRIPTION = "RVuln is a simple tool to help you to detect XSS, SQLi and other vulnerabilities"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/iinc0gnit0/RVuln.git"]
    RUN_COMMANDS = ["cd RVuln && sudo python3 rvuln.py"]
    PROJECT_URL = "https://github.com/iinc0gnit0/RVuln"


class XSSAttackTools(SecurityToolsCollection):
    TITLE = "XSS Attack Tools"
    TOOLS = [
        Dalfox(),
        XSSPayloadGenerator(),
        XSSFinder(),
        XSSFreak(),
        XSpear(),
        XSSCon(),
        XanXSS(),
        XSSStrike(),
        RVuln()
    ]
