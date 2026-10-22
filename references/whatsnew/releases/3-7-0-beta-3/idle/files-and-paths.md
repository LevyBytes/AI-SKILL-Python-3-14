# Python 3.7.0 beta 3 / idle / files and paths

[bpo-32984](https://bugs.python.org/issue?@action=redirect&bpo=32984): Assign `__file__` while a startup file executes. As Python does, IDLE may optionally execute a single startup file inside the Shell window ahead of showing the very first interactive prompt. With IDLE, `-s` executes whatever file is named by the environment variable `IDLESTARTUP` or [`PYTHONSTARTUP`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONSTARTUP); `-r file` executes `file`. Python assigns `__file__` to the name of the startup file ahead of executing it and clears the binding before the initial prompt. IDLE now behaves the same way when launched normally, lacking the `-n` option.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
