# curses: Terminal mode restoration, resizing and capability queries

curses.raw()

Switch into raw mode. Under raw mode the usual line buffering plus the processing of the interrupt, quit, suspend, and flow control keys are switched off; characters reach the curses input functions one at a time.

 curses.reset_prog_mode()

Bring the terminal back to “program” mode, as saved earlier by `def_prog_mode()`.

 curses.reset_shell_mode()

Bring the terminal back to “shell” mode, as saved earlier by `def_shell_mode()`.

 curses.resetty()

Bring the terminal modes back to the state they held at the most recent `savetty()` call.

 curses.resize_term(*nlines*, *ncols*)

A backend function that `resizeterm()` relies on, handling the bulk of the work; while resizing the windows, `resize_term()` blank-fills whatever areas got extended. The calling application ought to populate these areas with suitable data. The `resize_term()` function tries to resize every window. That said, owing to how pads are called, resizing those is impossible without further interaction with the application.

 curses.resizeterm(*nlines*, *ncols*)

Resize the standard and current windows to the named dimensions, and tune the other bookkeeping data the curses library keeps that tracks the window dimensions (notably the SIGWINCH handler).

 curses.savetty()

Stash the terminal modes' current state inside a buffer, ready for use by `resetty()`.

 curses.get_escdelay()

Fetch the value that `set_escdelay()` set.

Added in version 3.9.

 curses.set_escdelay(*ms*)

Set how many milliseconds to wait after reading an escape character, so as to tell apart a lone escape character punched in at the keyboard from the escape sequences that cursor and function keys send.

Added in version 3.9.

 curses.get_tabsize()

Fetch the value that `set_tabsize()` set.

Added in version 3.9.

 curses.set_tabsize(*size*)

Set how many columns the curses library uses when it turns a tab character into spaces while adding the tab to a window.

Added in version 3.9.

 curses.setsyx(*y*, *x*)

Place the virtual screen cursor at *y*, *x*. Should *y* and *x* both be `-1`, then `leaveok` is set `True`.

 curses.setupterm(*term=None*, *fd=-1*)

Initialize the terminal. *term* is a string naming the terminal, or `None`; when left out or `None`, the value of the `TERM` environment variable is used instead. *fd* is the file descriptor where any initialization sequences are dispatched; when not supplied or `-1`, the file descriptor for `sys.stdout` is used.

 curses.start_color()

This must run if the programmer intends to use colors, and ahead of any other color manipulation routine. A good habit is to call this routine immediately following `initscr()`.

`start_color()` sets up eight basic colors (black, red, green, yellow, blue, magenta, cyan, and white), along with two global variables inside the `curses` module, `COLORS` and `COLOR_PAIRS`, which hold the largest number of colors and color-pairs the terminal can handle. It additionally returns the terminal's colors to the values they carried right when the terminal was first switched on.

 curses.termattrs()

Give back a logical OR of every video attribute the terminal supports. Such information proves handy whenever a curses program demands full command over how the screen looks.

 curses.termname()

Give back the value of the environment variable `TERM`, as a bytes object, cut down to 14 characters.

 curses.tigetflag(*capname*)

Give back, as an integer, the value of the Boolean capability matching the terminfo capability name *capname*. Give back the value `-1` when *capname* is not a Boolean capability, or `0` when it is canceled or missing from the terminal description.

 curses.tigetnum(*capname*)

Give back, as an integer, the value of the numeric capability matching the terminfo capability name *capname*. Give back the value `-2` when *capname* is not a numeric capability, or `-1` when it is canceled or missing from the terminal description.

[Subject index](INDEX.md) · [Previous](curses-keyname-to-curses-qiflush.md) · [Continue](curses-tigetstr-to-curses-wrapper.md) · [Owning module, declaration or section: curses](curses-terminal-handling-for-character-cell-displays.md) · [Owning module, declaration or section: Functions](curses-error-to-curses-endwin.md)
