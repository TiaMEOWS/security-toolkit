# coding=utf-8
from core import SecurityTool
from core import SecurityToolsCollection


class GoSpider(SecurityTool):
    TITLE = "GoSpider"
    DESCRIPTION = "GoSpider is a fast web crawler"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/tiameows/gospider.git"]
    RUN_COMMANDS = ["cd gospider && sudo python3 gospider.py"]
    PROJECT_URL = "https://github.com/tiameows/gospider"


class WebCrawlingTools(SecurityToolsCollection):
    TITLE = "Web Crawling Tools"
    TOOLS = [
        GoSpider()
    ]
