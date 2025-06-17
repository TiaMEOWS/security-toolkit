# coding=utf-8
from core import SecurityTool
from core import SecurityToolsCollection


class WiFiJammer(SecurityTool):
    TITLE = "WiFi Jammer"
    DESCRIPTION = "WiFi Jammer is a tool to jam WiFi networks"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/tiameows/wifi-jammer.git"]
    RUN_COMMANDS = ["cd wifi-jammer && sudo python3 wifi-jammer.py"]


class WifiJammerNG(SecurityTool):
    TITLE = "WifiJammer-NG"
    DESCRIPTION = "WifiJammer-NG is a tool to jam WiFi networks"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/tiameows/wifijammer-ng.git"]
    RUN_COMMANDS = ["cd wifijammer-ng && sudo python3 wifijammer-ng.py"]
    PROJECT_URL = "https://github.com/tiameows/wifijammer-ng"


class KawaiiDeauther(SecurityTool):
    TITLE = "KawaiiDeauther"
    DESCRIPTION = "KawaiiDeauther is a tool to deauthenticate WiFi clients"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/tiameows/kawaiideauther.git"]
    RUN_COMMANDS = ["cd kawaiideauther && sudo python3 kawaiideauther.py"]
    PROJECT_URL = "https://github.com/tiameows/kawaiideauther"


class WifiJammingTools(SecurityToolsCollection):
    TITLE = "WiFi Jamming Tools"
    TOOLS = [
        WifiJammerNG(),
        KawaiiDeauther()
    ]
