# curses: Terminfo strings, input queues and curses wrapper

curses.tigetstr(*capname*)

Give back, as a bytes object, the value of the string capability matching the terminfo capability name *capname*. Give back `None` when *capname* is not a terminfo “string capability”, or is canceled or missing from the terminal description.

 curses.tparm(*str*[, *...*])

Fill in the bytes object *str* with the supplied parameters, where *str* ought to be a parameterized string drawn from the terminfo database. For instance, `tparm(tigetstr("cup"), 5, 3)` might yield `b'\033[6;4H'`, with the precise result hinging on terminal type.

 curses.typeahead(*fd*)

Direct that the file descriptor *fd* serve for typeahead checking. When *fd* is `-1`, no typeahead checking happens.

The curses library performs “line-breakout optimization” by periodically scanning for typeahead while refreshing the screen. Should input turn up, and should it be arriving from a tty, the current update is held off until refresh or doupdate runs once more, which lets it respond faster to commands typed ahead of time. This function lets you name a different file descriptor for typeahead checking.

 curses.unctrl(*ch*)

Give back a bytes object that forms a printable representation of the character *ch*. Control characters appear as a caret followed by the character, for instance as `b'^C'`. Printing characters stay as they are.

 curses.ungetch(*ch*)

Push *ch* so that the next `getch()` returns it.

Note

Only one *ch* can be pushed before `getch()` is called.

 curses.update_lines_cols()

Refresh the `LINES` and `COLS` module variables. Handy for catching a manual screen resize.

Added in version 3.5.

 curses.unget_wch(*ch*)

Push *ch* so that the next `get_wch()` returns it.

Note

Only one *ch* can be pushed before `get_wch()` is called.

Added in version 3.3.

 curses.ungetmouse(*id*, *x*, *y*, *z*, *bstate*)

Push a `KEY_MOUSE` event onto the input queue, tying the supplied state data to it.

 curses.use_env(*flag*)

When employed, this function ought to run before `initscr()` or newterm run. When *flag* is `False`, the line and column values named in the terminfo database are used, even where the environment variables `LINES` and `COLUMNS` (the default) are set, or where curses runs inside a window (in which case the default conduct would be to take the window size whenever `LINES` and `COLUMNS` go unset).

 curses.use_default_colors()

The same as `assume_default_colors(-1, -1)`.

 curses.wrapper(*func*, */*, **args*, ***kwargs*)

Set up curses and then call another callable object, *func*, which ought to be the remainder of your curses-using application. Should the application raise an exception, this function brings the terminal back to a sane state before re-raising that exception and producing a traceback. The callable object *func* receives the main window ‘stdscr’ as its first argument, trailed by whatever other arguments were passed to `wrapper()`. Ahead of calling *func*, `wrapper()` switches on cbreak mode, switches off echo, turns on the terminal keypad, and sets up colors when the terminal has color support. On exit (whether normal or by exception) it restores cooked mode, switches echo back on, and turns off the terminal keypad.

[Subject index](INDEX.md) · [Previous](curses-raw-to-curses-tigetnum.md) · [Continue](curses-window-class.md) · [Owning module, declaration or section: curses](curses-terminal-handling-for-character-cell-displays.md) · [Owning module, declaration or section: Functions](curses-error-to-curses-endwin.md)
