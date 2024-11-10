# Initialize git repository and sync dependencies
import subprocess
import os
from shutil import rmtree

if '{{ cookiecutter.use_docker }}' != 'y':
    rmtree('.dockerignore')
    os.remove('Dockerfile')

if '{{ cookiecutter.use_ci_cd }}' != 'y':
    rmtree('.github/workflows')

if '{{ cookiecutter.use_pre_commit_hooks }}' != 'y':
    os.remove('.pre-commit-config.yaml')

if '{{ cookiecutter.add_code_of_conduct }}' != 'y':
    os.remove('CONDUCT.md')

# Create virtual environment
subprocess.run(["uv", "venv", "--python={{ cookiecutter.python_version }}"])

# Sync dependencies
subprocess.run(["uv", "sync"])

# Run ruff lint
subprocess.run(["uv", "run", "ruff", "check", "--fix"])

# Initialize git repository
subprocess.run(["git", "init"])

# Add all files to git
subprocess.run(["git", "add", "."])

# Rename the default branch to main
subprocess.run(["git", "branch", "-m", "main"])

# Commit all files
subprocess.run(["git", "commit", "-m", "feat: Initial commit of {{cookie.cutter.__package_slug }}"])
