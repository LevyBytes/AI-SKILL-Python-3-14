# Startup and Code Execution

### Startup and Code Execution

When started with the `-s` option, IDLE runs the file named by the environment variables `IDLESTARTUP` or [`PYTHONSTARTUP`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONSTARTUP). `IDLESTARTUP` is consulted by IDLE first; when `IDLESTARTUP` exists, the file it names runs. When `IDLESTARTUP` is absent, IDLE turns to `PYTHONSTARTUP`. The files these environment variables point to make handy spots for keeping functions used often from the IDLE shell, or for running import statements that pull in common modules.

Besides this, `Tk` loads a startup file too whenever one exists. Note that loading of the Tk file is unconditional. That extra file, `.Idle.py`, is sought in the user’s home directory. Because statements there run in the Tk namespace, the file is not handy for importing functions intended for use from IDLE’s Python shell.

[Subject index](INDEX.md) · [Previous](text-colors.md) · [Continue](command-line-usage.md)
