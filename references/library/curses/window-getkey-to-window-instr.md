# curses: Window key input, line insertion and text inspection

window.getkey([*y*, *x*])

Fetch a character and hand back a string rather than an integer the way `getch()` does. Function keys, keypad keys, and other special keys yield a multibyte string holding the key name. In no-delay mode, an exception is raised when there is no input.

 window.getmaxyx()

Hand back a tuple `(y, x)` holding the window’s height and width.

 window.getparyx()

Hand back this window’s starting coordinates measured against its parent window as a tuple `(y, x)`. Return `(-1, -1)` when this window lacks a parent.

 window.getstr()

 window.getstr(*n*)

 window.getstr(*y*, *x*)

 window.getstr(*y*, *x*, *n*)

Read a bytes object from the user, offering basic line-editing support. The largest permitted value for *n* is 2047.

Changed in version 3.14: The largest permitted value for *n* rose from 1023 to 2047.

 window.getyx()

Hand back a tuple `(y, x)` giving the cursor’s present position measured against the window’s upper-left corner.

 window.hline(*ch*, *n*)

 window.hline(*y*, *x*, *ch*, *n*)

Draw a horizontal line that begins at `(y, x)`, spans length *n*, and is built from the character *ch*.

 window.idcok(*flag*)

When *flag* is `False`, curses stops contemplating the terminal’s hardware insert/delete character capability; when *flag* is `True`, character insertion and deletion become available. At the point curses is first set up, character insert/delete is enabled by default.

 window.idlok(*flag*)

When *flag* is `True`, `curses` attempts to leverage hardware line-editing facilities. Otherwise, line insertion and deletion stay off.

 window.immedok(*flag*)

When *flag* is `True`, every alteration to the window image refreshes the window automatically, sparing you from calling `refresh()` directly. That said, performance can suffer noticeably because of frequent wrefresh calls. This option starts out disabled.

 window.inch([*y*, *x*])

Hand back the character occupying the given window position. The lower 8 bits hold the character itself, while the higher bits hold the attributes.

 window.insch(*ch*[, *attr*])

 window.insch(*y*, *x*, *ch*[, *attr*])

Render character *ch* at `(y, x)` with attributes *attr*, pushing the line one character to the right from position *x*.

 window.insdelln(*nlines*)

Add *nlines* lines into the named window above the present line. The *nlines* lines at the bottom are discarded. When *nlines* is negative, remove *nlines* lines beginning with the one beneath the cursor and shift the remaining lines up. The bottom *nlines* lines are cleared. The cursor’s current position is unchanged.

 window.insertln()

Add an empty line beneath the cursor. Every subsequent line shifts down by one line.

 window.insnstr(*str*, *n*[, *attr*])

 window.insnstr(*y*, *x*, *str*, *n*[, *attr*])

Add a character string (only as many characters as fit on the line) ahead of the character under the cursor, capped at *n* characters. When *n* is zero or negative, the whole string is added. Every character to the cursor’s right shifts right, and the line’s rightmost characters drop off. The cursor position stays put (after moving to *y*, *x*, when specified).

 window.insstr(*str*[, *attr*])

 window.insstr(*y*, *x*, *str*[, *attr*])

Add a character string (only as many characters as fit on the line) ahead of the character under the cursor. Every character to the cursor’s right shifts right, and the line’s rightmost characters drop off. The cursor position stays put (after moving to *y*, *x*, when specified).

 window.instr([*n*])

 window.instr(*y*, *x*[, *n*])

Hand back a bytes object of characters pulled from the window beginning at the current cursor position, or at *y*, *x* when specified. Attributes are removed from the characters. When *n* is specified, `instr()` hands back a string no longer than *n* characters (not counting the trailing NUL). The largest permitted value for *n* is 2047.

Changed in version 3.14: The largest permitted value for *n* rose from 1023 to 2047.

[Subject index](INDEX.md) · [Previous](window-chgat-to-window-get-wch.md) · [Continue](window-is-linetouched-to-window-scroll.md) · [Owning module, declaration or section: curses](curses-terminal-handling-for-character-cell-displays.md) · [Owning module, declaration or section: curses.window](curses-window-class.md) · [Owning module, declaration or section: Window Objects](curses-window-class.md)
