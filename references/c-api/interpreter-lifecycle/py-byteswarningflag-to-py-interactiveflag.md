# interpreter lifecycle C API: `Py_BytesWarningFlag`, `Py_DebugFlag`, `Py_DontWriteBytecodeFlag`, `Py_FrozenFlag`, `Py_HashRandomizationFlag`, `Py_IgnoreEnvironmentFlag`, `Py_InspectFlag`, `Py_InteractiveFlag`

### Global configuration variables

A set of global configuration variables lets Python govern assorted features and options. Ordinarily these flags take their values from [command line options](https://docs.python.org/3.14/using/cmdline.html#using-on-interface-options).

Whenever an option assigns a flag, the flag holds a count of how many times that option appeared. As an illustration, `-b` raises `Py_BytesWarningFlag` to 1 while `-bb` raises `Py_BytesWarningFlag` to 2.

 int Py_BytesWarningFlag

Retained only for backward compatibility: prefer assigning [`PyConfig.bytes_warning`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.bytes_warning) instead, see [Python Initialization Configuration](https://docs.python.org/3.14/c-api/init_config.html#init-config).

Emit a warning whenever [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) or [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) is compared against [`str`](https://docs.python.org/3.14/library/stdtypes.html#str), or `bytes` against [`int`](https://docs.python.org/3.14/library/functions.html#int). Raise an error once the value reaches `2` or above.

Set by the [`-b`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-b) option.

Deprecated since version 3.12, will be removed in version 3.15.

 int Py_DebugFlag

Retained only for backward compatibility: prefer assigning [`PyConfig.parser_debug`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.parser_debug) instead, see [Python Initialization Configuration](https://docs.python.org/3.14/c-api/init_config.html#init-config).

Enable parser debugging output (intended for experts only, and dependent on compilation options).

Set by the [`-d`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-d) option and the [`PYTHONDEBUG`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONDEBUG) environment variable.

Deprecated since version 3.12, will be removed in version 3.15.

 int Py_DontWriteBytecodeFlag

Retained only for backward compatibility: prefer assigning [`PyConfig.write_bytecode`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.write_bytecode) instead, see [Python Initialization Configuration](https://docs.python.org/3.14/c-api/init_config.html#init-config).

With a non-zero value, Python refrains from writing `.pyc` files when source modules are imported.

Set by the [`-B`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-B) option and the [`PYTHONDONTWRITEBYTECODE`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONDONTWRITEBYTECODE) environment variable.

Deprecated since version 3.12, will be removed in version 3.15.

 int Py_FrozenFlag

Retained only for backward compatibility: prefer assigning [`PyConfig.pathconfig_warnings`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.pathconfig_warnings) instead, see [Python Initialization Configuration](https://docs.python.org/3.14/c-api/init_config.html#init-config).

Private flag used by `_freeze_module` and `frozenmain` programs.

Deprecated since version 3.12, will be removed in version 3.15.

 int Py_HashRandomizationFlag

Retained only for backward compatibility: prefer assigning [`PyConfig.hash_seed`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.hash_seed) and [`PyConfig.use_hash_seed`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.use_hash_seed) instead, see [Python Initialization Configuration](https://docs.python.org/3.14/c-api/init_config.html#init-config).

Becomes `1` whenever the [`PYTHONHASHSEED`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONHASHSEED) environment variable holds a non-empty string.

When this flag is non-zero, the [`PYTHONHASHSEED`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONHASHSEED) environment variable is consulted to seed the secret hash.

Deprecated since version 3.12, will be removed in version 3.15.

 int Py_IgnoreEnvironmentFlag

Retained only for backward compatibility: prefer assigning [`PyConfig.use_environment`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.use_environment) instead, see [Python Initialization Configuration](https://docs.python.org/3.14/c-api/init_config.html#init-config).

Disregard every `PYTHON*` environment variable that may be present, for instance [`PYTHONPATH`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONPATH) and [`PYTHONHOME`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONHOME).

Set by the [`-E`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-E) and [`-I`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-I) options.

Deprecated since version 3.12, will be removed in version 3.15.

 int Py_InspectFlag

Retained only for backward compatibility: prefer assigning [`PyConfig.inspect`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.inspect) instead, see [Python Initialization Configuration](https://docs.python.org/3.14/c-api/init_config.html#init-config).

When a script is supplied as the first argument, or the [`-c`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-c) option is in play, drop into interactive mode once the script or command finishes, even if [`sys.stdin`](https://docs.python.org/3.14/library/sys.html#sys.stdin) does not look like a terminal.

Set by the [`-i`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-i) option and the [`PYTHONINSPECT`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONINSPECT) environment variable.

Deprecated since version 3.12, will be removed in version 3.15.

 int Py_InteractiveFlag

Retained only for backward compatibility: prefer assigning [`PyConfig.interactive`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.interactive) instead, see [Python Initialization Configuration](https://docs.python.org/3.14/c-api/init_config.html#init-config).

Set by the [`-i`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-i) option.

Deprecated since version 3.12, will be removed in version 3.15.

[Subject index](INDEX.md) · [Previous source contract](pymem-getallocator-to-pymutex-unlock.md) · [Following source contract](py-isolatedflag-to-py-quietflag.md)
