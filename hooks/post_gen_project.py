# Initialize git repository and sync dependencies

import os
import subprocess

# Create virtual environment
subprocess.run(["uv", "venv", "--python={{cookiecutter.python_version}}"])

# Sync dependencies
subprocess.run(["uv", "sync"])

# Initialize git repository
subprocess.run(["git", "init"])

# Add all files to git
subprocess.run(["git", "add", "."])

# Commit all files
subprocess.run(["git", "commit", "-m", "chore: Initial commit"])
