# interpreter lifecycle C API: `Py_UnbufferedStdioFlag`, `Py_VerboseFlag`

int Py_UnbufferedStdioFlag

Retained only for backward compatibility: prefer assigning [`PyConfig.buffered_stdio`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.buffered_stdio) instead, see [Python Initialization Configuration](https://docs.python.org/3.14/c-api/init_config.html#init-config).

Compel the stdout and stderr streams to operate without buffering.

Set by the [`-u`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-u) option and the [`PYTHONUNBUFFERED`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONUNBUFFERED) environment variable.

Deprecated since version 3.12, will be removed in version 3.15.

 int Py_VerboseFlag

Retained only for backward compatibility: prefer assigning [`PyConfig.verbose`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.verbose) instead, see [Python Initialization Configuration](https://docs.python.org/3.14/c-api/init_config.html#init-config).

Emit a message every time a module is initialized, naming the location (filename or built-in module) it was loaded from. At a value of `2` or higher, emit a message for every file inspected while a module is being located. It additionally reports on module cleanup during exit.

Set by the [`-v`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-v) option and the [`PYTHONVERBOSE`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONVERBOSE) environment variable.

Deprecated since version 3.12, will be removed in version 3.15.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](py-byteswarningflag-to-py-interactiveflag.md) · [Previous source contract](py-isolatedflag-to-py-quietflag.md) · [Following source contract](py-initialize-to-py-bytesmain.md)
