# How do I check for a keypress without blocking?

### How do I check for a keypress without blocking?

Reach for the [`msvcrt`](https://docs.python.org/3.14/library/msvcrt.html#module-msvcrt) module, a standard extension module specific to Windows. It supplies a function `kbhit()` that reports whether a keyboard hit is waiting, plus `getch()` that grabs a single character without echoing it.

[Subject index](INDEX.md)
