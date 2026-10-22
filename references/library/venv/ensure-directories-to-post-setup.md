# venv / API: `ensure_directories()`, `create_configuration()`, `setup_python()`, `setup_scripts()`, `upgrade_dependencies()`, `post_setup()`

ensure_directories(*env_dir*)

Makes the environment directory plus any required subdirectories not yet present, and hands back a context object. That context object merely holds attributes (paths among them) for the remaining methods to draw on. When the `EnvBuilder` is built with the arg `clear=True`, the environment directory’s contents are cleared and then every required subdirectory is rebuilt.

What comes back as the context object is a [`types.SimpleNamespace`](https://docs.python.org/3.14/library/types.html#types.SimpleNamespace) carrying the attributes below:

- `env_dir` - Where the virtual environment lives. Feeds `__VENV_DIR__` within activation scripts (refer to `install_scripts()`).

- `env_name` - What the virtual environment is named. Feeds `__VENV_NAME__` within activation scripts (refer to `install_scripts()`).

- `prompt` - The prompt that the activation scripts will apply. Feeds `__VENV_PROMPT__` within activation scripts (refer to `install_scripts()`).

- `executable` - The Python executable underpinning the virtual environment. This allows for the situation in which one virtual environment is built from another.

- `inc_path` - The include path belonging to the virtual environment.

- `lib_path` - The purelib path belonging to the virtual environment.

- `bin_path` - The script path belonging to the virtual environment.

- `bin_name` - The script path’s name taken relative to where the virtual environment sits. Feeds `__VENV_BIN_NAME__` within activation scripts (refer to `install_scripts()`).

- `env_exe` - What the Python interpreter inside the virtual environment is named. Feeds `__VENV_PYTHON__` within activation scripts (refer to `install_scripts()`).

- `env_exec_cmd` - The Python interpreter’s name, with filesystem redirections accounted for. You can use this to launch Python in the virtual environment.

Changed in version 3.11: Paths for the directories that get created are now built using the *venv* [sysconfig installation scheme](https://docs.python.org/3.14/library/sysconfig.html#installation-paths).

Changed in version 3.12: The `lib_path` attribute joined the context, and the context object itself gained documentation.

 create_configuration(*context*)

Generates the `pyvenv.cfg` configuration file inside the environment.

 setup_python(*context*)

Lays down a copy of, or a symlink to, the Python executable within the environment. On POSIX systems, when a particular executable `python3.x` was used, symlinks named `python` and `python3` get created pointing at that executable, unless files bearing those names are already there.

 setup_scripts(*context*)

Places activation scripts suited to the platform into the virtual environment.

 upgrade_dependencies(*context*)

Brings the core venv dependency packages (at present [pip](https://pypi.org/project/pip/)) in the environment up to date. This works by shelling out to the environment’s `pip` executable.

Added in version 3.9.

Changed in version 3.12: [setuptools](https://pypi.org/project/setuptools/) has stopped being a core venv dependency.

 post_setup(*context*)

A stub method that third party implementations can override to pre-install packages into the virtual environment or carry out other steps after creation.

[Subject index](INDEX.md) · [Previous](venv-envbuilder-class-to-create.md) · [Continue](install-scripts-to-venv-create.md) · [Owning module, declaration or section: venv](venv-creation-of-virtual-environments.md) · [Owning module, declaration or section: API](venv-envbuilder-class-to-create.md)
