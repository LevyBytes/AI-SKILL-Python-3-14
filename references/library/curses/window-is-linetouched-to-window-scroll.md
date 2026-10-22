# curses: Window updates, movement, overlays and refresh

window.is_linetouched(*line*)

Return `True` when the named line changed since the most recent `refresh()` call; otherwise return `False`. Raise a `curses.error` exception when *line* is not valid for the given window.

 window.is_wintouched()

Return `True` when the named window changed since the most recent `refresh()` call; otherwise return `False`.

 window.keypad(*flag*)

When *flag* is `True`, `curses` interprets the escape sequences that certain keys (keypad, function keys) emit. When *flag* is `False`, those escape sequences remain untouched within the input stream.

 window.leaveok(*flag*)

When *flag* is `True`, the cursor stays wherever it is across updates rather than returning to the “cursor position.” This cuts down on cursor movement when feasible. Where supported, the cursor is hidden.

When *flag* is `False`, the cursor always lands at the “cursor position” following an update.

 window.move(*new_y*, *new_x*)

Reposition the cursor to `(new_y, new_x)`.

 window.mvderwin(*y*, *x*)

Relocate the window within its parent window. The window’s screen-relative parameters stay the same. This routine serves to show distinct regions of the parent window at one fixed physical spot on the screen.

 window.mvwin(*new_y*, *new_x*)

Relocate the window so that its upper-left corner sits at `(new_y, new_x)`.

 window.nodelay(*flag*)

When *flag* is `True`, `getch()` operates without blocking.

 window.notimeout(*flag*)

When *flag* is `True`, escape sequences are never timed out.

When *flag* is `False`, after a brief interval of a few milliseconds, an escape sequence goes uninterpreted and stays within the input stream untouched.

 window.noutrefresh()

Queue a refresh without acting yet. This function revises the data structure that captures the window’s intended state, but it does not push an update to the physical screen. Call `doupdate()` to make that happen.

 window.overlay(*destwin*[, *sminrow*, *smincol*, *dminrow*, *dmincol*, *dmaxrow*, *dmaxcol*])

Lay the window over *destwin*. The two windows need not match in size; only their overlapping area is copied. The copy is non-destructive, meaning the current background character leaves the existing contents of *destwin* intact.

For precise control over which region is copied, use the second form of `overlay()`. Here *sminrow* and *smincol* give the upper-left coordinates of the source window, and the remaining variables outline a rectangle within the destination window.

 window.overwrite(*destwin*[, *sminrow*, *smincol*, *dminrow*, *dmincol*, *dmaxrow*, *dmaxcol*])

Lay the window over *destwin*, overwriting it. The two windows need not match in size, in which event only their overlapping area is copied. The copy is destructive, meaning the current background character replaces the existing contents of *destwin*.

For precise control over which region is copied, use the second form of `overwrite()`. Here *sminrow* and *smincol* give the upper-left coordinates of the source window, and the remaining variables outline a rectangle within the destination window.

 window.putwin(*file*)

Write everything tied to the window into the supplied file object. That data can be recovered afterward with the `getwin()` function.

 window.redrawln(*beg*, *num*)

Flag the *num* screen lines, beginning at line *beg*, as corrupted so they get fully redrawn on the next `refresh()` call.

 window.redrawwin()

Touch the whole window so that the next `refresh()` call redraws it in full.

 window.refresh([*pminrow*, *pmincol*, *sminrow*, *smincol*, *smaxrow*, *smaxcol*])

Refresh the display right away (bringing the real screen into sync with earlier drawing/deleting methods).

The 6 optional arguments may be passed solely when the window is a pad built via `newpad()`. Those extra parameters identify which portion of the pad and the screen take part. *pminrow* and *pmincol* mark the upper left-hand corner of the rectangle to show within the pad. *sminrow*, *smincol*, *smaxrow*, and *smaxcol* mark the boundaries of the rectangle to show on the screen. The lower right-hand corner of the pad rectangle is derived from the screen coordinates, given that the two rectangles must match in size. Each rectangle must lie wholly inside its own structure. Negative values for *pminrow*, *pmincol*, *sminrow*, or *smincol* are handled as though they were zero.

 window.resize(*nlines*, *ncols*)

Reallocate the storage for a curses window so its dimensions match the values you give. When either dimension exceeds the current value, the window’s new cells are populated with blanks carrying the current background rendition (as established by `bkgdset()`) merged in.

 window.scroll([*lines=1*])

Move the screen or scrolling region upward by *lines* lines.

[Subject index](INDEX.md) · [Previous](window-getkey-to-window-instr.md) · [Continue](window-scrollok-to-window-vline.md) · [Owning module, declaration or section: curses](curses-terminal-handling-for-character-cell-displays.md) · [Owning module, declaration or section: curses.window](curses-window-class.md) · [Owning module, declaration or section: Window Objects](curses-window-class.md)
