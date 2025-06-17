# coding=utf-8
from core import SecurityTool
from core import SecurityToolsCollection


class Keydroid(SecurityTool):
    TITLE = "Keydroid"
    DESCRIPTION = "Keydroid is a tool to extract Android keystore"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/tiameows/keydroid.git"]
    RUN_COMMANDS = ["cd keydroid && sudo python3 keydroid.py"]
    PROJECT_URL = "https://github.com/tiameows/keydroid"


class MySMS(SecurityTool):
    TITLE = "MySMS"
    DESCRIPTION = "MySMS is a tool to intercept SMS messages"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/tiameows/mysms.git"]
    RUN_COMMANDS = ["cd mysms && sudo python3 mysms.py"]
    PROJECT_URL = "https://github.com/tiameows/mysms"


class LockPhish(SecurityTool):
    TITLE = "LockPhish"
    DESCRIPTION = "LockPhish is a tool to phish Android lock screen"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/tiameows/lockphish.git"]
    RUN_COMMANDS = ["cd lockphish && sudo python3 lockphish.py"]
    PROJECT_URL = "https://github.com/tiameows/lockphish"


class Droidcam(SecurityTool):
    TITLE = "Droidcam"
    DESCRIPTION = "Droidcam is a tool to access Android camera"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/tiameows/droidcam.git"]
    RUN_COMMANDS = ["cd droidcam && sudo python3 droidcam.py"]
    PROJECT_URL = "https://github.com/tiameows/droidcam"


class EvilApp(SecurityTool):
    TITLE = "EvilApp"
    DESCRIPTION = "EvilApp is a tool to create malicious Android apps"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/tiameows/evilapp.git"]
    RUN_COMMANDS = ["cd evilapp && sudo python3 evilapp.py"]
    PROJECT_URL = "https://github.com/tiameows/evilapp"


class AndroidAttackTools(SecurityToolsCollection):
    TITLE = "Android Attack Tools"
    TOOLS = [
        Keydroid(),
        MySMS(),
        LockPhish(),
        Droidcam(),
        EvilApp()
    ]
