# coding=utf-8
from core import SecurityTool
from core import SecurityToolsCollection


class SQLMap(SecurityTool):
    TITLE = "SQLMap"
    DESCRIPTION = "SQLMap is an open source penetration testing tool that automates the process of detecting and exploiting SQL injection flaws"
    INSTALL_COMMANDS = ["sudo apt-get install sqlmap"]
    RUN_COMMANDS = ["sqlmap"]
    PROJECT_URL = "https://github.com/sqlmapproject/sqlmap"


class NoSQLMap(SecurityTool):
    TITLE = "NoSQLMap"
    DESCRIPTION = "NoSQLMap is an open source Python tool designed to audit for as well as automate injection attacks and exploit default configuration weaknesses in NoSQL databases"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/codingo/NoSQLMap.git"]
    RUN_COMMANDS = ["cd NoSQLMap && sudo python3 nosqlmap.py"]
    PROJECT_URL = "https://github.com/codingo/NoSQLMap"


class SQLiScanner(SecurityTool):
    TITLE = "Damn Small SQLi Scanner"
    DESCRIPTION = "Damn Small SQLi Scanner (DSSS) is a fully functional SQL " \
                  "injection\nvulnerability scanner also supporting GET and " \
                  "POST parameters.\n" \
                  "[*]python3 dsss.py -h[help] | -u[URL]"
    INSTALL_COMMANDS = ["git clone https://github.com/stamparm/DSSS.git"]
    PROJECT_URL = "https://github.com/stamparm/DSSS"

    def __init__(self):
        super(SQLiScanner, self).__init__(runnable = False)


class Explo(SecurityTool):
    TITLE = "Explo"
    DESCRIPTION = "Explo is a simple tool to describe web security issues " \
                  "in a human and machine readable format.\n " \
                  "Usage:- \n " \
                  "[1] explo [--verbose|-v] testcase.yaml \n " \
                  "[2] explo [--verbose|-v] examples/*.yaml"
    INSTALL_COMMANDS = [
        "git clone https://github.com/dtag-dev-sec/explo.git",
        "cd explo;sudo python setup.py install"
    ]
    PROJECT_URL = "https://github.com/dtag-dev-sec/explo"

    def __init__(self):
        super(Explo, self).__init__(runnable = False)


class Blisqy(SecurityTool):
    TITLE = "Blisqy - Exploit Time-based blind-SQL injection"
    DESCRIPTION = "Blisqy is a tool to aid Web Security researchers to find " \
                  "Time-based Blind SQL injection \n on HTTP Headers and also " \
                  "exploitation of the same vulnerability.\n " \
                  "For Usage >> \n"
    INSTALL_COMMANDS = ["git clone https://github.com/JohnTroony/Blisqy.git"]
    PROJECT_URL = "https://github.com/JohnTroony/Blisqy"

    def __init__(self):
        super(Blisqy, self).__init__(runnable = False)


class Leviathan(SecurityTool):
    TITLE = "Leviathan - Wide Range Mass Audit Toolkit"
    DESCRIPTION = "Leviathan is a mass audit toolkit which has wide range " \
                  "service discovery,\nbrute force, SQL injection detection " \
                  "and running custom exploit capabilities. \n " \
                  "[*] It Requires API Keys \n " \
                  "More Usage [!] https://github.com/utkusen/leviathan/wiki"
    INSTALL_COMMANDS = [
        "git clone https://github.com/leviathan-framework/leviathan.git",
        "cd leviathan;sudo pip install -r requirements.txt"
    ]
    RUN_COMMANDS = ["cd leviathan;python leviathan.py"]
    PROJECT_URL = "https://github.com/leviathan-framework/leviathan"


class SQLScan(SecurityTool):
    TITLE = "SQLScan"
    DESCRIPTION = "sqlscan is quick web scanner for find an sql inject point." \
                  " not for educational, this is for hacking."
    INSTALL_COMMANDS = [
        "sudo apt install php php-bz2 php-curl php-mbstring curl",
        "sudo curl https://raw.githubusercontent.com/Cvar1984/sqlscan/dev/build/main.phar --output /usr/local/bin/sqlscan",
        "chmod +x /usr/local/bin/sqlscan"
    ]
    RUN_COMMANDS = ["sudo sqlscan"]
    PROJECT_URL = "https://github.com/Cvar1984/sqlscan"


class SQLTools(SecurityToolsCollection):
    TITLE = "SQL Tools"
    TOOLS = [
        SQLMap(),
        NoSQLMap(),
        SQLiScanner(),
        Explo(),
        Blisqy(),
        Leviathan(),
        SQLScan()
    ]
