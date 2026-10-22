# Python 3.8.0 alpha 1 / idle / files and paths

[bpo-35087](https://bugs.python.org/issue?@action=redirect&bpo=35087): Refresh the idlelib help files for the present doc build. The principal change is dropping the chapter-section numbers.

[bpo-33917](https://bugs.python.org/issue?@action=redirect&bpo=33917): Repair and document idlelib/idle_test/template.py. The reworked file compiles, runs, and tests OK. idle_test/README.txt describes how to apply it when creating fresh IDLE test files.

[bpo-32984](https://bugs.python.org/issue?@action=redirect&bpo=32984): Assign `__file__` while a startup file executes. Just as Python does, IDLE may optionally execute a single startup file inside the Shell window ahead of showing the first interactive prompt. With IDLE, `-s` executes whatever file the environment variable `IDLESTARTUP` or [`PYTHONSTARTUP`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONSTARTUP) points at; `-r file` runs `file`. Python assigns `__file__` to the name of the startup file before execution, then clears it ahead of the first prompt. Run the usual way, lacking the `-n` option, IDLE now behaves identically.

[bpo-35769](https://bugs.python.org/issue?@action=redirect&bpo=35769): Switch IDLE’s default file name away from ‘Untitled’ over to ‘untitled’.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
