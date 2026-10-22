# curses — Constants — Signature and initial contract

curses.LINES

The screen height, that is, the count of lines. It exists only once `initscr()` has been called. Updated by `update_lines_cols()`, `resizeterm()` and `resize_term()`.

Several constants exist for specifying character cell attributes. Precisely which constants exist depends on the system.

| Attribute | Meaning |
| --- | --- |
| curses.A_ALTCHARSET | Alternate character set mode |
| curses.A_BLINK | Blink mode |
| curses.A_BOLD | Bold mode |
| curses.A_DIM | Dim mode |
| curses.A_INVIS | Invisible or blank mode |
| curses.A_ITALIC | Italic mode |
| curses.A_NORMAL | Normal attribute |
| curses.A_PROTECT | Protected mode |
| curses.A_REVERSE | Reverse background and foreground colors |
| curses.A_STANDOUT | Standout mode |
| curses.A_UNDERLINE | Underline mode |
| curses.A_HORIZONTAL | Horizontal highlight |
| curses.A_LEFT | Left highlight |
| curses.A_LOW | Low highlight |
| curses.A_RIGHT | Right highlight |
| curses.A_TOP | Top highlight |
| curses.A_VERTICAL | Vertical highlight |

Added in version 3.7: `A_ITALIC` was added.

Several constants exist to pull out the matching attributes that certain methods return.

| Bit-mask | Meaning |
| --- | --- |
| curses.A_ATTRIBUTES | Bit-mask to extract attributes |
| curses.A_CHARTEXT | Bit-mask to extract a character |
| curses.A_COLOR | Bit-mask to extract color-pair field information |

Keys are named by integer constants whose names begin with `KEY_`. Precisely which keycaps exist depends on the system.

[Subject index](INDEX.md) · [Previous](curses-err-to-curses-cols.md) · [Continue](constants-navigation-editing-and-function-keys.md) · [Owning module, declaration or section: curses](curses-terminal-handling-for-character-cell-displays.md) · [Owning module, declaration or section: Constants](curses-err-to-curses-cols.md)
