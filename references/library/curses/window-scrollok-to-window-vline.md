# curses: Window scrolling, subwindows and touch synchronization

window.scrollok(*flag*)

Govern the behavior when a window’s cursor moves past the window’s edge or scrolling region — whether from a newline action on the bottom line or from typing the final character of the final line. When *flag* is `False`, the cursor stays on the bottom line. When *flag* is `True`, the window scrolls up by one line. Note that producing the physical scrolling effect on the terminal additionally requires calling `idlok()`.

 window.setscrreg(*top*, *bottom*)

Establish the scrolling region spanning from line *top* through line *bottom*. Every scrolling action happens inside this region.

 window.standend()

Disable the standout attribute. On certain terminals this also has the effect of disabling every attribute.

 window.standout()

Enable attribute *A_STANDOUT*.

 window.subpad(*begin_y*, *begin_x*)

 window.subpad(*nlines*, *ncols*, *begin_y*, *begin_x*)

Return a sub-window whose upper-left corner sits at `(begin_y, begin_x)` and whose width and height are *ncols* and *nlines*.

 window.subwin(*begin_y*, *begin_x*)

 window.subwin(*nlines*, *ncols*, *begin_y*, *begin_x*)

Return a sub-window whose upper-left corner sits at `(begin_y, begin_x)` and whose width and height are *ncols* and *nlines*.

By default the sub-window stretches from the given position down to the window’s lower right corner.

 window.syncdown()

Touch each location within the window that any of its ancestor windows has touched. Because `refresh()` invokes this routine, you should rarely ever need to call it on your own.

 window.syncok(*flag*)

When *flag* is `True`, `syncup()` runs automatically each time the window changes.

 window.syncup()

Touch every spot in the window’s ancestors that has been changed within the window.

 window.timeout(*delay*)

Choose blocking or non-blocking read behavior for the window. When *delay* is negative, blocking reads apply (waiting indefinitely for input). When *delay* is zero, non-blocking reads apply, and `getch()` returns `-1` when no input is pending. When *delay* is positive, `getch()` blocks for *delay* milliseconds and returns `-1` when no input has arrived by then.

 window.touchline(*start*, *count*[, *changed*])

Act as though *count* lines changed, beginning at line *start*. When *changed* is provided, it dictates whether the impacted lines are flagged as changed (*changed*`=True`) or unchanged (*changed*`=False`).

 window.touchwin()

Act as though the entire window changed, for the sake of drawing optimizations.

 window.untouchwin()

Flag every line in the window as unchanged since the most recent `refresh()` call.

 window.vline(*ch*, *n*[, *attr*])

 window.vline(*y*, *x*, *ch*, *n*[, *attr*])

Draw a vertical line that begins at `(y, x)`, spans length *n*, and is built from the character *ch* with attributes *attr*.

[Subject index](INDEX.md) · [Previous](window-is-linetouched-to-window-scroll.md) · [Continue](curses-err-to-curses-cols.md) · [Owning module, declaration or section: curses](curses-terminal-handling-for-character-cell-displays.md) · [Owning module, declaration or section: curses.window](curses-window-class.md) · [Owning module, declaration or section: Window Objects](curses-window-class.md)
