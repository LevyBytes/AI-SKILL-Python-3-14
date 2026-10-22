# Distribution, Distutils

# Distribution, Distutils

## Overview

Covers: Software Packaging and Distribution; distutils — Building and installing Python modules.

## Software Packaging and Distribution

### Software Packaging and Distribution

The libraries here assist with distributing and installing Python software. Although these modules are built to operate together with the [Python Package Index](https://pypi.org), you can equally point them at a local index server or run them with no index server whatsoever.

- [`ensurepip` — Bootstrapping the `pip` installer](https://docs.python.org/3.14/library/ensurepip.html)
  - [Command-line interface](https://docs.python.org/3.14/library/ensurepip.html#command-line-interface)
  - [Module API](https://docs.python.org/3.14/library/ensurepip.html#module-api)

- [`venv` — Creation of virtual environments](https://docs.python.org/3.14/library/venv.html)
  - [Creating virtual environments](https://docs.python.org/3.14/library/venv.html#creating-virtual-environments)
  - [How venvs work](https://docs.python.org/3.14/library/venv.html#how-venvs-work)
  - [API](https://docs.python.org/3.14/library/venv.html#api)
  - [An example of extending `EnvBuilder`](https://docs.python.org/3.14/library/venv.html#an-example-of-extending-envbuilder)

- [`zipapp` — Manage executable Python zip archives](https://docs.python.org/3.14/library/zipapp.html)
  - [Basic Example](https://docs.python.org/3.14/library/zipapp.html#basic-example)
  - [Command-Line Interface](https://docs.python.org/3.14/library/zipapp.html#command-line-interface)
  - [Python API](https://docs.python.org/3.14/library/zipapp.html#python-api)
  - [Examples](https://docs.python.org/3.14/library/zipapp.html#examples)
  - [Specifying the Interpreter](https://docs.python.org/3.14/library/zipapp.html#specifying-the-interpreter)
  - [Creating Standalone Applications with zipapp](https://docs.python.org/3.14/library/zipapp.html#creating-standalone-applications-with-zipapp)
    - [Caveats](https://docs.python.org/3.14/library/zipapp.html#caveats)

  - [The Python Zip Application Archive Format](https://docs.python.org/3.14/library/zipapp.html#the-python-zip-application-archive-format)

## distutils — Building and installing Python modules

### `distutils` — Building and installing Python modules

Deprecated since version 3.10, removed in version 3.12.

This module no longer ships with the Python standard library. Following deprecation in Python 3.10, it was [removed in Python 3.12](https://docs.python.org/3.14/whatsnew/3.12.html#whatsnew312-removed-distutils). That removal came out of [**PEP 632**](https://peps.python.org/pep-0632/), where you'll also find [migration advice](https://peps.python.org/pep-0632/#migration-advice).

[Python 3.11](https://docs.python.org/3.11/library/distutils.html) was the final release to ship the `distutils` module.

[Subject index](INDEX.md)
