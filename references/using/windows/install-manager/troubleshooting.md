# 4.1.14. Troubleshooting

### 4.1.14. Troubleshooting

When your Python install manager appears to be misbehaving, please go through the tests and fixes here to see whether they resolve it. If they do not, please file an issue on [our bug tracker](https://github.com/python/pymanager/issues), attaching any pertinent log files (written by default to your `%TEMP%` directory).

Troubleshooting

| Symptom | Things to try |
| --- | --- |
| Typing `python` in my terminal throws a “command not found” error or pops open the Store app. | Have you got the Python install manager set up? |
|  | Hit Start, launch “Manage app execution aliases”, and confirm the “Python (default)” aliases are switched on. Should they already be on, toggle them off and back on to refresh the command. A refresh may likewise be needed for the “Python (default windowed)” and “Python install manager” commands. |
|  | Verify that the `py` and `pymanager` commands function. |
|  | Confirm your `PATH` variable holds the entry for `%UserProfile%\AppData\Local\Microsoft\WindowsApps`. By default the operating system adds this entry a single time, following the other user paths. Drop it and shortcuts go undiscovered. |
| Typing `py` in my terminal throws a “command not found” error. | Have you got the Python install manager set up? |
|  | Hit Start, launch “Manage app execution aliases”, and confirm the “Python (default)” aliases are switched on. Should they already be on, toggle them off and back on to refresh the command. A refresh may likewise be needed for the “Python (default windowed)” and “Python install manager” commands. |
|  | Confirm your `PATH` variable holds the entry for `%UserProfile%\AppData\Local\Microsoft\WindowsApps`. By default the operating system adds this entry a single time, following the other user paths. Drop it and shortcuts go undiscovered. |
| Running commands with `py` in my terminal throws a “can’t open file” error. | Typically this signals that the legacy launcher is installed and outranks the Python install manager. To get rid of it, hit Start, launch “Installed apps”, look up “Python launcher” and uninstall it. |
| `python` doesn’t launch the same runtime as `py` | Hit Start, launch “Installed apps”, scan for any Python runtimes already present, and either delete them or Modify and turn off the `PATH` options. |
|  | Hit Start, launch “Manage app execution aliases”, and confirm your `python.exe` alias points to “Python (default)” |
| `python` and `py` don’t launch the runtime I expect | Inspect your `PYTHON_MANAGER_DEFAULT` environment variable or `default_tag` configuration. Running `py list` reveals your default according to these settings. |
|  | Runtimes the Python install manager governs get picked over unmanaged ones. Run `py install` to set up the runtime you intend, or set your default tag. |
|  | Prerelease and experimental installs outside the Python install manager’s control can be picked over stable releases. Set your default tag, or uninstall the prerelease runtime and put it back with `py install`. |
| `pythonw` or `pyw` don’t launch the same runtime as `python` or `py` | Hit Start, launch “Manage app execution aliases”, and confirm your `pythonw.exe` and `pyw.exe` aliases line up with the rest. |
| Typing `pip` in my terminal throws a “command not found” error. | Did you turn on a virtual environment? Activate one by running the `.venv\Scripts\activate` script in your terminal. |
|  | The package might be present yet lack the generated executable. Our advice is to use `python -m pip` in its place. Running `py install --refresh` and confirming the global shortcuts directory sits on `PATH` (the command output flags it if not) ought to bring commands like `pip` (along with other installed packages) into reach. |
| I installed a package with `pip` but its command is not found. | Did you turn on a virtual environment? Activate one by running the `.venv\Scripts\activate` script in your terminal. |
|  | The Python install manager does not auto-generate global shortcuts for fresh packages. By the same token, removing a package leaves its shortcuts behind. Run `py install --refresh` to refresh the global shortcuts for newly installed packages. |
| Typing `script-name.py` in the terminal opens in a new window. | The operating system has a known limit here. Either put `py` ahead of the script name, build a batch file holding `@py "%~dpn0.py" %*` named to match the script, or install the legacy launcher and pick it as the association for scripts. |
| Drag-dropping files onto a script doesn’t work | The operating system has a known limit here. It works with the legacy launcher, or with the Python install manager when it came from the MSI. |
| I have installed the Python install manager multiple times. | Installing it simultaneously from several sources is fine: the Store or WinGet, the MSIX hosted on the Python website, and the MSI. They all get along and will share configuration and runtimes. |
|  | Refer to the earlier Advanced installation section for ways to remove the install manager besides the usual Installed Apps (Add and Remove Programs) settings page. |
| My old `py.ini` settings no longer work. | The new Python install manager has dropped support for this configuration file and its settings, so it gets ignored. Consult Configuration for details on configuration settings. |

[Subject index](INDEX.md) · [Previous source section](index-signatures.md) · [Following source section](the-embeddable-package.md)
