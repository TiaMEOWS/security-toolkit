#!/usr/bin/env python3

import re
from core import SecurityTool
from core import SecurityToolsCollection
from security_toolkit import all_tools


def sanitize_anchor(text):
    return re.sub(r'[^a-z0-9]+', '-', text.lower())


def get_toc(tools, indentation = ""):
    md = ""
    for tool in tools:
        if isinstance(tool, SecurityToolsCollection):
            md += (indentation + "- [{}](#{})\n".format(
                tool.TITLE, sanitize_anchor(tool.TITLE)))
            md += get_toc(tool.TOOLS, indentation = indentation + '    ')
    return md


def get_tools_toc(tools, indentation = ""):
    md = ""
    for tool in tools:
        if isinstance(tool, SecurityToolsCollection):
            md += (indentation + "- [{}](#{})\n".format(
                tool.TITLE, sanitize_anchor(tool.TITLE)))
            md += get_tools_toc(tool.TOOLS, indentation = indentation + '  ')
        elif isinstance(tool, SecurityTool):
            if tool.PROJECT_URL:
                md += ("- [{}]({})\n".format(tool.TITLE, tool.PROJECT_URL))
            else:
                md += ("- {}\n".format(tool.TITLE))
    return md


def get_tools_content(tools, indentation = ""):
    md = ""
    for tool in tools:
        if isinstance(tool, SecurityToolsCollection):
            md += (indentation + "# {}\n".format(tool.TITLE))
            md += get_tools_toc(tool.TOOLS, indentation = indentation + '#')
        elif isinstance(tool, SecurityTool):
            if tool.PROJECT_URL:
                md += ("- [{}]({})\n".format(tool.TITLE, tool.PROJECT_URL))
            else:
                md += ("- {}\n".format(tool.TITLE))
    return md


def generate_readme():
    with open("README.md", "w") as f:
        f.write("# Security Toolkit Menu 🧰\n\n")
        f.write("A collection of security tools for penetration testing and security research.\n\n")
        f.write("## Installation\n\n")
        f.write("```bash\n")
        f.write("git clone https://github.com/tiameows/security-toolkit.git\n")
        f.write("cd security-toolkit\n")
        f.write("sudo python3 install.py\n")
        f.write("```\n\n")
        f.write("## Usage\n\n")
        f.write("```bash\n")
        f.write("sudo python3 security-toolkit.py\n")
        f.write("```\n\n")
        f.write("## Features\n\n")
        f.write(get_tools_toc(all_tools))
        f.write("\n## License\n\n")
        f.write("This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.\n\n")
        f.write("## Author\n\n")
        f.write("- **Tiameows** - *Initial work* - [GitHub](https://github.com/tiameows)\n\n")
        f.write("## Acknowledgments\n\n")
        f.write("- Thanks to all the contributors who have helped make this project better.\n")


if __name__ == "__main__":
    generate_readme()
