# int Py_RunMain(void)

int Py_RunMain(void)

Runs the main module within a completely configured CPython runtime.

Runs the command ([`PyConfig.run_command`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.run_command)), the script ([`PyConfig.run_filename`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.run_filename)) or the module ([`PyConfig.run_module`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.run_module)) named either on the command line or inside the configuration. When not one of those values is provided, it launches the interactive Python prompt (REPL) against the `__main__` module's global namespace.

When [`PyConfig.inspect`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.inspect) stays unset (its default), the result is `0` if the interpreter quits cleanly (meaning no exception was raised), the exit status from an unhandled [`SystemExit`](https://docs.python.org/3.14/library/exceptions.html#SystemExit), or `1` whenever some other unhandled exception occurs.

When [`PyConfig.inspect`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.inspect) is enabled (for instance, with the [`-i`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-i) option in play), the call does not return as the interpreter ends; execution carries on inside an interactive Python prompt (REPL) using the `__main__` module's global namespace. Should the interpreter have ended on an exception, that exception is re-raised right away within the REPL session. How the *REPL session* finishes then dictates the function's return value: `0`, `1`, or a [`SystemExit`](https://docs.python.org/3.14/library/exceptions.html#SystemExit) status, per the rules above.

This function will always finalize the Python interpreter prior to returning.

Refer to [Python Configuration](https://docs.python.org/3.14/c-api/init_config.html#init-python-config) for a sample of a tailored Python that runs in isolated mode at all times via `Py_RunMain()`.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](py-initialize-to-py-bytesmain.md) · [Following source contract](py-main.md) · [Following source contract](pyunstable-atexit.md)
