#!/bin/bash

# Colors
NC='\033[0m'
RED='\033[0;31m'
CYAN='\033[1;34m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'

# Minimum required Python version
MIN_PYTHON_VERSION="3.12"

# Logo Function
logo() {
    echo -e "\n${CYAN}"
    echo -e "**************************************************************************************************"
    echo -e "***************************************  Task Tracker CLI  ***************************************"
    echo -e "**************************************************************************************************"
    echo -e "${NC}\n"
}

# Detect Operating System
detect_os() {
    OS="$(uname -s)"
    case "$OS" in
        Linux*)     machine="LINUX";;
        Darwin*)    machine="MAC";;
        *)          echo -e "${RED}Unsupported OS: $OS${NC}"; exit 1;;
    esac
    echo -e "${CYAN}Detected OS: $machine${NC}"
}

# Check if Python is installed
check_python_installed() {
    if command -v python3 &> /dev/null; then
        PYTHON_VERSION=$(python3 --version | awk '{print $2}')
        echo -e "${CYAN}Python is installed: $PYTHON_VERSION${NC}"

        # Check if the version is at least 3.12
        if [[ $(echo -e "$PYTHON_VERSION\n$MIN_PYTHON_VERSION" | sort -V | head -n1) == "$MIN_PYTHON_VERSION" ]]; then
            echo -e "${GREEN}Python version meets the minimum required version ${MIN_PYTHON_VERSION}.${NC}"
        else
            echo -e "${YELLOW}Warning: Your Python version is lower than ${MIN_PYTHON_VERSION}. Please install Python ${MIN_PYTHON_VERSION} or higher.${NC}"
            echo -e "${CYAN}You may need to manually install the required version.${NC}"
            exit 1
        fi
    else
        echo -e "${RED}Python is not installed on your system.${NC}"
        echo -e "${YELLOW}Please install Python ${MIN_PYTHON_VERSION} or higher to proceed.${NC}"
        exit 1
    fi
}

# Make Script Executable
make_executable() {
    if [ -f "main.py" ]; then
        chmod +x main.py
        echo -e "${GREEN}CLI script made executable!${NC}"
    else
        echo -e "${RED}Error: main.py not found! Please ensure the file exists in the current directory.${NC}"
        exit 1
    fi
}

# Create Symlink for CLI
create_symlink() {
    SYMLINK="/usr/local/bin/tasktrackercli"

    if [[ -L "$SYMLINK" ]]; then
        echo -e "${CYAN}Existing symlink detected. Updating it...${NC}"
        sudo rm "$SYMLINK"
    fi

    sudo ln -s "$(pwd)/main.py" "$SYMLINK"
    if [[ $? -eq 0 ]]; then
        echo -e "${GREEN}Symlink created successfully! Use 'tasktrackercli' to interact with the Task Tracker CLI.${NC}"
    else
        echo -e "${RED}Failed to create a symlink. Please run the script as root or manually create the symlink.${NC}"
        exit 1
    fi
}

# Show Usage Instructions
show_usage() {
    echo -e "\n${CYAN}Setup completed. Usage instructions:${NC}"
    echo -e "  ${YELLOW}python3 main.py${NC} - To run the Task Tracker CLI application"
    echo -e "  ${YELLOW}tasktrackercli${NC} - To run globally if symlink is created"
    echo -e "${NC}\n"
}

# Main Function
main() {
    logo
    detect_os
    check_python_installed
    make_executable
    create_symlink
    show_usage
}

# Execute Main
main
