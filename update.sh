#!/bin/bash

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

# Banner
echo -e "${BLUE}                                    https://github.com/tiameows/security-toolkit ${NC}"

# Check if running as root
if [ "$EUID" -ne 0 ]; then 
    echo -e "${RED}Please run as root${NC}"
    exit
fi

# Set installation directory
install_dir="/usr/share/security-toolkit"

# Update the tool
echo -e "[*]Updating security-toolkit..."
if [ -d "$install_dir" ]; then
    cd "$install_dir"
    git pull
    echo -e "[*]Marking security-toolkit directory as safe-directory"
    git config --global --add safe.directory "$install_dir"
    echo -e "${GREEN}[+]Update completed${NC}"
else
    echo -e "${RED}[!]security-toolkit is not installed${NC}"
fi
