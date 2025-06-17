# coding=utf-8
import subprocess

from core import SecurityTool
from core import SecurityToolsCollection


class AndroGuard(SecurityTool):
    TITLE = "Androguard"
    DESCRIPTION = "Androguard is a Reverse engineering, Malware and goodware " \
                  "analysis of Android applications and more"
    INSTALL_COMMANDS = ["sudo pip3 install -U androguard"]
    PROJECT_URL = "https://github.com/androguard/androguard "

    def __init__(self):
        super(AndroGuard, self).__init__(runnable = False)


class Apk2Gold(SecurityTool):
    TITLE = "Apk2Gold"
    DESCRIPTION = "Apk2Gold is a CLI tool for decompiling Android apps to Java"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/lxdvs/apk2gold.git",
        "cd apk2gold;sudo bash make.sh"
    ]
    PROJECT_URL = "https://github.com/lxdvs/apk2gold "

    def run(self):
        uinput = input("Enter (.apk) File >> ")
        subprocess.run(["sudo", "apk2gold", uinput])


class Jadx(SecurityTool):
    TITLE = "JadX"
    DESCRIPTION = "Jadx is Dex to Java decompiler.\n" \
                  "[*] decompile Dalvik bytecode to java classes from APK, dex," \
                  " aar and zip files\n" \
                  "[*] decode AndroidManifest.xml and other resources from " \
                  "resources.arsc"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/skylot/jadx.git",
        "cd jadx;./gradlew dist"
    ]
    PROJECT_URL = "https://github.com/skylot/jadx"

    def __init__(self):
        super(Jadx, self).__init__(runnable = False)


class Radare2(SecurityTool):
    TITLE = "Radare2"
    DESCRIPTION = "Radare2 is a complete framework for reverse-engineering and analyzing binaries"
    INSTALL_COMMANDS = ["sudo apt-get install radare2"]
    RUN_COMMANDS = ["radare2"]
    PROJECT_URL = "https://github.com/radareorg/radare2"


class Ghidra(SecurityTool):
    TITLE = "Ghidra"
    DESCRIPTION = "Ghidra is a software reverse engineering (SRE) framework"
    INSTALL_COMMANDS = ["sudo apt-get install ghidra"]
    RUN_COMMANDS = ["ghidra"]
    PROJECT_URL = "https://github.com/NationalSecurityAgency/ghidra"


class ReverseEngineeringTools(SecurityToolsCollection):
    TITLE = "Reverse Engineering Tools"
    TOOLS = [
        AndroGuard(),
        Apk2Gold(),
        Jadx(),
        Radare2(),
        Ghidra()
    ]
