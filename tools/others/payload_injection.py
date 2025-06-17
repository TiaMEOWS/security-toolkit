# coding=utf-8
from core import SecurityTool
from core import SecurityToolsCollection


class DebInject(SecurityTool):
    TITLE = "DebInject"
    DESCRIPTION = "DebInject is a tool to inject payloads into Debian packages"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/tiameows/debinject.git"]
    RUN_COMMANDS = ["cd debinject && sudo python3 debinject.py"]
    PROJECT_URL = "https://github.com/tiameows/debinject"


class Pixload(SecurityTool):
    TITLE = "Pixload"
    DESCRIPTION = "Pixload is a tool to inject payloads into images"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/tiameows/pixload.git"]
    RUN_COMMANDS = ["cd pixload && sudo python3 pixload.py"]
    PROJECT_URL = "https://github.com/tiameows/pixload"

    def __init__(self):
        # super(Pixload, self).__init__([
        #     ('How To Use', self.show_project_page)
        # ], runnable = False)
        super(Pixload, self).__init__(runnable = False)


class PayloadInjectorTools(SecurityToolsCollection):
    TITLE = "Payload Injector Tools"
    TOOLS = [
        DebInject(),
        Pixload()
    ]
