import os

# The Python version the user selected during Cookiecutter setup
selected_version = "{{ cookiecutter.python_version }}"

# Available versions for the matrix (could be dynamically expanded later)
all_versions = ["3.9", "3.10", "3.11", "3.12", "3.13"]

# Determine the previous and next versions
selected_index = all_versions.index(selected_version)
prev_version = all_versions[selected_index - 1] if selected_index > 0 else None
next_version = all_versions[selected_index + 1] if selected_index < len(all_versions) - 1 else None

# Construct the version matrix
versions = [v for v in [prev_version, selected_version, next_version] if v is not None]

# Now write this matrix to the CI YAML
ci_path = os.path.join("{{cookiecutter.project_slug}}", ".github", "workflows", "continuous-integration.yml")

with open(ci_path, "r") as f:
    ci_content = f.read()

# Replace the placeholder for the Python version matrix
ci_content = ci_content.replace("python_version_matrix", ", ".join(versions))

# Write the updated CI config file
with open(ci_path, "w") as f:
    f.write(ci_content)

print(f"Updated CI configuration with Python version matrix: {versions}")
