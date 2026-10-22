# Starting and ending a curses application

### Starting and ending a curses application

curses has to be initialized before you do anything else. You accomplish this by invoking the [`initscr()`](https://docs.python.org/3.14/library/curses.html#curses.initscr) function, which identifies the terminal type, dispatches whatever setup codes the terminal needs, and builds assorted internal data structures. When it succeeds, `initscr()` hands back a window object standing for the whole screen; by convention this gets the name `stdscr`, mirroring the corresponding C variable’s name.

```python
import curses
stdscr = curses.initscr()

```

To be able to read keys yet only show them in particular situations, curses applications normally disable automatic echoing of keystrokes to the screen. Doing so means invoking the [`noecho()`](https://docs.python.org/3.14/library/curses.html#curses.noecho) function.

```python
curses.noecho()

```

Frequently applications must also respond to keys at once, with no need for the Enter key to be hit; this is termed cbreak mode, in contrast to the standard buffered input mode.

```python
curses.cbreak()

```

As a rule terminals deliver special keys—the cursor keys, or navigation keys like Page Up and Home—as an escape sequence of several bytes. You could code your application to anticipate and handle such sequences yourself, but curses is able to handle that for you, instead returning a special value like [`curses.KEY_LEFT`](https://docs.python.org/3.14/library/curses.html#curses.KEY_LEFT). For curses to take care of this, you must turn on keypad mode.

```python
stdscr.keypad(True)

```

Shutting down a curses application is far simpler than firing one up. You’ll need to call:

```python
curses.nocbreak()
stdscr.keypad(False)
curses.echo()

```

to undo the curses-friendly terminal settings. After that, call the [`endwin()`](https://docs.python.org/3.14/library/curses.html#curses.endwin) function so the terminal returns to its original operating mode.

```python
curses.endwin()

```

One frequent headache while debugging a curses application is winding up with a scrambled terminal because the application died without putting the terminal back the way it was. Under Python this typically arises when your code has a bug and throws an uncaught exception. For instance, your keystrokes are no longer echoed to the screen as you type, which turns using the shell into a chore.

You can sidestep these headaches in Python and greatly simplify debugging by importing the [`curses.wrapper()`](https://docs.python.org/3.14/library/curses.html#curses.wrapper) function and applying it as shown:

```python
from curses import wrapper

def main(stdscr):
    # Clear screen
    stdscr.clear()

    # This raises ZeroDivisionError when i == 10.
    for i in range(0, 11):
        v = i-10
        stdscr.addstr(i, 0, '10 divided by {} is {}'.format(v, 10/v))

        stdscr.refresh()
        stdscr.getkey()

wrapper(main)

```

A callable object is what the [`wrapper()`](https://docs.python.org/3.14/library/curses.html#curses.wrapper) function accepts, and it performs the initializations outlined above, additionally setting up colors whenever color support exists. `wrapper()` next executes the callable you handed it. As soon as that callable returns, `wrapper()` puts the terminal back into its original state. Invocation of the callable happens within a [`try`](https://docs.python.org/3.14/reference/compound_stmts.html#try)…[`except`](https://docs.python.org/3.14/reference/compound_stmts.html#except) that traps exceptions, restores the terminal’s state, and afterward re-raises the exception. As a result an exception won’t leave your terminal in a strange condition and you’ll still be able to read the exception’s message together with its traceback.

[Subject index](INDEX.md) · [Previous source context](the-python-curses-module.md) · [Following source context](windows-and-pads.md)
