# curses: `window.addnstr()`, `window.addstr()`, `window.attroff()`, `window.attron()`, `window.attrset()`, `window.bkgd()`, `window.bkgdset()`, `window.border()`, `window.box()`

window.addnstr(*str*, *n*[, *attr*])

 window.addnstr(*y*, *x*, *str*, *n*[, *attr*])

Render up to *n* characters from the string *str* at `(y, x)` using attributes *attr*, replacing whatever currently occupies those cells.

 window.addstr(*str*[, *attr*])

 window.addstr(*y*, *x*, *str*[, *attr*])

Render the string *str* at `(y, x)` using attributes *attr*, replacing whatever currently occupies those cells.

Note

- Drawing beyond the bounds of a window, subwindow, or pad triggers `curses.error`. When you write into the bottom-right cell of a window, subwindow, or pad, an exception is thrown once the string has been emitted.

- There is a [bug in ncurses](https://bugs.python.org/issue35924) — the library that backs this Python module — that may produce SegFaults during window resizing. The fix shipped in ncurses-6.1-20190511. Should you be limited to an older ncurses, sidestep the problem by never passing a *str* with embedded newlines to `addstr()`. Make a separate `addstr()` call per line instead.

 window.attroff(*attr*)

Drop attribute *attr* from the “background” collection that governs every write into the active window.

 window.attron(*attr*)

Append attribute *attr* to the “background” collection that governs every write into the active window.

 window.attrset(*attr*)

Define the “background” attribute collection as *attr*. That collection starts out as `0` (no attributes).

 window.bkgd(*ch*[, *attr*])

Assign the window’s background property to the character *ch* together with attributes *attr*. That update then propagates across every cell in the window:

- Each character’s attribute throughout the window switches to the new background attribute.

- Anywhere the old background character is found, it is replaced by the new background character.

 window.bkgdset(*ch*[, *attr*])

Define the background of the window. The background of a window pairs a character with whatever attributes you choose. The attribute portion of the background is OR’ed together with each non-blank character written into the window. Both the character and attribute portions of the background apply to blank characters. The background attaches to the character as a property and travels with it through every scroll and insert/delete line/character operation.

 window.border([*ls*[, *rs*[, *ts*[, *bs*[, *tl*[, *tr*[, *bl*[, *br*]]]]]]]])

Render a border surrounding the window’s edges. Every parameter names the character used for one segment of the border; consult the table below for specifics.

Note

Passing `0` for any parameter selects the default character for that slot. Keyword parameters are *not* permitted. The table lists the defaults:

| Parameter | Description | Default value |
| --- | --- | --- |
| *ls* | Left side | `ACS_VLINE` |
| *rs* | Right side | `ACS_VLINE` |
| *ts* | Top | `ACS_HLINE` |
| *bs* | Bottom | `ACS_HLINE` |
| *tl* | Upper-left corner | `ACS_ULCORNER` |
| *tr* | Upper-right corner | `ACS_URCORNER` |
| *bl* | Bottom-left corner | `ACS_LLCORNER` |
| *br* | Bottom-right corner | `ACS_LRCORNER` |

 window.box([*vertch*, *horch*])

Comparable to `border()`, except both *ls* and *rs* take *vertch* while both *ts* and *bs* take *horch*. This function always relies on the default corner characters.

[Subject index](INDEX.md) · [Continue](window-chgat-to-window-get-wch.md) · [Owning module, declaration or section: curses](curses-terminal-handling-for-character-cell-displays.md) · [Owning module, declaration or section: curses.window](curses-window-class.md) · [Owning module, declaration or section: Window Objects](curses-window-class.md) · [Owning module, declaration or section: window.addch; window.addch](window-addch.md)
