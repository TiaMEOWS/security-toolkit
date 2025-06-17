# coding=utf-8
import os

from core import SecurityTool
from core import SecurityToolsCollection


class AnonSurf(SecurityTool):
    TITLE = "AnonSurf"
    DESCRIPTION = "AnonSurf is a tool for anonymous surfing"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/tiameows/anonsurf.git"]
    RUN_COMMANDS = ["cd anonsurf && sudo python3 anonsurf.py"]
    PROJECT_URL = "https://github.com/tiameows/anonsurf"

    def __init__(self):
        super(AnonSurf, self).__init__([('Stop', self.stop)])

    def stop(self):
        os.system("sudo anonsurf stop")


class Multitor(SecurityTool):
    TITLE = "Multitor"
    DESCRIPTION = "How to stay in multi places at the same time"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/trimstray/multitor.git",
        "cd multitor;sudo bash setup.sh install"
    ]
    RUN_COMMANDS = ["multitor --init 2 --user debian-tor --socks-port 9000 --control-port 9900 --proxy privoxy --haproxy"]
    PROJECT_URL = "https://github.com/trimstray/multitor"

    def __init__(self):
        super(Multitor, self).__init__(runnable = False)


class AnonSurfTools(SecurityToolsCollection):
    TITLE = "Anonymous Surfing Tools"
    DESCRIPTION = ""
    TOOLS = [
        AnonSurf(),
        Multitor()
    ]
