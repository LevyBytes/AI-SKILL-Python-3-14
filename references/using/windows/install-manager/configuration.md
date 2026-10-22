# 4.1.8. Configuration

### 4.1.8. Configuration

The Python install manager draws its setup from a layered stack of configuration files, plus environment variables, command-line options, and registry settings. Broadly, configuration files can configure anything, the placement of other configuration files included, whereas registry settings belong to administrators alone and take precedence over configuration files. Command-line options outrank every other setting, but not every option exists.

This section describes the defaults, though keep in mind that modified or overridden installs may resolve settings in other ways.

An administrator may set up a global configuration file, which is read first. The user configuration file lives at `%AppData%\Python\pymanager.json` (be aware that this path sits under `Roaming`, not `Local`) and is read after that, overwriting any settings from files read earlier. You can name a further configuration file through the `PYTHON_MANAGER_CONFIG` environment variable or the `--config` command line option (but not both at once). Administrative customization options described later can alter these locations.

The settings below are the ones judged likely to be changed during normal use. Later sections cover those meant for administrative customization.

Standard configuration options

| Config Key | Environment Variable | Description |
| --- | --- | --- |
| `default_tag` | PYTHON_MANAGER_DEFAULT?? | The default version that is preferred for launching or installing. The default reading of this is the latest version that is not a prerelease, coming from the CPython team. |
| `default_platform` | `PYTHON_MANAGER_DEFAULT_PLATFORM` | The default platform preferred for launching or installing. It acts as a suffix appended to the given tag, so `py -V:3.14` would lean toward an install for `3.14-64` where one is present (with `default_platform` set to `-64`), yet falls back to `3.14` where no tagged install is present. |
| `logs_dir` | `PYTHON_MANAGER_LOGS` | Where log files get written. The default is `%TEMP%`. |
| `automatic_install` | PYTHON_MANAGER_AUTOMATIC_INSTALL?? | True permits automatic installs while `py exec` is used for launching (or `py` where no runtimes have yet been installed). Whatever this is set to, other commands never install on their own. The default is true. |
| `include_unmanaged` | `PYTHON_MANAGER_INCLUDE_UNMANAGED` | True lets runtimes the Python install manager did not install be listed and launched; false leaves them out. The default is true. |
| `shebang_can_run_anything` | `PYTHON_MANAGER_SHEBANG_CAN_RUN_ANYTHING` | True permits shebangs within `.py` files to start applications besides Python runtimes; false blocks it. The default is true. |
| `shebang_templates` | (none) | A map pairing each shebang line template with a replacement command, like `py -V:<tag>`, or with a substitute string. Consult Shebang lines for further details. |
| `log_level` | `PYMANAGER_VERBOSE`, `PYMANAGER_DEBUG` | Sets the default output level (0-50). The default is 20. Smaller values yield more output. These environment variables are boolean, and might emit extra output while starting up that later configuration then suppresses. |
| `confirm` | `PYTHON_MANAGER_CONFIRM` | True asks for confirmation ahead of certain actions (such as uninstall); false bypasses the confirmation. The default is true. |
| `install.source` | `PYTHON_MANAGER_SOURCE_URL` | Override the index feed to obtain new installs from. |
| `install.enable_entrypoints` | (none) | True makes global commands for installed packages (such as `pip.exe`). The packages themselves define these. Where this is false, only the Python interpreter gets global commands made. The default is true. After altering this setting you should run `py install --refresh`. |
| `list.format` | `PYTHON_MANAGER_LIST_FORMAT` | Names the default format the `py list` command applies. The default is `table`. |
| `install_dir` | (none) | Names the root directory into which runtimes get installed. Should you alter this setting, runtimes installed earlier stop working unless you relocate them to the new spot. |
| `global_dir` | (none) | Names the directory holding global commands (such as `python3.14.exe` and `pip.exe`). Put this directory on your `PATH` so the commands become reachable from your terminal. |
| `download_dir` | (none) | Names the directory that holds downloaded files. This directory serves as a temporary cache and may be tidied up periodically. |

Dotted names belong nested inside JSON objects; for instance, `list.format` would be written as `{"list": {"format": "table"}}`.

[Subject index](INDEX.md) · [Previous source section](uninstalling-runtimes.md) · [Following source section](shebang-lines.md)
