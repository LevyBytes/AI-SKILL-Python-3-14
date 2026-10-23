# Termios

# Termios

### `termios` - POSIX style tty control

---

This module exposes the POSIX system calls used for tty I/O control. The full account of those calls lives in the *[termios(3)](https://manpages.debian.org/termios(3))* Unix manual page. Support is limited to Unix releases that ship POSIX *termios* style tty I/O control and have it configured at installation time.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

Every function here expects a file descriptor *fd* as its leading argument. That value may be a plain integer descriptor — for instance one handed back by `sys.stdin.fileno()` — or a [file object](https://docs.python.org/3.14/glossary.html#term-file-object) like `sys.stdin` directly.

Alongside the functions, this module exports all the constants required to drive them; each carries the same name as its C equivalent. Consult your platform's own documentation when you need details on driving these terminal control interfaces.

These are the functions the module makes available:

`termios.tcgetattr(*fd*)`

Hand back a list holding the tty attributes belonging to file descriptor *fd*, in this shape: `[iflag, oflag, cflag, lflag, ispeed, ospeed, cc]` where *cc* is itself a list of the tty special characters (each one a string of length 1, apart from the entries at indices `VMIN` and `VTIME`, which come back as integers wherever those fields exist). Reading the flags and speeds, and indexing into the *cc* array, must be done through the symbolic constants the `termios` module declares.

`termios.tcsetattr(*fd*, *when*, *attributes*)`

Apply the tty attributes to file descriptor *fd* drawn from *attributes*, a list shaped like the one `tcgetattr()` produces. The moment at which the change happens is governed by the *when* argument:

`termios.TCSANOW`

Apply the attribute change right away.

`termios.TCSADRAIN`

Apply the change only once every queued output byte has gone out.

`termios.TCSAFLUSH`

Apply the change after all queued output is sent and any queued input is thrown away.

`termios.tcsendbreak(*fd*, *duration*)`

Emit a break on file descriptor *fd*. When *duration* is zero the break lasts between 0.25–0.5 seconds; any nonzero *duration* carries a meaning that depends on the system.

`termios.tcdrain(*fd*)`

Block until every byte written to file descriptor *fd* has finished transmitting.

`termios.tcflush(*fd*, *queue*)`

Throw away queued data on file descriptor *fd*. Which queue is cleared depends on the *queue* selector: `TCIFLUSH` targets the input queue, `TCOFLUSH` the output queue, or `TCIOFLUSH` clears both at once.

`termios.tcflow(*fd*, *action*)`

Halt or resume the flow of input or output on file descriptor *fd*. Allowed values for the *action* argument are `TCOOFF` to pause output, `TCOON` to resume output, `TCIOFF` to pause input, or `TCION` to resume input.

`termios.tcgetwinsize(*fd*)`

Produce a tuple `(ws_row, ws_col)` holding the tty window dimensions for file descriptor *fd*. Needs `termios.TIOCGWINSZ` or `termios.TIOCGSIZE`.

Added in version 3.11.

`termios.tcsetwinsize(*fd*, *winsize*)`

Apply the tty window dimensions to file descriptor *fd*, taken from *winsize* — a two-item tuple `(ws_row, ws_col)` matching what `tcgetwinsize()` returns. At least one pair out of (`termios.TIOCGWINSZ`, `termios.TIOCSWINSZ`); (`termios.TIOCGSIZE`, `termios.TIOCSSIZE`) has to be defined.

Added in version 3.11.

See also

Module [`tty`](https://docs.python.org/3.14/library/tty.html#module-tty)

Helper routines for the usual terminal control jobs.

### Example

Below is a routine that requests a password while keeping echo switched off. Observe the pattern of pairing a standalone `tcgetattr()` call with a [`try`](https://docs.python.org/3.14/reference/compound_stmts.html#try) … [`finally`](https://docs.python.org/3.14/reference/compound_stmts.html#finally) statement, which guarantees the previous tty attributes are put back precisely whatever occurs:

```python
def getpass(prompt="Password: "):
    import termios, sys
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    new = termios.tcgetattr(fd)
    new[3] = new[3] & ~termios.ECHO          # lflags
    try:
        termios.tcsetattr(fd, termios.TCSADRAIN, new)
        passwd = input(prompt)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)
    return passwd

```

[Subject index](INDEX.md)
