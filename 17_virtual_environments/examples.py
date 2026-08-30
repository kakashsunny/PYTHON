# Virtual Environments Examples and Commands

# Since virtual environments are terminal-centric, this file demonstrates 
# programmatically inspecting current environment information.

import sys
import os

# 1. Detect if running inside a Virtual Environment
def is_venv():
    # If sys.prefix and sys.base_prefix are different, a venv is active
    return getattr(sys, "base_prefix", sys.prefix) != sys.prefix

print("Is running inside a virtual environment?", is_venv())

# 2. Print current execution paths
print("Python Executable Path:", sys.executable)
print("Python prefix path:", sys.prefix)

# 3. Generating command guidelines
commands = """
# Command Reference Guide:
# -------------------------
# Create:
python -m venv .venv

# Activate (Windows Powershell):
.venv\\Scripts\\Activate.ps1

# Activate (Mac/Linux):
source .venv/bin/activate

# Install dependencies:
pip install requests
"""
print(commands)
