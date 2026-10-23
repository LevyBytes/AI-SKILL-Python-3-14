# curses - Constants

### Constants

The `curses` module exposes these data members:

 curses.ERR

Certain curses routines that yield an integer, like `getch()`, return `ERR` when they fail.

 curses.OK

Certain curses routines that yield an integer, like `napms()`, return `OK` when they succeed.

 curses.version

A bytes object that holds the module’s current version.

 curses.ncurses_version

A named tuple holding the three parts of the ncurses library version: *major*, *minor*, and *patch*. Every value is an integer. The parts are also reachable by name, so `curses.ncurses_version[0]` matches `curses.ncurses_version.major`, and so forth.

Availability: if the ncurses library is used.

Added in version 3.8.

 curses.COLORS

The greatest number of colors the terminal can handle. It exists only once `start_color()` has been called.

 curses.COLOR_PAIRS

The greatest number of color pairs the terminal can handle. It exists only once `start_color()` has been called.

 curses.COLS

The screen width, that is, the count of columns. It exists only once `initscr()` has been called. Updated by `update_lines_cols()`, `resizeterm()` and `resize_term()`.

[Subject index](INDEX.md) · [Previous](window-scrollok-to-window-vline.md) · [Continue](curses-lines.md) · [Owning module, declaration or section: curses](curses-terminal-handling-for-character-cell-displays.md)
