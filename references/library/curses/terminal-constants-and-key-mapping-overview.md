# curses — curses constants, key capabilities and terminal mappings — Section introduction and initial examples

VT100 terminals and the software emulations of them, X terminal emulators included, usually offer a minimum of four function keys (`KEY_F1`, `KEY_F2`, `KEY_F3`, `KEY_F4`), with the arrow keys tied to `KEY_UP`, `KEY_DOWN`, `KEY_LEFT` and `KEY_RIGHT` just as you would guess. Should your machine sport a PC keyboard, you can count on arrow keys plus twelve function keys (though some older PC keyboards top out at ten); on top of that, these keypad mappings hold as standard:

| Keycap | Constant |
| --- | --- |
| Insert | KEY_IC |
| Delete | KEY_DC |
| Home | KEY_HOME |
| End | KEY_END |
| Page Up | KEY_PPAGE |
| Page Down | KEY_NPAGE |

Below is a table of characters drawn from the alternate character set. Carried over from the VT100 terminal, they tend to be on hand across software emulations like X terminals. Where no graphic exists, curses settles for a rough printable ASCII stand-in.

Note

You can only reach these once `initscr()` has been called.

| ACS code | Meaning |
| --- | --- |
| curses.ACS_BBSS | another label for the upper right corner |
| curses.ACS_BLOCK | filled square block |
| curses.ACS_BOARD | grid of squares |
| curses.ACS_BSBS | another label for the horizontal line |
| curses.ACS_BSSB | another label for the upper left corner |
| curses.ACS_BSSS | another label for the top tee |
| curses.ACS_BTEE | tee at the bottom |
| curses.ACS_BULLET | bullet mark |
| curses.ACS_CKBOARD | stippled checkerboard |
| curses.ACS_DARROW | downward-pointing arrow |
| curses.ACS_DEGREE | the degree sign |
| curses.ACS_DIAMOND | diamond shape |
| curses.ACS_GEQUAL | greater-than-or-equal sign |
| curses.ACS_HLINE | line drawn horizontally |
| curses.ACS_LANTERN | the lantern glyph |
| curses.ACS_LARROW | arrow pointing left |
| curses.ACS_LEQUAL | less-than-or-equal sign |
| curses.ACS_LLCORNER | bottom-left corner |
| curses.ACS_LRCORNER | bottom-right corner |
| curses.ACS_LTEE | tee on the left |
| curses.ACS_NEQUAL | the not-equal sign |
| curses.ACS_PI | the pi character |
| curses.ACS_PLMINUS | the plus-or-minus sign |
| curses.ACS_PLUS | large plus sign |
| curses.ACS_RARROW | arrow pointing right |
| curses.ACS_RTEE | tee on the right |
| curses.ACS_S1 | scanline 1 |
| curses.ACS_S3 | scanline 3 |
| curses.ACS_S7 | scanline 7 |
| curses.ACS_S9 | scanline 9 |
| curses.ACS_SBBS | another label for the lower right corner |
| curses.ACS_SBSB | another label for the vertical line |
| curses.ACS_SBSS | another label for the right tee |
| curses.ACS_SSBB | another label for the lower left corner |
| curses.ACS_SSBS | another label for the bottom tee |
| curses.ACS_SSSB | another label for the left tee |
| curses.ACS_SSSS | another label for the crossover or large plus |
| curses.ACS_STERLING | the pound sterling sign |
| curses.ACS_TTEE | tee at the top |
| curses.ACS_UARROW | upward-pointing arrow |
| curses.ACS_ULCORNER | top-left corner |
| curses.ACS_URCORNER | top-right corner |
| curses.ACS_VLINE | line drawn vertically |

The table that follows enumerates the mouse button constants that `getmouse()` works with:

| Mouse button constant | Meaning |
| --- | --- |
| curses.BUTTONn_PRESSED | press of mouse button *n* |
| curses.BUTTONn_RELEASED | release of mouse button *n* |
| curses.BUTTONn_CLICKED | click of mouse button *n* |
| curses.BUTTONn_DOUBLE_CLICKED | double-click of mouse button *n* |
| curses.BUTTONn_TRIPLE_CLICKED | triple-click of mouse button *n* |
| curses.BUTTON_SHIFT | Shift held while the button state changed |
| curses.BUTTON_CTRL | Control held while the button state changed |
| curses.BUTTON_ALT | Control held while the button state changed |

Changed in version 3.10: Provided the underlying curses library supplies them, the `BUTTON5_*` constants are now made available.

This next table runs through the colors defined ahead of time:

[Subject index](INDEX.md) · [Continue](terminal-color-constants-table.md) · [Owning module, declaration or section: curses](curses-terminal-handling-for-character-cell-displays.md) · [Owning module, declaration or section: curses constants, key capabilities and terminal mappings](curses-err-to-curses-cols.md) · [Preceding source contract and version conditions](constants-shifted-and-terminal-event-keys.md)
