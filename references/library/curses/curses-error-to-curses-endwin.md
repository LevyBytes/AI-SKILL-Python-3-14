# curses: Curses exceptions, colors and terminal initialization

### Functions

The module `curses` defines the following exception:

 *exception *curses.error

Raised when a function from the curses library reports an error.

Note

Anytime the *x* or *y* arguments passed to a function or method are optional, they fall back to the cursor's present position. Anytime *attr* is optional, it falls back to `A_NORMAL`.

The module `curses` defines the following functions:

 curses.assume_default_colors(*fg*, *bg*, */*)

Permit colors to take on default values on terminals that offer this feature. Reach for this when your application needs transparency support.

- Map the terminal's default foreground/background colors onto color number `-1`. Thus `init_pair(x, COLOR_RED, -1)` sets up pair *x* as red over the default background, while `init_pair(x, -1, COLOR_BLUE)` sets up pair *x* as the default foreground over blue.

- Redefine the color-pair `0` to be `(fg, bg)`.

Added in version 3.14.

 curses.baudrate()

Give back the terminal's output rate measured in bits per second. On software terminal emulators this returns a constant high figure. It survives for historical reasons; long ago it served to build output loops for timing delays and now and then to vary behavior according to line speed.

 curses.beep()

Sound a brief attention tone.

 curses.can_change_color()

Give back `True` or `False`, according to whether the programmer is able to alter the colors the terminal shows.

 curses.cbreak()

Switch into cbreak mode. Under cbreak mode (occasionally labeled “rare” mode), the usual tty line buffering is switched off and characters become readable one at a time. Yet, in contrast to raw mode, special characters (interrupt, quit, suspend, and flow control) keep their influence over the tty driver and the calling program. Invoking `raw()` first and then `cbreak()` leaves the terminal sitting in cbreak mode.

 curses.color_content(*color_number*)

Give back how intense the red, green, and blue (RGB) components are within the color *color_number*, a value required to fall between `0` and `COLORS - 1`. The result is a 3-tuple holding the R,G,B values for that color, each ranging from `0` (no component) up to `1000` (the largest amount of the component).

 curses.color_pair(*pair_number*)

Give back the attribute value used to render text in the named color pair. Only the first 256 color pairs are supported. You may merge this attribute value with `A_STANDOUT`, `A_REVERSE`, and the rest of the `A_*` attributes. The function `pair_number()` is this one's inverse.

 curses.curs_set(*visibility*)

Set how the cursor appears. *visibility* accepts `0`, `1`, or `2`, meaning invisible, normal, or very visible. Where the terminal can honor the requested visibility, the prior cursor state is returned; otherwise an exception is raised. On a lot of terminals, the “visible” mode shows up as an underline cursor and the “very visible” mode as a block cursor.

 curses.def_prog_mode()

Record the present terminal mode as the “program” mode — the mode in effect while the running program is using curses. (The opposite is the “shell” mode, for moments when the program is not in curses.) Later calls to `reset_prog_mode()` bring this mode back.

 curses.def_shell_mode()

Record the present terminal mode as the “shell” mode — the mode in effect while the running program is not using curses. (The opposite is the “program” mode, when the program is using curses capabilities.) Later calls to `reset_shell_mode()` bring this mode back.

 curses.delay_output(*ms*)

Introduce a pause of *ms* milliseconds into output.

 curses.doupdate()

Refresh the physical screen. The curses library maintains two data structures: one mirrors the current physical screen contents, while a virtual screen captures the desired upcoming state. Calling `doupdate()` brings the physical screen into agreement with that virtual screen.

You can revise the virtual screen through a `noutrefresh()` call once write operations such as `addstr()` have run against a window. An ordinary `refresh()` call amounts to `noutrefresh()` chained with `doupdate()`; when several windows need updating, you can boost performance and possibly cut down screen flicker by firing `noutrefresh()` against every window and then a lone `doupdate()`.

 curses.echo()

Switch into echo mode. While echo mode is active, each character that arrives is echoed to the screen at the moment it is entered.

 curses.endwin()

De-initialize the library, and bring the terminal back to its normal state.

[Subject index](INDEX.md) · [Previous](curses-terminal-handling-for-character-cell-displays.md) · [Continue](curses-erasechar-to-curses-isendwin.md) · [Owning module, declaration or section: curses](curses-terminal-handling-for-character-cell-displays.md)
