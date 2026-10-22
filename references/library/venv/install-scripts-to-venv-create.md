# venv / API: `install_scripts()`, `create_git_ignore_file()`, `venv.create()`

install_scripts(*context*, *path*)

Subclasses can call this method from within `setup_scripts()` or `post_setup()` to help install custom scripts into the virtual environment.

*path* names a directory expected to hold the subdirectories `common`, `posix`, `nt`; each one holds scripts bound for the environment’s `bin` directory. Whatever sits in `common` and in the directory matching [`os.name`](https://docs.python.org/3.14/library/os.html#os.name) is copied across once some placeholder text is substituted:

- `__VENV_DIR__` becomes the environment directory’s absolute path.

- `__VENV_NAME__` becomes the environment name (the last path segment of the environment directory).

- `__VENV_PROMPT__` becomes the prompt (the environment name wrapped in parentheses, followed by a space)

- `__VENV_BIN_NAME__` becomes the bin directory’s name (either `bin` or `Scripts`).

- `__VENV_PYTHON__` becomes the absolute path to the environment’s executable.

The directories may already exist (covering the case of upgrading an environment already in place).

 create_git_ignore_file(*context*)

Writes a `.gitignore` file inside the virtual environment so that the Git source control manager ignores the directory in its entirety.

Added in version 3.13.

Changed in version 3.7.2: On Windows, redirector scripts for `python[w].exe` are now used rather than copying the real binaries. Within 3.7.2 alone, `setup_python()` is a no-op except when running from a build inside the source tree.

Changed in version 3.7.3: On Windows the redirector scripts are copied during `setup_python()` rather than `setup_scripts()`. That differed in 3.7.2. Where symlinks are in play, links are made to the original executables.

A module-level convenience function exists as well:

 `venv.create(env_dir, system_site_packages=False, clear=False, symlinks=False, with_pip=False, prompt=None, upgrade_deps=False, *, scm_ignore_files=frozenset())`

Construct an `EnvBuilder` from the supplied keyword arguments, then call its `create()` method passing the *env_dir* argument.

Added in version 3.3.

Changed in version 3.4: The *with_pip* parameter was introduced

Changed in version 3.6: The *prompt* parameter was introduced

Changed in version 3.9: The *upgrade_deps* parameter was introduced

Changed in version 3.13: The *scm_ignore_files* parameter was introduced

[Subject index](INDEX.md) · [Previous](ensure-directories-to-post-setup.md) · [Continue](an-example-of-extending-envbuilder.md) · [Owning module, declaration or section: venv](venv-creation-of-virtual-environments.md) · [Owning module, declaration or section: API](venv-envbuilder-class-to-create.md)
