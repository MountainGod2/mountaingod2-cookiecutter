# {{ cookiecutter.__package_slug }}

{{ cookiecutter.package_short_description }}

## Installation

```bash
$ pip install {{ cookiecutter.__package_slug }}
```

## Usage

- TODO

{% if cookiecutter.use_docker == 'y' -%}
## Running with Docker

```bash
$ docker build -t {{ cookiecutter.__package_slug }} .
$ docker run --rm {{ cookiecutter.__package_slug }}
```

{% endif -%}
{% if cookiecutter.add_code_of_conduct == 'y' -%}
## Contributing

This project is released with a [Code of Conduct](CONDUCT.md). By contributing, you agree to abide by its terms.

{% endif -%}
## License

`{{ cookiecutter.__package_slug }}` was created by {{ cookiecutter.author_name }}. {% if cookiecutter.open_source_license != 'None' -%}It is licensed under the terms of the {{ cookiecutter.open_source_license }} license.{% else %}{{ cookiecutter.author_name }} retains all rights to the source and it may not be reproduced, distributed, or used to create derivative works.{% endif %}

## Credits

`{{ cookiecutter.__package_slug }}` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `mountaingod2-cookiecutter` [template](https://github.com/MountainGod2/mountaingod2-cookiecutter).
