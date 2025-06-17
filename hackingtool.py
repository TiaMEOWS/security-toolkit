#!/usr/bin/env python3
# Version 2.0.0
import os
import sys
import webbrowser
from platform import system
from time import sleep

from core import SecurityTool
from core import SecurityToolsCollection
from tools.anonsurf import AnonSurfTools
from tools.ddos import DDOSTools
from tools.exploit_frameworks import ExploitFrameworkTools
from tools.forensic_tools import ForensicTools
from tools.information_gathering_tools import InformationGatheringTools
from tools.other_tools import OtherTools
from tools.payload_creator import PayloadCreatorTools
from tools.phising_attack import PhishingAttackTools
from tools.post_exploitation import PostExploitationTools
from tools.remote_administration import RemoteAdministrationTools
from tools.reverse_engineering import ReverseEngineeringTools
from tools.sql_tools import SqlInjectionTools
from tools.steganography import SteganographyTools
from tools.tool_manager import ToolManager
from tools.webattack import WebAttackTools
from tools.wireless_attack_tools import WirelessAttackTools
from tools.wordlist_generator import WordlistGeneratorTools
from tools.xss_attack import XSSAttackTools

logo = """\033[36m
  ████████╗██╗ █████╗ ███╗   ███╗███████╗ ██████╗ ██╗    ██╗███████╗
  ╚══██╔══╝██║██╔══██╗████╗ ████║██╔════╝██╔═══██╗██║    ██║██╔════╝
     ██║   ██║███████║██╔████╔██║█████╗  ██║   ██║██║ █╗ ██║███████╗
     ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  ██║   ██║██║███╗██║╚════██║
     ██║   ██║██║  ██║██║ ╚═╝ ██║███████╗╚██████╔╝╚███╔███╔╝███████║
     ╚═╝   ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝ ╚═════╝  ╚══╝╚══╝ ╚══════╝
                                                                      
                                    \033[34m[✔] https://github.com/tiameows   [✔]
                                    \033[34m[✔]            Version 2.0.0     [✔]
                                    \033[91m[X] Advanced Security Toolkit    [X]
\033[97m """

# New features and tools
all_tools = [
    AnonSurfTools(),
    InformationGatheringTools(),
    WordlistGeneratorTools(),
    WirelessAttackTools(),
    SqlInjectionTools(),
    PhishingAttackTools(),
    WebAttackTools(),
    PostExploitationTools(),
    ForensicTools(),
    PayloadCreatorTools(),
    ExploitFrameworkTools(),
    ReverseEngineeringTools(),
    DDOSTools(),
    RemoteAdministrationTools(),
    XSSAttackTools(),
    SteganographyTools(),
    OtherTools(),
    ToolManager()
]

class AllTools(SecurityToolsCollection):
    TITLE = "Tiameows Security Toolkit"
    TOOLS = all_tools

    def show_info(self):
        print(logo + '\033[0m \033[97m')
        print("\033[92m[+] New Features in v2.0.0:")
        print("    - Enhanced UI/UX")
        print("    - Improved tool organization")
        print("    - Better error handling")
        print("    - New security features\033[97m")

def main():
    tools = SecurityToolsCollection()
    tools.run()

if __name__ == "__main__":
    try:
        if system() == 'Linux':
            fpath = os.path.expanduser("~/tiameows_toolkit_path.txt")
            if not os.path.exists(fpath):
                os.system('clear')
                print("""
                        [@] Set Installation Path
                        [1] Manual 
                        [2] Default
                """)
                choice = input("Tiameows =>> ").strip()

                if choice == "1":
                    inpath = input("Enter Path (with Directory Name) >> ").strip()
                    with open(fpath, "w") as f:
                        f.write(inpath)
                    print("Successfully Set Path to: {}".format(inpath))
                elif choice == "2":
                    autopath = "/home/tiameows_toolkit/"
                    with open(fpath, "w") as f:
                        f.write(autopath)
                    print("Your Default Path Is: {}".format(autopath))
                    sleep(3)
                else:
                    print("Invalid choice. Please try again.")
                    sys.exit(0)

            with open(fpath) as f:
                archive = f.readline()
                os.makedirs(archive, exist_ok=True)
                os.chdir(archive)
                AllTools().show_options()

        elif system() == "Windows":
            print(
                r"\033[91m For optimal performance, please run this tool on a Debian-based system\e[00m"
            )
            sleep(2)
            webbrowser.open_new_tab("https://github.com/tiameows")

        else:
            print("Unsupported operating system. Please check compatibility.")

    except KeyboardInterrupt:
        print("\nExiting Tiameows Security Toolkit...")
        sleep(2)

    main()
