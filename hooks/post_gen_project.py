"""Initialize git repository and sync dependencies"""
import subprocess

# Create virtual environment
subprocess.run(["uv", "venv", "--python={{ cookiecutter.python_version }}"])

# Sync dependencies
subprocess.run(["uv", "sync"])

# Run ruff lint
subprocess.run(["uv", "run", "ruff", "check", "--fix"])

# Create git repository add gh-pages branch and set default branch to main
subprocess.run(["git", "init"])
subprocess.run(["git", "checkout", "-b", "gh-pages"])
subprocess.run(["git", "checkout", "-b", "main"])
subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", "Initial commit"])
subprocess.run(["git", "branch", "-m", "main"])

# Print message
print("Project initialized!")