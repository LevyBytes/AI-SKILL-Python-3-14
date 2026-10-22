# Python 3.12.0 alpha 1 / build / readline

[gh-90005](https://github.com/python/cpython/issues/90005): The `configure` script now leans on `pkg-config` to discover what [`readline`](https://docs.python.org/3.14/library/readline.html#module-readline) and [`curses`](https://docs.python.org/3.14/library/curses.html#module-curses) depend on. Automatic discovery covers `ncurses` / `ncursesw` exclusively; the legacy `curses` library is not wired up on its own. The fallback that handled an absent `termcap` or `tinfo` library is gone.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
