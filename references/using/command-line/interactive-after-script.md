# -i

-i

Drop into interactive mode once execution finishes.

Supplying the `-i` option brings you into interactive mode under any of these conditions:

- When a script is passed as first argument

- When the `-c` option is used

- When the `-m` option is used

Interactive mode kicks in even where [`sys.stdin`](https://docs.python.org/3.14/library/sys.html#sys.stdin) does not look like a terminal. The `PYTHONSTARTUP` file goes unread.

This comes in handy for examining global variables or a stack trace after a script throws an exception. See also `PYTHONINSPECT`.

[Subject index](INDEX.md) · [Previous source section](ignore-environment.md) · [Following source section](isolated-mode.md)
