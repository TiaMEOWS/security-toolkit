import os

from core import SecurityTool
from core import SecurityToolsCollection


class TheFatRat(SecurityTool):
    TITLE = "The FatRat"
    DESCRIPTION = "TheFatRat Provides An Easy way to create Backdoors and \n" \
                  "Payload which can bypass most anti-virus"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/Screetsec/TheFatRat.git",
        "cd TheFatRat && sudo chmod +x setup.sh"
    ]
    RUN_COMMANDS = ["cd TheFatRat && sudo bash setup.sh"]
    PROJECT_URL = "https://github.com/Screetsec/TheFatRat"

    def __init__(self):
        super(TheFatRat, self).__init__([
            ('Update', self.update),
            ('Troubleshoot', self.troubleshoot)
        ])

    def update(self):
        os.system(
            "cd TheFatRat && bash update && chmod +x setup.sh && bash setup.sh")

    def troubleshoot(self):
        os.system("cd TheFatRat && sudo chmod +x chk_tools && ./chk_tools")


class Brutal(SecurityTool):
    TITLE = "Brutal"
    DESCRIPTION = "Brutal is a toolkit to quickly create various payload," \
                  "powershell attack,\nvirus attack and launch listener for " \
                  "a Human Interface Device"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/Screetsec/Brutal.git",
        "cd Brutal && sudo chmod +x Brutal.sh"
    ]
    RUN_COMMANDS = ["cd Brutal && sudo bash Brutal.sh"]
    PROJECT_URL = "https://github.com/Screetsec/Brutal"

    def show_info(self):
        super(Brutal, self).show_info()
        print("""
        [!] Requirement
            >> Arduino Software (I used v1.6.7)
            >> TeensyDuino
            >> Linux udev rules
            >> Copy and paste the PaensyLib folder inside your Arduino libraries
    
        [!] Kindly Visit below link for Installation for Arduino 
            >> https://github.com/Screetsec/Brutal/wiki/Install-Requirements 
        """)


class Stitch(SecurityTool):
    TITLE = "Stitch"
    DESCRIPTION = "Stitch is Cross Platform Python Remote Administrator Tool\n\t" \
                  "[!] Refer Below Link For Wins & MAc Os"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/nathanlopez/Stitch.git",
        "cd Stitch && sudo pip install -r lnx_requirements.txt"
    ]
    RUN_COMMANDS = ["cd Stitch && sudo python main.py"]
    PROJECT_URL = "https://nathanlopez.github.io/Stitch"


class MSFVenom(SecurityTool):
    TITLE = "MSFVenom"
    DESCRIPTION = "MSFVenom is a tool to generate and encode payloads"
    INSTALL_COMMANDS = ["sudo apt-get install metasploit-framework"]
    RUN_COMMANDS = ["msfvenom"]
    PROJECT_URL = "https://github.com/rapid7/metasploit-framework"


class Venom(SecurityTool):
    TITLE = "Venom Shellcode Generator"
    DESCRIPTION = "venom 1.0.11 (malicious_server) was build to take " \
                  "advantage of \n apache2 webserver to deliver payloads " \
                  "(LAN) using a fake webpage written in html"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/r00t-3xp10it/venom.git",
        "sudo chmod -R 775 venom*/ && cd venom*/ && cd aux && sudo bash setup.sh",
        "sudo ./venom.sh -u"
    ]
    RUN_COMMANDS = ["cd venom && sudo ./venom.sh"]
    PROJECT_URL = "https://github.com/r00t-3xp10it/venom"


class Spycam(SecurityTool):
    TITLE = "Spycam"
    DESCRIPTION = "Script to generate a Win32 payload that takes the webcam " \
                  "image every 1 minute and send it to the attacker"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/indexnotfound404/spycam.git",
        "cd spycam && bash install.sh && chmod +x spycam"
    ]
    RUN_COMMANDS = ["cd spycam && ./spycam"]
    PROJECT_URL = "https://github.com/indexnotfound404/spycam"


class MobDroid(SecurityTool):
    TITLE = "Mob-Droid"
    DESCRIPTION = "Mob-Droid helps you to generate metasploit payloads in " \
                  "easy way\n without typing long commands and save your time"
    INSTALL_COMMANDS = [
        "git clone https://github.com/kinghacker0/mob-droid.git"]
    RUN_COMMANDS = ["cd mob-droid;sudo python mob-droid.py"]
    PROJECT_URL = "https://github.com/kinghacker0/Mob-Droid"


class Enigma(SecurityTool):
    TITLE = "Enigma"
    DESCRIPTION = "Enigma is a Multiplatform payload dropper"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/UndeadSec/Enigma.git"]
    RUN_COMMANDS = ["cd Enigma;sudo python enigma.py"]
    PROJECT_URL = "https://github.com/UndeadSec/Enigma"


class PayloadCreator(SecurityTool):
    TITLE = "Payload Creator"
    DESCRIPTION = "Payload Creator is a tool to create custom payloads"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/tiameows/payload-creator.git"]
    RUN_COMMANDS = ["cd payload-creator && sudo python3 payload-creator.py"]
    PROJECT_URL = "https://github.com/tiameows/payload-creator"


class PayloadCreatorTools(SecurityToolsCollection):
    TITLE = "Payload Creator Tools"
    TOOLS = [
        TheFatRat(),
        Brutal(),
        Stitch(),
        MSFVenom(),
        Venom(),
        Spycam(),
        MobDroid(),
        Enigma(),
        PayloadCreator()
    ]
