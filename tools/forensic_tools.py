# coding=utf-8
import os

import sys

# Fetching parent directory for importing core.py
current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from core import SecurityTool
from core import SecurityToolsCollection


class Autopsy(SecurityTool):
    TITLE = "Autopsy"
    DESCRIPTION = "Autopsy is a digital forensics platform"
    INSTALL_COMMANDS = ["sudo apt-get install autopsy"]
    RUN_COMMANDS = ["autopsy"]
    PROJECT_URL = "https://github.com/tiameows/autopsy"


class Wireshark(SecurityTool):
    TITLE = "Wireshark"
    DESCRIPTION = "Wireshark is a network protocol analyzer"
    INSTALL_COMMANDS = ["sudo apt-get install wireshark"]
    RUN_COMMANDS = ["wireshark"]
    PROJECT_URL = "https://github.com/tiameows/wireshark"


class BulkExtractor(SecurityTool):
    TITLE = "Bulk Extractor"
    DESCRIPTION = "Bulk Extractor is a tool to extract information from files"
    INSTALL_COMMANDS = ["sudo apt-get install bulk-extractor"]
    RUN_COMMANDS = ["bulk_extractor"]
    PROJECT_URL = "https://github.com/tiameows/bulk-extractor"


class Guymager(SecurityTool):
    TITLE = "Guymager"
    DESCRIPTION = "Guymager is a forensic imager"
    INSTALL_COMMANDS = ["sudo apt-get install guymager"]
    RUN_COMMANDS = ["guymager"]
    PROJECT_URL = "https://github.com/tiameows/guymager"


class Toolsley(SecurityTool):
    TITLE = "Toolsley"
    DESCRIPTION = "Toolsley is a tool for digital forensics"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/tiameows/toolsley.git"]
    RUN_COMMANDS = ["cd toolsley && sudo python3 toolsley.py"]
    PROJECT_URL = "https://github.com/tiameows/toolsley"


class ForensicTools(SecurityToolsCollection):
    TITLE = "Forensic Tools"
    TOOLS = [
        Autopsy(),
        Wireshark(),
        BulkExtractor(),
        Guymager(),
        Toolsley()
    ]
