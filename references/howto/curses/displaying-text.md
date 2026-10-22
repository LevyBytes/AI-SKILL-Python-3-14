# Displaying Text

### Displaying Text

To a C programmer, curses can at times resemble a tangled labyrinth of functions, every one differing in some subtle way. For instance, `addstr()` shows a string at the current cursor spot in the `stdscr` window, whereas `mvaddstr()` first moves to a supplied y,x coordinate before showing the string. `waddstr()` works exactly like `addstr()` except that it lets you name a window to use rather than defaulting to `stdscr`. `mvwaddstr()` lets you name both a window and a coordinate.

Happily, all of these details are concealed by the Python interface. `stdscr` is a window object just like any other, and methods such as [`addstr()`](https://docs.python.org/3.14/library/curses.html#curses.window.addstr) take several argument forms. There are normally four distinct forms.

| Form | Description |
| --- | --- |
| *str* or *ch* | At the present position, render the string *str* or character *ch* |
| *str* or *ch*, *attr* | At the present position, render the string *str* or character *ch*, applying attribute *attr* |
| *y*, *x*, *str* or *ch* | Relocate to position *y,x* inside the window, then render *str* or *ch* |
| *y*, *x*, *str* or *ch*, *attr* | Relocate to position *y,x* inside the window, then render *str* or *ch*, applying attribute *attr* |

Through attributes you can render text in emphasized styles like boldface, underline, reverse code, or color. The following subsection will go into them more thoroughly.

As the value to render, the [`addstr()`](https://docs.python.org/3.14/library/curses.html#curses.window.addstr) method accepts a Python string or bytestring. A bytestring’s contents go to the terminal unchanged. Strings get encoded into bytes via the value held in the window’s [`encoding`](https://docs.python.org/3.14/library/curses.html#curses.window.encoding) attribute; that defaults to the default system encoding that [`locale.getencoding()`](https://docs.python.org/3.14/library/locale.html#locale.getencoding) returns.

A character is what the [`addch()`](https://docs.python.org/3.14/library/curses.html#curses.window.addch) methods accept; that character may be an integer, a length-1 bytestring, or a length-1 string.

For extension characters, constants are supplied; these constants are integers above 255. As an example, [`ACS_PLMINUS`](https://docs.python.org/3.14/library/curses.html#curses.ACS_PLMINUS) is a +/- symbol, while [`ACS_ULCORNER`](https://docs.python.org/3.14/library/curses.html#curses.ACS_ULCORNER) is the upper left corner of a box (useful when drawing borders). Alternatively you may use the matching Unicode character.

Because windows keep track of where the cursor sat after the previous operation, if you omit the *y,x* coordinates the string or character lands wherever the previous operation finished. The cursor can also be relocated with the `move(y,x)` method. Since certain terminals always show a flashing cursor, you may want to make sure the cursor rests somewhere it won’t prove distracting; a cursor blinking at some seemingly random spot can be confusing.

Should your application not require a blinking cursor whatsoever, you can call `curs_set(False)` to render it invisible. So that older curses versions stay compatible, there’s a `leaveok(bool)` function that acts as a synonym for [`curs_set()`](https://docs.python.org/3.14/library/curses.html#curses.curs_set). With *bool* set to true, the curses library will try to hide the flashing cursor, freeing you from worrying about where it’s been left.

[Subject index](INDEX.md) · [Previous source context](windows-and-pads.md) · [Following source context](attributes-and-color.md)
