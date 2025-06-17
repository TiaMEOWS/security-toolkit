# coding=utf-8
from core import SecurityTool
from core import SecurityToolsCollection


class TerminalMultiplexer(SecurityTool):
    TITLE = "Terminal Multiplexer"
    DESCRIPTION = "Terminal Multiplexer is a tool to manage multiple terminal sessions"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/tiameows/terminal-multiplexer.git"]
    RUN_COMMANDS = ["cd terminal-multiplexer && sudo python3 terminal-multiplexer.py"]
    PROJECT_URL = "https://github.com/tiameows/terminal-multiplexer"


class Crivo(SecurityTool):
    TITLE = "Crivo"
    DESCRIPTION = "Crivo is a tool to filter and analyze data"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/tiameows/crivo.git"]
    RUN_COMMANDS = ["cd crivo && sudo python3 crivo.py"]
    PROJECT_URL = "https://github.com/tiameows/crivo"


class MixTools(SecurityToolsCollection):
    TITLE = "Mix Tools"
    TOOLS = [
        TerminalMultiplexer(),
        Crivo()
    ]

