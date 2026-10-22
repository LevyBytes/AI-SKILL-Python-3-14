# venv — How venvs work

### How venvs work

While a Python interpreter executes from within a virtual environment, [`sys.prefix`](https://docs.python.org/3.14/library/sys.html#sys.prefix) and [`sys.exec_prefix`](https://docs.python.org/3.14/library/sys.html#sys.exec_prefix) reference the virtual environment’s own directories, while [`sys.base_prefix`](https://docs.python.org/3.14/library/sys.html#sys.base_prefix) together with [`sys.base_exec_prefix`](https://docs.python.org/3.14/library/sys.html#sys.base_exec_prefix) reference those belonging to the base Python that built the environment. Testing `sys.prefix != sys.base_prefix` alone tells you whether the running interpreter is executing from a virtual environment.

A virtual environment can be “activated” by means of a script located in its binary directory (`bin` on POSIX; `Scripts` on Windows). That prepends the directory in question to your `PATH`, so that issuing **python** runs the environment’s Python interpreter and you can launch installed scripts without spelling out their full path. How you invoke the activation script differs by platform (replace `*<venv>*` with the path of the directory that holds the virtual environment):

| Platform | Shell | Command to activate virtual environment |
| --- | --- | --- |
| POSIX | bash/zsh | `$ source *<venv>*/bin/activate` |
| fish | `$ source *<venv>*/bin/activate.fish` |  |
| csh/tcsh | `$ source *<venv>*/bin/activate.csh` |  |
| pwsh | `$ *<venv>*/bin/Activate.ps1` |  |
| Windows | cmd.exe | `C:\> *<venv>*\Scripts\activate.bat` |
| PowerShell | `PS C:\> *<venv>*\Scripts\Activate.ps1` |  |

Added in version 3.4: **fish** and **csh** activation scripts.

Added in version 3.8: For PowerShell Core support, PowerShell activation scripts placed under POSIX.

Activating a virtual environment isn’t strictly something you *need* to do, since you can instead give the full path to that environment’s Python interpreter whenever you call Python. On top of that, every script the environment installs should be executable even without activation.

To make that work, scripts placed into virtual environments carry a “shebang” line referencing the environment’s Python interpreter, `#!/*<path-to-venv>*/bin/python`. As a result the script runs under that interpreter no matter what `PATH` happens to contain. Under Windows, “shebang” line handling works if you have the [Python install manager](https://docs.python.org/3.14/using/windows.html#launcher) installed. Consequently, double-clicking an installed script within a Windows Explorer window ought to launch it under the right interpreter without the environment needing activation or a place on `PATH`.

Once a virtual environment is activated, the `VIRTUAL_ENV` environment variable holds the path of that environment. Because using a virtual environment doesn’t demand that you explicitly activate it, `VIRTUAL_ENV` can’t be trusted as a signal of whether one is in use.

Warning

Since scripts installed in environments are not meant to assume the environment is active, their shebang lines hold the absolute paths leading to their environment’s interpreters. For that reason, environments are by nature non-portable in the general case. Keep a straightforward way to rebuild any environment at hand (for instance, given a requirements file `requirements.txt`, running `pip install -r requirements.txt` with the environment’s `pip` installs every package the environment requires). Whenever you have to relocate an environment somewhere new, build it afresh at the wanted spot and remove the original. If moving the environment happened because you relocated a parent directory of it, rebuild the environment at its new spot. Failing that, software installed within the environment may behave unexpectedly.

To shut off a virtual environment, type `deactivate` at your shell. How exactly this happens depends on the platform and is an internal implementation detail (commonly a script or a shell function does the job).

[Subject index](INDEX.md) · [Previous](creating-virtual-environments-env-dir.md) · [Continue](venv-envbuilder-class-to-create.md) · [Owning module, declaration or section: venv](venv-creation-of-virtual-environments.md)
