# curses: Terminal input, capability detection and screen initialization

curses.erasechar()

Hand back, as a one-byte bytes object, whatever erase character the user currently has. Under Unix operating systems this is a trait of the curses program's controlling tty, and the curses library does not configure it on its own.

 curses.filter()

The `filter()` routine, when employed, has to run before `initscr()` runs. During those calls the result is that `LINES` becomes `1`; the capabilities `clear`, `cup`, `cud`, `cud1`, `cuu1`, `cuu`, `vpa` are switched off; and the `home` string takes on the value of `cr`. As a consequence the cursor — and likewise the screen updates — stay locked to the current line. You might apply this to allow character-at-a-time line editing while leaving the rest of the screen alone.

 curses.flash()

Flash the screen. In other words, flip it to reverse-video and then flip it back after a brief moment. Certain people favor such a ‘visible bell’ over the audible attention signal that `beep()` makes.

 curses.flushinp()

Empty every input buffer. Doing so discards any typeahead the user supplied that the program has not yet handled.

 curses.getmouse()

Once `getch()` hands back `KEY_MOUSE` to flag a mouse event, you should invoke this method to fetch the queued mouse event, delivered as a 5-tuple `(id, x, y, z, bstate)`. *id* is an ID value that tells multiple devices apart, and *x*, *y*, *z* hold the event's coordinates. (*z* goes unused at present.) *bstate* is an integer whose bits get set to mark the event's type, formed as the bitwise OR of one or more of the constants below, with *n* standing for the button number from 1 to 5: `BUTTONn_PRESSED`, `BUTTONn_RELEASED`, `BUTTONn_CLICKED`, `BUTTONn_DOUBLE_CLICKED`, `BUTTONn_TRIPLE_CLICKED`, `BUTTON_SHIFT`, `BUTTON_CTRL`, `BUTTON_ALT`.

Changed in version 3.10: The `BUTTON5_*` constants are henceforth exposed whenever the underlying curses library makes them available.

 curses.getsyx()

Give back the virtual screen cursor's current coordinates as a tuple `(y, x)`. When `leaveok` happens to be `True` at that moment, return `(-1, -1)` instead.

 curses.getwin(*file*)

Read the window-related data that an earlier `window.putwin()` call placed in the file. The routine proceeds to build and set up a fresh window from that data, then hands back the new window object.

 curses.has_colors()

Give back `True` when the terminal is capable of showing colors; otherwise give back `False`.

 curses.has_extended_color_support()

Give back `True` when the module offers extended colors; otherwise give back `False`. Extended color support permits more than 256 color pairs on terminals that handle more than 16 colors (for example xterm-256color).

Extended color support needs ncurses version 6.1 or newer.

Added in version 3.10.

 curses.has_ic()

Give back `True` when the terminal provides insert- and delete-character capabilities. This function remains only for historical reasons, since every modern software terminal emulator carries such capabilities.

 curses.has_il()

Give back `True` when the terminal provides insert- and delete-line capabilities, or is able to imitate them through scrolling regions. This function remains only for historical reasons, since every modern software terminal emulator carries such capabilities.

 curses.has_key(*ch*)

Accept a key value *ch* and give back `True` when the present terminal type knows a key carrying that value.

 curses.halfdelay(*tenths*)

Applied for half-delay mode, which resembles cbreak mode in that characters the user types reach the program right away. Yet, having blocked for *tenths* tenths of a second, it raises an exception if nothing has been typed. The *tenths* value has to be a number from `1` to `255`. Call `nocbreak()` to exit half-delay mode.

 curses.init_color(*color_number*, *r*, *g*, *b*)

Redefine a color by taking the number of the color you want changed and then three RGB values (the quantities of the red, green, and blue components). *color_number* has to fall between `0` and `COLORS - 1`. Each of *r*, *g*, *b* has to be a value from `0` to `1000`. After `init_color()` runs, every appearance of that color on the screen switches at once to the fresh definition. On most terminals this function does nothing; it operates only when `can_change_color()` gives back `True`.

 curses.init_pair(*pair_number*, *fg*, *bg*)

Redefine a color-pair. It accepts three arguments: the number of the color-pair you want changed, the foreground color number, and the background color number. *pair_number* has to fall between `1` and `COLOR_PAIRS - 1` (the `0` color pair is changeable only through `use_default_colors()` and `assume_default_colors()`). The *fg* and *bg* arguments have to fall between `0` and `COLORS - 1`, or, once you have called `use_default_colors()` or `assume_default_colors()`, `-1`. When the color-pair had already been initialized, the screen is refreshed and every appearance of that color-pair switches to the fresh definition.

 curses.initscr()

Initialize the library. Hand back a window object standing for the entire screen.

Note

Should an error arise while opening the terminal, the underlying curses library can drive the interpreter to exit.

 curses.is_term_resized(*nlines*, *ncols*)

Give back `True` when `resize_term()` would alter the window structure, and `False` if not.

 curses.isendwin()

Give back `True` when `endwin()` has already been called (meaning the curses library has been deinitialized).

[Subject index](INDEX.md) · [Previous](curses-error-to-curses-endwin.md) · [Continue](curses-keyname-to-curses-qiflush.md) · [Owning module, declaration or section: curses](curses-terminal-handling-for-character-cell-displays.md) · [Owning module, declaration or section: Functions](curses-error-to-curses-endwin.md)
