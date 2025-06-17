# coding=utf-8
import os
import socket
import subprocess
import webbrowser

from core import SecurityTool
from core import SecurityToolsCollection
from core import clear_screen


class NMAP(SecurityTool):
    TITLE = "NMAP"
    DESCRIPTION = "NMAP is a network mapper"
    INSTALL_COMMANDS = ["sudo apt-get install nmap"]
    RUN_COMMANDS = ["nmap"]
    PROJECT_URL = "https://github.com/nmap/nmap"


class Dracnmap(SecurityTool):
    TITLE = "Dracnmap"
    DESCRIPTION = "Dracnmap is a tool to automate NMAP scans"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/tiameows/dracnmap.git"]
    RUN_COMMANDS = ["cd dracnmap && sudo python3 dracnmap.py"]
    PROJECT_URL = "https://github.com/tiameows/dracnmap"


class PortScan(SecurityTool):
    TITLE = "PortScan"
    DESCRIPTION = "PortScan is a tool to scan ports"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/tiameows/portscan.git"]
    RUN_COMMANDS = ["cd portscan && sudo python3 portscan.py"]
    PROJECT_URL = "https://github.com/tiameows/portscan"


class Host2IP(SecurityTool):
    TITLE = "Host2IP"
    DESCRIPTION = "Host2IP is a tool to resolve hostnames to IP addresses"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/tiameows/host2ip.git"]
    RUN_COMMANDS = ["cd host2ip && sudo python3 host2ip.py"]
    PROJECT_URL = "https://github.com/tiameows/host2ip"


class XeroSploit(SecurityTool):
    TITLE = "XeroSploit"
    DESCRIPTION = "XeroSploit is a penetration testing toolkit"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/tiameows/xerosploit.git"]
    RUN_COMMANDS = ["cd xerosploit && sudo python3 xerosploit.py"]
    PROJECT_URL = "https://github.com/tiameows/xerosploit"


class RedHawk(SecurityTool):
    TITLE = "RedHawk"
    DESCRIPTION = "RedHawk is a tool for information gathering"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/tiameows/redhawk.git"]
    RUN_COMMANDS = ["cd redhawk && sudo python3 redhawk.py"]
    PROJECT_URL = "https://github.com/tiameows/redhawk"


class ReconSpider(SecurityTool):
    TITLE = "ReconSpider"
    DESCRIPTION = "ReconSpider is a tool for reconnaissance"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/tiameows/reconspider.git"]
    RUN_COMMANDS = ["cd reconspider && sudo python3 reconspider.py"]
    PROJECT_URL = "https://github.com/tiameows/reconspider"


class IsItDown(SecurityTool):
    TITLE = "IsItDown"
    DESCRIPTION = "IsItDown is a tool to check if websites are down"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/tiameows/isitdown.git"]
    RUN_COMMANDS = ["cd isitdown && sudo python3 isitdown.py"]
    PROJECT_URL = "https://github.com/tiameows/isitdown"


class Infoga(SecurityTool):
    TITLE = "Infoga"
    DESCRIPTION = "Infoga is a tool for email reconnaissance"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/tiameows/infoga.git"]
    RUN_COMMANDS = ["cd infoga && sudo python3 infoga.py"]
    PROJECT_URL = "https://github.com/tiameows/infoga"


class ReconDog(SecurityTool):
    TITLE = "ReconDog"
    DESCRIPTION = "ReconDog is a tool for reconnaissance"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/tiameows/recondog.git"]
    RUN_COMMANDS = ["cd recondog && sudo python3 recondog.py"]
    PROJECT_URL = "https://github.com/tiameows/recondog"


class Striker(SecurityTool):
    TITLE = "Striker"
    DESCRIPTION = "Striker is a tool for reconnaissance"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/tiameows/striker.git"]
    RUN_COMMANDS = ["cd striker && sudo python3 striker.py"]
    PROJECT_URL = "https://github.com/tiameows/striker"


class SecretFinder(SecurityTool):
    TITLE = "SecretFinder"
    DESCRIPTION = "SecretFinder is a tool to find secrets"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/tiameows/secretfinder.git"]
    RUN_COMMANDS = ["cd secretfinder && sudo python3 secretfinder.py"]
    PROJECT_URL = "https://github.com/tiameows/secretfinder"


class Shodan(SecurityTool):
    TITLE = "Shodan"
    DESCRIPTION = "Shodan is a search engine for Internet-connected devices"
    INSTALL_COMMANDS = ["sudo pip3 install shodan"]
    RUN_COMMANDS = ["shodan"]
    PROJECT_URL = "https://github.com/tiameows/shodan"


class PortScannerRanger(SecurityTool):
    TITLE = "PortScannerRanger"
    DESCRIPTION = "PortScannerRanger is a tool to scan ports"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/tiameows/portscannerranger.git"]
    RUN_COMMANDS = ["cd portscannerranger && sudo python3 portscannerranger.py"]
    PROJECT_URL = "https://github.com/tiameows/portscannerranger"


class Breacher(SecurityTool):
    TITLE = "Breacher"
    DESCRIPTION = "Breacher is a tool for information gathering"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/tiameows/breacher.git"]
    RUN_COMMANDS = ["cd breacher && sudo python3 breacher.py"]
    PROJECT_URL = "https://github.com/tiameows/breacher"


class InformationGatheringTools(SecurityToolsCollection):
    TITLE = "Information Gathering Tools"
    TOOLS = [
        NMAP(),
        Dracnmap(),
        PortScan(),
        Host2IP(),
        XeroSploit(),
        RedHawk(),
        ReconSpider(),
        IsItDown(),
        Infoga(),
        ReconDog(),
        Striker(),
        SecretFinder(),
        Shodan(),
        PortScannerRanger(),
        Breacher()
    ]
