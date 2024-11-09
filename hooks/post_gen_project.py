"""Initialize git repository and sync dependencies"""
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

# Create gh-pages branch
subprocess.run(["git", "checkout", "--orphan", "gh-pages"])

# Remove all files from gh-pages branch
subprocess.run(["git", "rm", "-rf", "."])

# Commit changes to gh-pages branch
subprocess.run(["git", "commit", "--allow-empty", "-m", "Initial commit"])

# Switch back to main branch
subprocess.run(["git", "checkout", "main"])

# Commit changes to main branch
subprocess.run(["git", "commit", "-m", "Initial commit"])

# Print success message
print("Initialized git repository and synced dependencies.")