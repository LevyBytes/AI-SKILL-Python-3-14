# venv: Virtual-environment creation and directory layout

### Creating virtual environments

To produce a virtual environment, run the `venv` module:

```shell
python -m venv /path/to/new/virtual/environment

```

Doing so makes the target directory (any required parent directories included) and drops a `pyvenv.cfg` file inside it whose `home` key references the Python installation that the command was launched from. Alongside this it builds a `bin` (or, on Windows, a `Scripts`) subdirectory holding either a copy or a symlink of the Python executable (whichever suits the platform or the arguments supplied when the environment was created). Additionally it produces a `lib/pythonX.Y/site-packages` subdirectory (which on Windows is `Lib\site-packages`). Should a directory already be present at that path, it gets reused.

Changed in version 3.5: Building virtual environments is now done by way of `venv` as the recommended route.

Deprecated since version 3.6, removed in version 3.8: For Python 3.3 and 3.4, **pyvenv** had been the advised way to make virtual environments; 3.5 superseded it by having you run `venv` directly.

Under Windows, run the `venv` command this way:

```ps1con
PS> python -m venv C:\path\to\new\virtual\environment

```

Passing `-h` to the command lists the options it accepts:

```none
usage: venv [-h] [--system-site-packages] [--symlinks | --copies] [--clear]
            [--upgrade] [--without-pip] [--prompt PROMPT] [--upgrade-deps]
            [--without-scm-ignore-files]
            ENV_DIR [ENV_DIR ...]

Creates virtual Python environments in one or more target directories.

Once an environment has been created, you may wish to activate it, e.g. by
sourcing an activate script in its bin directory.

```

[Subject index](INDEX.md) · [Previous](venv-creation-of-virtual-environments.md) · [Continue](creating-virtual-environments-env-dir.md) · [Owning module, declaration or section: venv](venv-creation-of-virtual-environments.md)
