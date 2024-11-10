# MountainGod2-Cookiecutter: A cookiecutter template for Python packages

`mountaingod2-cookiecutter` is a [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) template for creating a Python package using [`uv`](https://github.com/astral-sh/uv).

## Usage

1. Install [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/):

    ```bash
    pip install cookiecutter
    ```

2. Generate a Python package structure using [`mountaingod2-cookiecutter`](https://github.com/MountainGod2/mountaingod2-cookiecutter):

    ```bash
    cookiecutter https://github.com/MountainGod2/mountaingod2-cookiecutter.git
    ```

3. After responding to the prompts you should have a directory structure similar to that shown below.

    ```text
    pkg
    ├── .github
    │   └── ISSUE_TEMPLATE                  ┐
    │       └── bug_report.md               │ GitHub issue templates
    │       └── feature_request.md          ┘
    │   └── workflows                       ┐
    │       └── close-stale-issues.ml       │
    │       └── codeql-analysis.yml         │ Github Actions workflows
    │       └── continuous-deployment.yml   │
    │       └── continous-integration.yml   │
    │       └── docker-image-build.yml      ┘
    │   └── pull_request_template.md
    │   └── renovate.json
    ├── .gitignore
    ├── .pre-commit.yml
    ├── .readthedocs.yml
    ├── CHANGELOG.md
    ├── CONDUCT.md
    ├── CONTRIBUTING.md
    ├── docs                                ┐
    │   ├── make.bat                        │
    │   ├── Makefile                        │
    │   ├── requirements.txt                │
    │   ├── changelog.md                    │ Package documentation
    │   ├── conduct.md                      │
    │   ├── conf.py                         │
    │   ├── contributing.md                 │
    │   ├── index.md                        │
    │   └── usage.ipynb                     ┘
    ├── LICENSE
    ├── README.md
    ├── pyproject.toml
    ├── src                                 ┐
    │   └── pkg                             ┘ Package source code
    └── tests                               ┐
        └── test_pkg.py                     ┘ Package tests
    ```

## License

`mountaingod2-cookiecutter` was created by MountainGod2. It is licensed under the terms of the MIT license.

## Acknowledgements

`mountaingod2-cookiecutter` was inspired by the Py-Pkgs `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
