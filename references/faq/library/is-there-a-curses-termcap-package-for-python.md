# Is there a curses/termcap package for Python?

### Is there a curses/termcap package for Python?

For Unix variants: a curses module ships in the standard Python source distribution under the [Modules](https://github.com/python/cpython/tree/3.14/Modules) subdirectory, although it isn't built by default. (Be aware that the Windows distribution lacks this ? no curses module exists for Windows.)

Beyond the basic curses features, the [`curses`](https://docs.python.org/3.14/library/curses.html#module-curses) module also exposes many extra functions drawn from ncurses and SYSV curses, including colour, alternative character set support, pads, and mouse support. As a result, the module won't work on operating systems limited to BSD curses, but no currently maintained OS appears to fall in that group.

[Subject index](INDEX.md)
