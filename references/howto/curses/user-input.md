# User Input

### User Input

Only very simple input mechanisms come with the C curses library. Python’s [`curses`](https://docs.python.org/3.14/library/curses.html#module-curses) module throws in a basic text-input widget. (Wider assortments of widgets come with other libraries such as [Urwid](https://pypi.org/project/Urwid/).)

Getting input from a window can be done in two ways:

- [`getch()`](https://docs.python.org/3.14/library/curses.html#curses.window.getch) refreshes the screen and then holds until the user presses a key, echoing the key if [`echo()`](https://docs.python.org/3.14/library/curses.html#curses.echo) was called beforehand. You may, if you wish, supply a coordinate to which the cursor should move before it pauses.

- [`getkey()`](https://docs.python.org/3.14/library/curses.html#curses.window.getkey) performs the same operation but turns the integer into a string. A single character comes back as a 1-character string, while special keys like function keys come back as longer strings holding a key name such as `KEY_UP` or `^G`.

Using the [`nodelay()`](https://docs.python.org/3.14/library/curses.html#curses.window.nodelay) window method, you can avoid waiting on the user. Following `nodelay(True)`, the window’s `getch()` and `getkey()` turn non-blocking. To indicate that no input is ready, `getch()` returns `curses.ERR` (a value of -1) while `getkey()` raises an exception. A [`halfdelay()`](https://docs.python.org/3.14/library/curses.html#curses.halfdelay) function also exists, which serves to (in effect) put a timer on every `getch()`; should no input arrive within a stated delay (counted in tenths of a second), curses raises an exception.

What the `getch()` method returns is an integer; should it fall between 0 and 255, it stands for the ASCII code of the pressed key. Values above 255 are special keys like Page Up, Home, or the cursor keys. You can match the returned value against constants such as [`curses.KEY_PPAGE`](https://docs.python.org/3.14/library/curses.html#curses.KEY_PPAGE), [`curses.KEY_HOME`](https://docs.python.org/3.14/library/curses.html#curses.KEY_HOME), or [`curses.KEY_LEFT`](https://docs.python.org/3.14/library/curses.html#curses.KEY_LEFT). Your program’s main loop might resemble the following:

```python
while True:
    c = stdscr.getch()
    if c == ord('p'):
        PrintDocument()
    elif c == ord('q'):
        break  # Exit the while loop
    elif c == curses.KEY_HOME:
        x = y = 0

```

ASCII class-membership functions that accept either integer or 1-character string arguments are supplied by the [`curses.ascii`](https://docs.python.org/3.14/library/curses.ascii.html#module-curses.ascii) module; these can help you write more legible tests inside such loops. The module also furnishes conversion functions that accept either integer or 1-character-string arguments and hand back the same type. As an example, [`curses.ascii.ctrl()`](https://docs.python.org/3.14/library/curses.ascii.html#curses.ascii.ctrl) hands back the control character matching its argument.

A method to fetch a whole string, [`getstr()`](https://docs.python.org/3.14/library/curses.html#curses.window.getstr), is also available. It sees little use, since what it can do is rather limited; the sole editing keys on offer are the backspace key and the Enter key, the latter ending the string. You may optionally cap it at a set number of characters.

```python
curses.echo()            # Enable echoing of characters

# Get a 15-character string, with the cursor on the top line
s = stdscr.getstr(0,0, 15)

```

A text box backing an Emacs-style set of keybindings is provided by the [`curses.textpad`](https://docs.python.org/3.14/library/curses.html#module-curses.textpad) module. Several methods on the [`Textbox`](https://docs.python.org/3.14/library/curses.html#curses.textpad.Textbox) class enable editing with input validation as well as collecting the edit results either keeping or dropping trailing spaces. Here’s an example:

```python
import curses
from curses.textpad import Textbox, rectangle

def main(stdscr):
    stdscr.addstr(0, 0, "Enter IM message: (hit Ctrl-G to send)")

    editwin = curses.newwin(5,30, 2,1)
    rectangle(stdscr, 1,0, 1+5+1, 1+30+1)
    stdscr.refresh()

    box = Textbox(editwin)

    # Let the user edit until Ctrl-G is struck.
    box.edit()

    # Get resulting contents
    message = box.gather()

```

For more details, see the library documentation on [`curses.textpad`](https://docs.python.org/3.14/library/curses.html#module-curses.textpad).

[Subject index](INDEX.md) · [Following source continuation](curses-further-information-and-api-coverage.md) · [Previous source context](attributes-and-color.md) · [Following source context](curses-further-information-and-api-coverage.md)
