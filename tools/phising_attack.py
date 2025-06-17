# coding=utf-8
import os

from core import SecurityTool
from core import SecurityToolsCollection

class autophisher(SecurityTool):
    TITLE = "Autophisher RK"
    DESCRIPTION = "Automated Phishing Toolkit"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/CodingRanjith/autophisher.git",
        "cd autophisher"
    ]
    RUN_COMMANDS = ["cd autophisher;sudo bash autophisher.sh"]
    PROJECT_URL = "https://github.com/CodingRanjith/autophisher"
    
class Pyphisher(SecurityTool):
    TITLE = "Pyphisher"
    DESCRIPTION = "Easy to use phishing tool with 77 website templates"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/KasRoudra/PyPhisher",
        "cd PyPhisher/files",
        "pip3 install -r requirements.txt"
    ]
    RUN_COMMANDS = ["cd PyPhisher;sudo python3 pyphisher.py"]
    PROJECT_URL = "git clone https://github.com/KasRoudra/PyPhisher"    
    
class AdvPhishing(SecurityTool):
    TITLE = "AdvPhishing"
    DESCRIPTION = "This is Advance Phishing Tool ! OTP PHISHING"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/Ignitetch/AdvPhishing.git",
        "cd AdvPhishing;chmod 777 *;bash Linux-Setup.sh"]
    RUN_COMMANDS = ["cd AdvPhishing && sudo bash AdvPhishing.sh"]
    PROJECT_URL = "https://github.com/Ignitetch/AdvPhishing"      

class Setoolkit(SecurityTool):
    TITLE = "Setoolkit"
    DESCRIPTION = "The Social-Engineer Toolkit is an open-source penetration\n" \
                  "testing framework designed for social engine"
    INSTALL_COMMANDS = [
        "git clone https://github.com/trustedsec/social-engineer-toolkit/",
        "cd social-engineer-toolkit && sudo python3 setup.py"
    ]
    RUN_COMMANDS = ["sudo setoolkit"]
    PROJECT_URL = "https://github.com/trustedsec/social-engineer-toolkit"


class SocialFish(SecurityTool):
    TITLE = "SocialFish"
    DESCRIPTION = "Automated Phishing Tool & Information Collector NOTE: username is 'root' and password is 'pass'"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/UndeadSec/SocialFish.git && sudo apt-get install python3 python3-pip python3-dev -y",
        "cd SocialFish && sudo python3 -m pip install -r requirements.txt"
    ]
    RUN_COMMANDS = ["cd SocialFish && sudo python3 SocialFish.py root pass"]
    PROJECT_URL = "https://github.com/UndeadSec/SocialFish"


class HiddenEye(SecurityTool):
    TITLE = "HiddenEye"
    DESCRIPTION = "Modern Phishing Tool With Advanced Functionality And " \
                  "Multiple Tunnelling Services \n" \
                  "\t [!]https://github.com/DarkSecDevelopers/HiddenEye"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/Morsmalleo/HiddenEye.git ;sudo chmod 777 HiddenEye",
        "cd HiddenEye;sudo pip3 install -r requirements.txt;sudo pip3 install requests;pip3 install pyngrok"
    ]
    RUN_COMMANDS = ["cd HiddenEye;sudo python3 HiddenEye.py"]
    PROJECT_URL = "https://github.com/Morsmalleo/HiddenEye.git"


class Evilginx2(SecurityTool):
    TITLE = "Evilginx2"
    DESCRIPTION = "evilginx2 is a man-in-the-middle attack framework used " \
                  "for phishing login credentials along with session cookies,\n" \
                  "which in turn allows to bypass 2-factor authentication protection.\n\n\t " \
                  "[+]Make sure you have installed GO of version at least 1.14.0 \n" \
                  "[+]After installation, add this to your ~/.profile, assuming that you installed GO in /usr/local/go\n\t " \
                  "[+]export GOPATH=$HOME/go \n " \
                  "[+]export PATH=$PATH:/usr/local/go/bin:$GOPATH/bin \n" \
                  "[+]Then load it with source ~/.profiles."
    INSTALL_COMMANDS = [
        "sudo apt-get install git make;go get -u github.com/kgretzky/evilginx2",
        "cd $GOPATH/src/github.com/kgretzky/evilginx2;make",
        "sudo make install;sudo evilginx"
    ]
    RUN_COMMANDS = ["sudo evilginx"]
    PROJECT_URL = "https://github.com/kgretzky/evilginx2"


class ISeeYou(SecurityTool):
    TITLE = "I-See_You"
    DESCRIPTION = "[!] ISeeYou is a tool to find Exact Location of Victom By" \
                  " User SocialEngineering or Phishing Engagement..\n" \
                  "[!] Users can expose their local servers to the Internet " \
                  "and decode the location coordinates by looking at the log file"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/Viralmaniar/I-See-You.git",
        "cd I-See-You && sudo chmod u+x ISeeYou.sh"
    ]
    RUN_COMMANDS = ["cd I-See-You && sudo bash ISeeYou.sh"]
    PROJECT_URL = "https://github.com/Viralmaniar/I-See-You"


class SayCheese(SecurityTool):
    TITLE = "SayCheese"
    DESCRIPTION = "Take webcam shots from target just sending a malicious link"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/hangetzzu/saycheese"]
    RUN_COMMANDS = ["cd saycheese && sudo bash saycheese.sh"]
    PROJECT_URL = "https://github.com/hangetzzu/saycheese"


class QRJacking(SecurityTool):
    TITLE = "QR Code Jacking"
    DESCRIPTION = "QR Code Jacking (Any Website)"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/cryptedwolf/ohmyqr.git && sudo apt -y install scrot"]
    RUN_COMMANDS = ["cd ohmyqr && sudo bash ohmyqr.sh"]
    PROJECT_URL = "https://github.com/cryptedwolf/ohmyqr"
    
class WifiPhisher(SecurityTool):
    TITLE = "WifiPhisher"
    DESCRIPTION = "The Rogue Access Point Framework"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/wifiphisher/wifiphisher.git",
        "cd wifiphisher"]
    RUN_COMMANDS = ["cd wifiphisher && sudo python setup.py"]
    PROJECT_URL = "https://github.com/wifiphisher/wifiphisher"   
    
class BlackEye(SecurityTool):
    TITLE = "BlackEye"
    DESCRIPTION = "The ultimate phishing tool with 38 websites available!"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/thelinuxchoice/blackeye",
        "cd blackeye "]
    RUN_COMMANDS = ["cd blackeye && sudo bash blackeye.sh"]
    PROJECT_URL = "https://github.com/An0nUD4Y/blackeye"      

class ShellPhish(SecurityTool):
    TITLE = "ShellPhish"
    DESCRIPTION = "Phishing Tool for 18 social media"
    INSTALL_COMMANDS = ["git clone https://github.com/An0nUD4Y/shellphish.git"]
    RUN_COMMANDS = ["cd shellphish;sudo bash shellphish.sh"]
    PROJECT_URL = "https://github.com/An0nUD4Y/shellphish"
    
class Thanos(SecurityTool):
    TITLE = "Thanos"
    DESCRIPTION = "Thanos is a phishing tool"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/tiameows/thanos.git"]
    RUN_COMMANDS = ["cd thanos && sudo python3 thanos.py"]
    PROJECT_URL = "https://github.com/tiameows/thanos"
    
class QRLJacking(SecurityTool):
    TITLE = "QRLJacking"
    DESCRIPTION = "QRLJacking is a tool for QR code jacking"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/tiameows/qrljacking.git"]
    RUN_COMMANDS = ["cd qrljacking && sudo python3 qrljacking.py"]
    PROJECT_URL = "https://github.com/tiameows/qrljacking"
    
class Maskphish(SecurityTool):
    TITLE = "Maskphish"
    DESCRIPTION = "Maskphish is a tool to mask phishing URLs"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/tiameows/maskphish.git"]
    RUN_COMMANDS = ["cd maskphish && sudo python3 maskphish.py"]
    PROJECT_URL = "https://github.com/tiameows/maskphish"

class BlackPhish(SecurityTool):
    TITLE = "BlackPhish"
    DESCRIPTION = "BlackPhish is a tool for phishing attacks"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/tiameows/blackphish.git"]
    RUN_COMMANDS = ["cd blackphish && sudo python3 blackphish.py"]
    PROJECT_URL = "https://github.com/tiameows/blackphish"

class dnstwist(SecurityTool):
    Title='dnstwist'
    Install_commands=['sudo git clone https://github.com/elceef/dnstwist.git','cd dnstwist']
    Run_commands=['cd dnstwist;sudo python3 dnstwist.py']
    project_url='https://github.com/elceef/dnstwist'

class DNSTwist(SecurityTool):
    TITLE = "DNSTwist"
    DESCRIPTION = "DNSTwist is a tool to find similar domain names"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/tiameows/dnstwist.git"]
    RUN_COMMANDS = ["cd dnstwist && sudo python3 dnstwist.py"]
    PROJECT_URL = "https://github.com/tiameows/dnstwist"

class PhishingAttackTools(SecurityToolsCollection):
    TITLE = "Phishing Attack Tools"
    TOOLS = [
        autophisher(),
        Pyphisher(),
        AdvPhishing(),
        Setoolkit(),
        SocialFish(),
        HiddenEye(),
        Evilginx2(),
        ISeeYou(),
        SayCheese(),
        QRJacking(),
        BlackEye(),
        ShellPhish(),
        Thanos(),
        QRLJacking(),
        Maskphish(),
        BlackPhish(),
        dnstwist(),
        DNSTwist()
    ]
