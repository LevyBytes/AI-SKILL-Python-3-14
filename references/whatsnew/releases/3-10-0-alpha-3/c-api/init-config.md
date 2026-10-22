# Python 3.10.0 alpha 3 / c api / init config

[bpo-41713](https://bugs.python.org/issue?@action=redirect&bpo=41713): Took out the undocumented `PyOS_InitInterrupts()` function. Bringing up Python already wires in signal handlers on its own: consult [`PyConfig.install_signal_handlers`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.install_signal_handlers). Victor Stinner authored this patch.

[bpo-42260](https://bugs.python.org/issue?@action=redirect&bpo=42260): A single parse of the [`PyConfig.argv`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.argv) arguments is now all the [`PyConfig_Read()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Read) function performs: once those arguments are processed, [`PyConfig.parse_argv`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.parse_argv) gets the value `2`. Because Python's own arguments get stripped out of `PyConfig.argv`, a second parse would misread the application's options as though they were Python options.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
