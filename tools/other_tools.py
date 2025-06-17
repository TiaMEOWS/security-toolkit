# coding=utf-8
import os
import subprocess

from core import SecurityTool
from core import SecurityToolsCollection
from tools.others.android_attack import AndroidAttackTools
from tools.others.email_verifier import EmailVerifyTools
from tools.others.hash_crack import HashCrackingTools
from tools.others.homograph_attacks import IDNHomographAttackTools
from tools.others.mix_tools import MixTools
from tools.others.payload_injection import PayloadInjectorTools
from tools.others.socialmedia import SocialMediaBruteforceTools
from tools.others.socialmedia_finder import SocialMediaFinderTools
from tools.others.web_crawling import WebCrawlingTools
from tools.others.wifi_jamming import WifiJammingTools


class HatCloud(SecurityTool):
    TITLE = "HatCloud(Bypass CloudFlare for IP)"
    DESCRIPTION = "HatCloud build in Ruby. It makes bypass in CloudFlare for " \
                  "discover real IP."
    INSTALL_COMMANDS = ["git clone https://github.com/HatBashBR/HatCloud.git"]
    PROJECT_URL = "https://github.com/HatBashBR/HatCloud"

    def run(self):
        site = input("Enter Site >> ")
        os.chdir("HatCloud")
        subprocess.run(["sudo", "ruby", "hatcloud.rb", "-b", site])


class OtherTools(SecurityTool):
    TITLE = "Other Tools"
    DESCRIPTION = "Other security tools"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/tiameows/security-tools.git"]
    RUN_COMMANDS = ["cd security-tools && sudo python3 security-tools.py"]
    PROJECT_URL = "https://github.com/tiameows/security-tools"


class OtherToolsCollection(SecurityToolsCollection):
    TITLE = "Other Tools Collection"
    TOOLS = [
        SocialMediaBruteforceTools(),
        AndroidAttackTools(),
        HatCloud(),
        IDNHomographAttackTools(),
        EmailVerifyTools(),
        HashCrackingTools(),
        WifiJammingTools(),
        SocialMediaFinderTools(),
        PayloadInjectorTools(),
        WebCrawlingTools(),
        MixTools(),
        OtherTools()
    ]
