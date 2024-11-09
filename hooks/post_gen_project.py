# Initialize git repository and sync dependencies
import subprocess

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
subprocess.run(["git", "commit", "-m", "chore: Initial commit"])
