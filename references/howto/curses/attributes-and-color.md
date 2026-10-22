# Attributes and Color

### Attributes and Color

There are several ways characters can be shown. A text-based application’s status lines are often rendered in reverse video, and a text viewer might have to highlight particular words. curses enables this by letting you assign an attribute to every cell on the screen.

An attribute is an integer in which each bit stands for a different attribute. You may attempt to render text with several attribute bits turned on, yet curses makes no promise that every possible combination is supported, or that they’re all visually separate. That hinges on what the terminal in use can do, so the safest course is to keep to the most widely supported attributes, which are listed here.

| Attribute | Description |
| --- | --- |
| `A_BLINK` | Blinking text |
| `A_BOLD` | Extra bright or bold text |
| `A_DIM` | Half bright text |
| `A_REVERSE` | Reverse-video text |
| `A_STANDOUT` | The best highlighting mode available |
| `A_UNDERLINE` | Underlined text |

Hence, to show a reverse-video status line along the screen’s top line, you might write:

```python
stdscr.addstr(0, 0, "Current mode: Typing mode",
              curses.A_REVERSE)
stdscr.refresh()

```

On terminals that offer it, the curses library also handles color. The most widespread such terminal is likely the Linux console, with color xterms close behind.

For color, you have to call the [`start_color()`](https://docs.python.org/3.14/library/curses.html#curses.start_color) function shortly after calling [`initscr()`](https://docs.python.org/3.14/library/curses.html#curses.initscr) in order to set up the default color set (the [`curses.wrapper()`](https://docs.python.org/3.14/library/curses.html#curses.wrapper) function handles this on its own). With that done, the [`has_colors()`](https://docs.python.org/3.14/library/curses.html#curses.has_colors) function returns TRUE when the terminal being used really can show color. (Note: the American spelling ‘color’ is what curses uses, rather than the Canadian/British spelling ‘colour’. Anyone accustomed to the British spelling will simply have to accept misspelling it for the benefit of these functions.)

curses keeps a limited set of color pairs, each holding a foreground (that is, text) color and a background color. The [`color_pair()`](https://docs.python.org/3.14/library/curses.html#curses.color_pair) function gives you the attribute value matching a color pair; you can bitwise-OR this with other attributes such as [`A_REVERSE`](https://docs.python.org/3.14/library/curses.html#curses.A_REVERSE), though, once more, such combinations aren’t guaranteed to function on every terminal.

Here is an example that shows a line of text using color pair 1:

```python
stdscr.addstr("Pretty text", curses.color_pair(1))
stdscr.refresh()

```

Like I said before, a color pair is made up of a foreground and a background color. The `init_pair(n, f, b)` function redefines color pair *n*, giving it foreground color f and background color b. Color pair 0 is fixed at white on black and cannot be altered.

Colors carry numbers, and [`start_color()`](https://docs.python.org/3.14/library/curses.html#curses.start_color) sets up 8 basic colors as it switches on color mode. These are: 0:black, 1:red, 2:green, 3:yellow, 4:blue, 5:magenta, 6:cyan, and 7:white. Named constants for each of these colors are defined by the [`curses`](https://docs.python.org/3.14/library/curses.html#module-curses) module: [`curses.COLOR_BLACK`](https://docs.python.org/3.14/library/curses.html#curses.COLOR_BLACK), [`curses.COLOR_RED`](https://docs.python.org/3.14/library/curses.html#curses.COLOR_RED), and so on.

Let’s bring all of this together. To set color 1 to red text on a white background, you would call:

```python
curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)

```

After you redefine a color pair, any text already on screen that used that color pair shifts to the new colors. New text can also be shown in this color via:

```python
stdscr.addstr(0,0, "RED ALERT!", curses.color_pair(1))

```

Especially advanced terminals can redefine the actual colors to a chosen RGB value. This lets you change color 1, which is normally red, into purple or blue or whatever other color you fancy. Regrettably, the Linux console doesn’t support this, so I can’t experiment with it and have no examples to offer. To check whether your terminal can do this, call [`can_change_color()`](https://docs.python.org/3.14/library/curses.html#curses.can_change_color), which returns `True` when the capability exists. If you happen to own such a gifted terminal, consult your system’s man pages for further details.

[Subject index](INDEX.md) · [Previous source context](displaying-text.md) · [Following source context](user-input.md)
