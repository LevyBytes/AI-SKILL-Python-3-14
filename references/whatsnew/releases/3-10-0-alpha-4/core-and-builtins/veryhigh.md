# Python 3.10.0 alpha 4 / core and builtins / veryhigh

[bpo-32381](https://bugs.python.org/issue?@action=redirect&bpo=32381): Corrected the encoding name used when a `.pyc` file runs on Windows: [`PyRun_SimpleFileExFlags()`](https://docs.python.org/3.14/c-api/veryhigh.html#c.PyRun_SimpleFileExFlags) now decodes the filename with the right encoding.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
