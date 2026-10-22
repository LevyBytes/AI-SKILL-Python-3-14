# Python 3.10.0 alpha 3 / core and builtins / init config

[bpo-41686](https://bugs.python.org/issue?@action=redirect&bpo=41686): Under Windows the `SIGINT` event, `_PyOS_SigintEvent()`, now gets created even when Python is set up to skip installing signal handlers (that is, when [`PyConfig.install_signal_handlers`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.install_signal_handlers) equals to 0, or `Py_InitializeEx(0)`).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
