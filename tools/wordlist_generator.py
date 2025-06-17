# coding=utf-8
from core import SecurityTool
from core import SecurityToolsCollection


class Cupp(SecurityTool):
    TITLE = "Cupp"
    DESCRIPTION = "Cupp is a tool to generate custom wordlists"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/Mebus/cupp.git"]
    RUN_COMMANDS = ["cd cupp && sudo python3 cupp.py"]
    PROJECT_URL = "https://github.com/Mebus/cupp.git"


class WlCreator(SecurityTool):
    TITLE = "WordlistCreator"
    DESCRIPTION = "WordlistCreator is a tool to generate custom wordlists"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/tiameows/wlcreator.git"]
    RUN_COMMANDS = ["cd wlcreator && sudo python3 wlcreator.py"]
    PROJECT_URL = "https://github.com/tiameows/wlcreator"


class GoblinWordGenerator(SecurityTool):
    TITLE = "Goblin WordGenerator"
    DESCRIPTION = "Goblin WordGenerator is a tool to generate custom wordlists"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/UndeadSec/GoblinWordGenerator.git"]
    RUN_COMMANDS = ["cd GoblinWordGenerator && sudo python3 goblin.py"]
    PROJECT_URL = "https://github.com/UndeadSec/GoblinWordGenerator.git"


class showme(SecurityTool):
    TITLE = "Password list (1.4 Billion Clear Text Password)"
    DESCRIPTION = "Password list (1.4 Billion Clear Text Password)"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/Viralmaniar/SMWYG-Show-Me-What-You-Got.git"]
    RUN_COMMANDS = ["cd SMWYG-Show-Me-What-You-Got && sudo python3 SMWYG.py"]
    PROJECT_URL = "https://github.com/Viralmaniar/SMWYG-Show-Me-What-You-Got"


class WordlistGeneratorTools(SecurityToolsCollection):
    TITLE = "Wordlist Generator"
    TOOLS = [
        Cupp(),
        WlCreator(),
        GoblinWordGenerator(),
        showme()
    ]
