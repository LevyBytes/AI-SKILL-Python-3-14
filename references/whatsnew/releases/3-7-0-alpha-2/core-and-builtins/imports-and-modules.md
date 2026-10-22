# Python 3.7.0 alpha 2 / core and builtins / imports and modules

[bpo-31642](https://bugs.python.org/issue?@action=redirect&bpo=31642): Brought back the ability to block ?from package import module? by assigning None to sys.modules[?package.module?].

[bpo-31574](https://bugs.python.org/issue?@action=redirect&bpo=31574): Two dtrace probes were instrumented into Importlib to profile import timing.

[bpo-31492](https://bugs.python.org/issue?@action=redirect&bpo=31492): Repair assertion failures that arise when an import from a module carrying a bad `__name__` attribute fails, and when accessing an attribute of such a module fails. Oren Milman wrote the patch.

[bpo-31415](https://bugs.python.org/issue?@action=redirect&bpo=31415): Introduce the `-X importtime` option to report how long every import takes. That is handy for tuning an application's startup time. The [`PYTHONPROFILEIMPORTTIME`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONPROFILEIMPORTTIME) variable is supported as an equivalent way to turn this on.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
