# curses: Window clearing, deletion, geometry and character input

window.chgat(*attr*)

 window.chgat(*num*, *attr*)

 window.chgat(*y*, *x*, *attr*)

 window.chgat(*y*, *x*, *num*, *attr*)

Apply attributes to *num* characters at the cursor’s current location, or at position `(y, x)` when that is provided. When *num* is omitted or equals `-1`, the attribute applies to every character through to the line’s end. The cursor is moved to position `(y, x)` when that is provided. The altered line is marked via the `touchline()` method, so its content gets redrawn at the next window refresh.

 window.clear()

Behaves like `erase()`, but additionally forces the entire window to be redrawn at the following `refresh()` call.

 window.clearok(*flag*)

When *flag* is `True`, the window is wiped completely at the next `refresh()` call.

 window.clrtobot()

Wipe everything from the cursor down to the window’s end: every line beneath the cursor is removed, followed by the equivalent of `clrtoeol()`.

 window.clrtoeol()

Wipe everything from the cursor to the line’s end.

 window.cursyncup()

Synchronize the current cursor position across all of the window’s ancestors so they match this window’s current cursor position.

 window.delch([*y*, *x*])

Remove whatever character sits at `(y, x)`.

 window.deleteln()

Remove the line beneath the cursor. Every subsequent line shifts up by one line.

 window.derwin(*begin_y*, *begin_x*)

 window.derwin(*nlines*, *ncols*, *begin_y*, *begin_x*)

Short for “derive window”, `derwin()` works exactly like a call to `subwin()`, but with *begin_y* and *begin_x* measured from the window’s origin rather than from the full screen. Return a window object for the derived window.

 window.echochar(*ch*[, *attr*])

Place character *ch* with attribute *attr*, then immediately invoke `refresh()` on the window.

 window.enclose(*y*, *x*)

Check whether the supplied screen-relative character-cell coordinates fall inside the given window, returning `True` or `False`. This helps identify which screen windows surround the spot where a mouse event landed.

Changed in version 3.10: Earlier it returned `1` or `0` rather than `True` or `False`.

 window.encoding

The encoding applied when encoding method arguments (Unicode strings and characters). A subwindow inherits the encoding attribute from its parent window upon creation, such as via `window.subwin()`. The default is the current locale encoding (refer to [`locale.getencoding()`](https://docs.python.org/3.14/library/locale.html#locale.getencoding)).

Added in version 3.3.

 window.erase()

Wipe the window.

 window.getbegyx()

Hand back a tuple `(y, x)` giving the coordinates of the upper-left corner.

 window.getbkgd()

Hand back this window’s present background character/attribute pair.

 window.getch([*y*, *x*])

Fetch a character. Keep in mind the returned integer need *not* fall within ASCII range: function keys, keypad keys, and the like map to numbers above 255. In no-delay mode, `-1` comes back when no input exists; otherwise the call waits for a key press.

 window.get_wch([*y*, *x*])

Fetch a wide character. Most keys yield a character, whereas function keys, keypad keys, and other special keys yield an integer. In no-delay mode, an exception is raised when there is no input.

Added in version 3.3.

[Subject index](INDEX.md) · [Previous](window-addnstr-to-window-box.md) · [Continue](window-getkey-to-window-instr.md) · [Owning module, declaration or section: curses](curses-terminal-handling-for-character-cell-displays.md) · [Owning module, declaration or section: curses.window](curses-window-class.md) · [Owning module, declaration or section: Window Objects](curses-window-class.md)
