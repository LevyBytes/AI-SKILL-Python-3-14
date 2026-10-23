# Tty

# Tty

### `tty` - Terminal control functions

**Source code:** [Lib/tty.py](https://github.com/python/cpython/tree/3.14/Lib/tty.py)

---

Functions for switching a tty into cbreak mode and raw mode are what the `tty` module provides.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

Since the [`termios`](https://docs.python.org/3.14/library/termios.html#module-termios) module is a prerequisite, usage is confined to Unix.

These are the functions exposed by the `tty` module:

`tty.cfmakeraw(*mode*)`

Takes the tty attribute list *mode* — a list shaped like whatever [`termios.tcgetattr()`](https://docs.python.org/3.14/library/termios.html#termios.tcgetattr) returns — and transforms it into the attributes of a tty running in raw mode.

Added in version 3.12.

`tty.cfmakecbreak(*mode*)`

Takes the tty attribute list *mode* — a list shaped like whatever [`termios.tcgetattr()`](https://docs.python.org/3.14/library/termios.html#termios.tcgetattr) returns — and transforms it into the attributes of a tty running in cbreak mode.

Both the `ECHO` and `ICANON` local mode flags inside *mode* are turned off, and at the same time the minimum input is fixed at 1 byte with zero delay.

Added in version 3.12.

Changed in version 3.12.2: The `ICRNL` flag stays untouched now. That aligns with how `stty cbreak` acts on Linux and macOS, and with the long-standing conduct of `setcbreak()`.

`tty.setraw(*fd*, *when=termios.TCSAFLUSH*)`

Switches the file descriptor *fd* into raw mode. When *when* is left out, the default is [`termios.TCSAFLUSH`](https://docs.python.org/3.14/library/termios.html#termios.TCSAFLUSH), and that argument flows on to [`termios.tcsetattr()`](https://docs.python.org/3.14/library/termios.html#termios.tcsetattr). Just before *fd* is flipped to raw mode, the result of [`termios.tcgetattr()`](https://docs.python.org/3.14/library/termios.html#termios.tcgetattr) is captured, and that captured value becomes the return value.

Changed in version 3.12: Rather than `None`, what comes back is now the tty's original attributes.

`tty.setcbreak(*fd*, *when=termios.TCSAFLUSH*)`

Switches the file descriptor *fd* into cbreak mode. When *when* is left out, the default is [`termios.TCSAFLUSH`](https://docs.python.org/3.14/library/termios.html#termios.TCSAFLUSH), and that argument flows on to [`termios.tcsetattr()`](https://docs.python.org/3.14/library/termios.html#termios.tcsetattr). Just before *fd* is flipped to cbreak mode, the result of [`termios.tcgetattr()`](https://docs.python.org/3.14/library/termios.html#termios.tcgetattr) is captured, and that captured value becomes the return value.

Both the `ECHO` and `ICANON` local mode flags are turned off, and at the same time the minimum input is fixed at 1 byte with zero delay.

Changed in version 3.12: Where `None` once came back, the call now yields the tty's original attributes.

Changed in version 3.12.2: The `ICRNL` flag now stays in place. This brings back how Python 3.11 and earlier behaved, and it lines up with the cbreak-mode descriptions Linux, macOS, & BSDs give in their `stty(1)` man pages.

See also

Module [`termios`](https://docs.python.org/3.14/library/termios.html#module-termios)

The low-level interface for controlling a terminal.

[Subject index](INDEX.md)
