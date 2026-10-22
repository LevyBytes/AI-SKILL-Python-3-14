# venv: Virtual-environment CLI directory and creation options

ENV_DIR

A mandatory argument naming the directory where the environment is to be created.

 --system-site-packages

Grant the virtual environment reach into the system site-packages directory.

 --symlinks

Attempt symlinks instead of copies in cases where symlinks aren’t the platform’s default.

 --copies

Attempt copies instead of symlinks, even on platforms whose default is symlinks.

 --clear

Wipe out the contents of the environment directory should it already be present, prior to creating the environment.

 --upgrade

Bring the environment directory up to this Python version, on the assumption that Python was upgraded where it sits.

 --without-pip

Bypass installing or upgrading pip inside the virtual environment (by default pip is bootstrapped).

 --prompt &lt;PROMPT&gt;

Supply a different prompt prefix to use for this environment.

 --upgrade-deps

Bring core dependencies (pip) up to the newest version available on PyPI.

 --without-scm-ignore-files

Bypass adding SCM ignore files into the environment directory (Git has default support).

Changed in version 3.4: pip is now installed by default; the `--without-pip` and `--copies` options were introduced.

Changed in version 3.4: Previously, an existing target directory triggered an error unless either the `--clear` or the `--upgrade` option had been supplied.

Changed in version 3.9: The `--upgrade-deps` option was added so that pip + setuptools can be brought up to the newest releases on PyPI.

Changed in version 3.12: `setuptools` no longer counts as a core venv dependency.

Changed in version 3.13: The `--without-scm-ignore-files` option was introduced.

Changed in version 3.13: By default `venv` now writes a `.gitignore` file for Git.

Note

Symlinks do work on Windows, yet using them isn’t advised. Worth flagging in particular: a double-click on `python.exe` from File Explorer follows the symlink straight away and disregards the virtual environment.

Note

Under Microsoft Windows, enabling the `Activate.ps1` script may be necessary, which you do by adjusting the execution policy for the user. The following PowerShell command accomplishes this:

```powershell
PS C:\> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

```

Refer to [About Execution Policies](https://go.microsoft.com/fwlink/?LinkID=135170) for more details.

The generated `pyvenv.cfg` file additionally carries an `include-system-site-packages` key, which is `true` when `venv` runs with the `--system-site-packages` option and otherwise `false`.

Provided the `--without-pip` option is absent, [`ensurepip`](https://docs.python.org/3.14/library/ensurepip.html#module-ensurepip) gets called to bootstrap `pip` into the virtual environment.

You may hand `venv` several paths at once, and when you do an identical virtual environment — matching the options given — is built at each path you supplied.

[Subject index](INDEX.md) · [Previous](creating-virtual-environments.md) · [Continue](how-venvs-work.md) · [Owning module, declaration or section: venv](venv-creation-of-virtual-environments.md) · [Owning module, declaration or section: Creating virtual environments](creating-virtual-environments.md)
