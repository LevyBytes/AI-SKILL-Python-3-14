# Python 3.6.5 release candidate 1 / idle / files and paths

[bpo-32984](https://bugs.python.org/issue?@action=redirect&bpo=32984): Assign `__file__` while a startup file is running. As Python does, IDLE may optionally execute one startup file inside the Shell window prior to showing the first interactive input prompt. With IDLE, `-s` runs whatever file is named in the environmental variable `IDLESTARTUP` or [`PYTHONSTARTUP`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONSTARTUP); `-r file` runs `file`. Before running the file Python assigns `__file__` to the startup file name, then unsets it ahead of the first prompt. IDLE now mirrors that during a normal run, that is without the `-n` option.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
