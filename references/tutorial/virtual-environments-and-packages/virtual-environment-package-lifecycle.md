# Installing, selecting, upgrading and removing virtual-environment packages

### 12.3. Managing Packages with pip

Installing, upgrading, and removing packages is handled through a tool named **pip**. Unless told otherwise, `pip` pulls packages from the [Python Package Index](https://pypi.org). You're free to browse the Python Package Index by visiting it in your web browser.

A range of subcommands belong to `pip`: “install”, “uninstall”, “freeze”, and so on. (For the full `pip` documentation, see the [Installing Python modules](https://docs.python.org/3.14/installing/index.html#installing-index) guide.)

Naming a package alone installs its newest version:

```console
(tutorial-env) $ python -m pip install novas
Collecting novas
  Downloading novas-3.1.1.3.tar.gz (136kB)
Installing collected packages: novas
  Running setup.py install for novas
Successfully installed novas-3.1.1.3

```

A particular version can be installed too, by writing the package name, then `==`, then the version number:

```console
(tutorial-env) $ python -m pip install requests==2.6.0
Collecting requests==2.6.0
  Using cached requests-2.6.0-py2.py3-none-any.whl
Installing collected packages: requests
Successfully installed requests-2.6.0

```

Run that command again and `pip` will spot that the asked-for version is already present and do nothing. Pass a different version number to fetch that one, or run `python -m pip install --upgrade` to move the package up to its latest version:

```console
(tutorial-env) $ python -m pip install --upgrade requests
Collecting requests
Installing collected packages: requests
  Found existing installation: requests 2.6.0
    Uninstalling requests-2.6.0:
      Successfully uninstalled requests-2.6.0
Successfully installed requests-2.7.0

```

Running `python -m pip uninstall` with one or more package names after it strips those packages out of the virtual environment.

[Subject index](INDEX.md) · [Previous source section](creating-virtual-environments.md) · [Following source section](inspecting-packages-and-reproducing-requirements.md) · [Related tutorial example and explanation](inspecting-packages-and-reproducing-requirements.md) · [Create and activate the virtual environment](creating-virtual-environments.md)
