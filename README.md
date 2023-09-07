# Custom Downloader

[![Python CI](https://github.com/4ngelf/CustomDownloader/actions/workflows/python-ci.yml/badge.svg)](https://github.com/4ngelf/CustomDownloader/actions/workflows/python-ci.yml)

A simple Download manager with webscraping features.

## Current custom downloaders

- jkanime.net episodes

## Getting started <a name = "getting_started"></a>

### Installation

<small>TODO</small>

### Usage <a name = "usage"></a>

<small>TODO</small>

## Development

To run and build this project from source, follow this steps:

1. Install [Python][Python-install] and [Poetry][poetry-install].
   see-also: [pyenv][pyenv-install], [pipx][pipx-install].

2. Run this commands on shell (cmd, sh, bash, zsh, fish)

```bash
# Checkout this repository on current directory
git clone https://github.com/4ngelf/CustomDownloader.git
cd ./CustomDownloader

# Install dependencies and prepare project
poetry install && poetry run invoke prepare

# Run app
poetry run custom-downloader
```

### build binaries

<small>TODO</small>


## License

[MIT License](./LICENSE)

<!-- Links -->
[Python-install]: https://www.python.org/downloads/
[poetry-install]: https://python-poetry.org/docs/#installation
[pyenv-install]: https://github.com/pyenv/pyenv#installation
[pipx-install]: https://pypa.github.io/pipx/installation/
