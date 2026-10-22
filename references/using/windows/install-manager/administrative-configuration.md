# 4.1.11. Administrative configuration

### 4.1.11. Administrative configuration

Administrators have several options for overriding how the Python install manager is configured. They support local caching, turning off particular shortcut kinds, and replacing bundled content. Every configuration option listed above is available, along with the ones described below.

You can override configuration options through the registry by writing values under `HKEY_LOCAL_MACHINE\Software\Policies\Python\PyManager`, where the value name corresponds to the configuration key and the value type is `REG_SZ`. This key itself is customizable, but only through edits to the core config file shipped with the Python install manager. Our recommendation, though, is to use registry values solely to point `base_config` at a JSON file holding the complete set of overrides. A registry key override supersedes every other configured setting, whereas `base_config` lets users keep adjusting the settings they need.

Keep in mind that most settings backed by environment variables work that way because their default value names the variable. Override them and the environment variable stops working, unless your override names another variable. As an illustration, the default value of `confirm` is literally `%PYTHON_MANAGER_CONFIRM%`, which gets resolved at load time. Set the value to `yes` and the environment variable is no longer consulted. Set it to `%CONFIRM%` and that environment variable takes over instead.

Any configuration setting that is a path is treated as relative to the folder holding the configuration file that declared it.

Administrative configuration options

| Config Key | Description |
| --- | --- |
| `base_config` | The top-priority configuration file that gets read. Bear in mind that this setting can be changed solely by the built-in configuration file plus the registry. |
| `user_config` | The configuration file read in second place. |
| `additional_config` | The configuration file read in third place. |
| `registry_override_key` | The registry spot examined for overrides. Bear in mind that altering this setting is possible only via the built-in configuration file. |
| `bundled_dir` | A read-only folder that holds files cached locally. |
| `install.fallback_source` | A path or URL pointing to an index to fall back on whenever the primary index is unreachable. |
| `install.enable_shortcut_kinds` | A comma-delimited roster of shortcut kinds to permit (for example `"pep514,start"`). Even permitted shortcuts can still be turned off via `disable_shortcut_kinds`. |
| `install.disable_shortcut_kinds` | A comma-delimited roster of shortcut kinds to leave out (for example `"pep514,start"`). Shortcuts turned off here are not switched back on by `enable_shortcut_kinds`. |
| `install.hard_link_entrypoints` | Set true to apply hard links for global shortcuts and conserve disk space. When false, every shortcut executable is duplicated instead. Once you alter this setting, you have to run `py install --refresh --force` so existing commands get updated. The default is true. You might need to switch it off for troubleshooting or on systems that struggle with file links. |
| `pep514_root` | The registry spot where PEP 514 entries are read and written. The default is `HKEY_CURRENT_USER\Software\Python`. |
| `start_folder` | The Start menu folder that receives shortcuts. The default is `Python`. This path is taken relative to the user’s Programs folder. |
| `virtual_env` | The path of the active virtual environment. The default is `%VIRTUAL_ENV%`, though leaving it empty switches off venv detection. |
| `shebang_can_run_anything_silently` | Set true to hide visible warnings whenever a shebang starts an application that is not a Python runtime. |
| `source_settings` | A map from source URL to settings tied to that particular index. Should several configuration files contain this section, per-URL settings get added or replaced, yet the individual settings within are not blended. For now these settings cover index signatures alone. |

[Subject index](INDEX.md) · [Previous source section](advanced-installation.md) · [Following source section](installing-free-threaded-binaries.md)
