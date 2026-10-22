# curses: `window.addch()`

window.addch(*ch*[, *attr*])

 window.addch(*y*, *x*, *ch*[, *attr*])

Paint character *ch* at `(y, x)` carrying attributes *attr*, writing over whatever character had previously been painted at that spot. By default the character position and attributes take the window object's current settings.

Note

Writing past the edge of the window, subwindow, or pad raises a `curses.error`. Trying to write into the lower right corner of a window, subwindow, or pad makes an exception get raised once the character has been printed.

[Subject index](INDEX.md) · [Previous](curses-window-class.md) · [Owning module, declaration or section: curses](curses-terminal-handling-for-character-cell-displays.md) · [Owning module, declaration or section: curses.window](curses-window-class.md) · [Owning module, declaration or section: Window Objects](curses-window-class.md)
