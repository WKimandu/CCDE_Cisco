#!/bin/bash
# Linux setup script for CCDE_Cisco project
# Run this on the Linux server to set up SSH and the development environment

# Terminal colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}=== CCDE & Cisco ACI Knowledge Base Setup ===${NC}"
echo "This script will set up your Linux environment for the project."

# Step 1: Set up SSH for key-based authentication
echo -e "\n${GREEN}Step 1: Setting up SSH for key-based authentication${NC}"

# Create .ssh directory if it doesn't exist
mkdir -p ~/.ssh
chmod 700 ~/.ssh

# Create/append to authorized_keys
echo -e "\n${BLUE}Adding public key to authorized_keys${NC}"
echo "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIEIJ9x31sOqZfKPN8xI8NckJPOoA4hmk+qsA54GVYIVc CCDE_Cisco Linux Server Key" >> ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys

# Configure SSH server to accept key-based authentication
echo -e "\n${BLUE}Configuring SSH server${NC}"
if grep -q "^#PubkeyAuthentication" /etc/ssh/sshd_config; then
    # Uncomment and enable PubkeyAuthentication
    sudo sed -i 's/^#PubkeyAuthentication.*/PubkeyAuthentication yes/' /etc/ssh/sshd_config
elif ! grep -q "^PubkeyAuthentication" /etc/ssh/sshd_config; then
    # Add PubkeyAuthentication if it doesn't exist
    echo "PubkeyAuthentication yes" | sudo tee -a /etc/ssh/sshd_config
fi

# Restart SSH service
echo -e "\n${BLUE}Restarting SSH service${NC}"
sudo systemctl restart ssh

# Step 2: Install base dependencies
echo -e "\n${GREEN}Step 2: Installing base dependencies${NC}"

# Detect the Linux distribution
if [ -f /etc/os-release ]; then
    . /etc/os-release
    OS=$NAME
fi

# Install dependencies based on the distribution
if [[ "$OS" == *"Ubuntu"* ]] || [[ "$OS" == *"Debian"* ]]; then
    echo -e "\n${BLUE}Detected Ubuntu/Debian-based system${NC}"
    sudo apt update
    sudo apt install -y python3 python3-pip python3-dev git ffmpeg build-essential \
        libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev curl \
        libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev \
        libgl1-mesa-glx
elif [[ "$OS" == *"Fedora"* ]] || [[ "$OS" == *"CentOS"* ]] || [[ "$OS" == *"Red Hat"* ]]; then
    echo -e "\n${BLUE}Detected Fedora/CentOS/RHEL-based system${NC}"
    sudo dnf update -y
    sudo dnf install -y python3 python3-pip python3-devel git ffmpeg curl \
        zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel openssl-devel \
        xz xz-devel libffi-devel findutils mesa-libGL
else
    echo -e "\n${RED}Unsupported distribution. Please install dependencies manually.${NC}"
    exit 1
fi

# Step 3: Install Miniconda (if not already installed)
echo -e "\n${GREEN}Step 3: Installing Miniconda${NC}"
if [ -d "$HOME/miniconda3" ]; then
    echo -e "${BLUE}Miniconda already installed${NC}"
else
    echo -e "${BLUE}Downloading and installing Miniconda${NC}"
    curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
    chmod +x Miniconda3-latest-Linux-x86_64.sh
    ./Miniconda3-latest-Linux-x86_64.sh -b
    rm Miniconda3-latest-Linux-x86_64.sh
    
    # Add to PATH
    export PATH="$HOME/miniconda3/bin:$PATH"
    
    # Initialize conda for bash
    ~/miniconda3/bin/conda init bash
    
    # Source bashrc to make conda available
    source ~/.bashrc
fi

# Step 4: Clone the repository
echo -e "\n${GREEN}Step 4: Cloning the repository${NC}"
mkdir -p ~/Documents
cd ~/Documents

if [ -d "CCDE_Cisco" ]; then
    echo -e "${BLUE}Repository already exists. Pulling latest changes.${NC}"
    cd CCDE_Cisco
    git pull
else
    echo -e "${BLUE}Cloning the repository${NC}"
    git clone https://github.com/WKimandu/CCDE_Cisco.git
    cd CCDE_Cisco
fi

# Step 5: Create conda environment
echo -e "\n${GREEN}Step 5: Creating conda environment${NC}"
if conda info --envs | grep -q "CCDE_Cisco"; then
    echo -e "${BLUE}CCDE_Cisco environment already exists${NC}"
else
    echo -e "${BLUE}Creating CCDE_Cisco environment${NC}"
    conda env create -f environment.yml
fi

# Activate the environment
echo -e "\n${BLUE}Activating CCDE_Cisco environment${NC}"
source ~/miniconda3/bin/activate CCDE_Cisco

# Step 6: Install additional dependencies
echo -e "\n${GREEN}Step 6: Installing additional dependencies${NC}"
pip install -r requirements.txt

# Install spaCy model
echo -e "\n${BLUE}Installing spaCy model${NC}"
python -m spacy download en_core_web_sm

# Step 7: Make scripts executable
echo -e "\n${GREEN}Step 7: Making scripts executable${NC}"
find . -name "*.sh" -exec chmod +x {} \;

# Step 8: Final setup
echo -e "\n${GREEN}Step 8: Final setup${NC}"
echo -e "${BLUE}Setting up conda auto-activation${NC}"
echo "CCDE_Cisco" > .conda-auto-env

# Add conda auto-activation to .bashrc
if ! grep -q "conda-auto-env" ~/.bashrc; then
    echo '
# Auto-activate conda environments
function cd() {
  builtin cd "$@"
  if [[ -f ".conda-auto-env" ]]; then
    ENV=$(cat .conda-auto-env)
    if [[ $CONDA_DEFAULT_ENV != $ENV ]]; then
      conda activate $ENV
    fi
  fi
}
' >> ~/.bashrc
fi

echo -e "\n${GREEN}Setup complete!${NC}"
echo -e "Your Linux environment for CCDE & Cisco ACI Knowledge Base is ready."
echo -e "To start working on the project:"
echo -e "1. Start a new terminal or run 'source ~/.bashrc'"
echo -e "2. Navigate to the project: cd ~/Documents/CCDE_Cisco"
echo -e "3. The conda environment will activate automatically"
