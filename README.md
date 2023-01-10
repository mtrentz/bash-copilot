# bash-copilot
Simple script to get copilot suggestion for bash commands and execute it.

<img src="/demo.gif" width="600" />

# Requirements
1. Neovim installed and configured with github copilot
2. Python

# How it works
Run with 
```
python3 bcp.py
```
Complete the rest of the prompt with your command, exit with :wq and the script will be executed.

# Use anywhere
```
sudo cp bcp.py /usr/bin/bcp
sudo chmod +x /usr/bin/bcp
bcp
```

# Scripts
All scripts are stored in ~/.bcp/
