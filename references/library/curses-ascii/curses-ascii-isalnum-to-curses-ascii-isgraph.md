# curses.ascii: `curses.ascii.isalnum()`, `curses.ascii.isalpha()`, `curses.ascii.isascii()`, `curses.ascii.isblank()`, `curses.ascii.iscntrl()`, `curses.ascii.isdigit()`, `curses.ascii.isgraph()`

# Curses.Ascii

### `curses.ascii` - Utilities for ASCII characters

**Source code:** [Lib/curses/ascii.py](https://github.com/python/cpython/tree/3.14/Lib/curses/ascii.py)

---

For ASCII characters, the `curses.ascii` module hands you named constants together with functions that check whether a character belongs to one ASCII class or another. Those constants name the control characters in this way:

| Name | Meaning |
| --- | --- |
| curses.ascii.NUL |  |
| curses.ascii.SOH | Start of heading, console interrupt |
| curses.ascii.STX | Start of text |
| curses.ascii.ETX | End of text |
| curses.ascii.EOT | End of transmission |
| curses.ascii.ENQ | Enquiry, goes with `ACK` flow control |
| curses.ascii.ACK | Acknowledgement |
| curses.ascii.BEL | Bell |
| curses.ascii.BS | Backspace |
| curses.ascii.TAB | Tab |
| curses.ascii.HT | Alias for `TAB`: “Horizontal tab” |
| curses.ascii.LF | Line feed |
| curses.ascii.NL | Alias for `LF`: “New line” |
| curses.ascii.VT | Vertical tab |
| curses.ascii.FF | Form feed |
| curses.ascii.CR | Carriage return |
| curses.ascii.SO | Shift-out, begin alternate character set |
| curses.ascii.SI | Shift-in, resume default character set |
| curses.ascii.DLE | Data-link escape |
| curses.ascii.DC1 | XON, for flow control |
| curses.ascii.DC2 | Device control 2, block-mode flow control |
| curses.ascii.DC3 | XOFF, for flow control |
| curses.ascii.DC4 | Device control 4 |
| curses.ascii.NAK | Negative acknowledgement |
| curses.ascii.SYN | Synchronous idle |
| curses.ascii.ETB | End transmission block |
| curses.ascii.CAN | Cancel |
| curses.ascii.EM | End of medium |
| curses.ascii.SUB | Substitute |
| curses.ascii.ESC | Escape |
| curses.ascii.FS | File separator |
| curses.ascii.GS | Group separator |
| curses.ascii.RS | Record separator, block-mode terminator |
| curses.ascii.US | Unit separator |
| curses.ascii.SP | Space |
| curses.ascii.DEL | Delete |

Keep in mind that a good many of these barely matter in present-day use. Their mnemonics trace back to teleprinter practice from before digital computers existed.

What the module offers next is this set of functions, modeled on their counterparts in the standard C library:

 curses.ascii.isalnum(*c*)

Tests whether the character is ASCII alphanumeric; this matches `isalpha(c) or isdigit(c)`.

 curses.ascii.isalpha(*c*)

Tests whether the character is ASCII alphabetic; this matches `isupper(c) or islower(c)`.

 curses.ascii.isascii(*c*)

Tests whether the value sits inside the 7-bit ASCII set.

 curses.ascii.isblank(*c*)

Tests for an ASCII whitespace character: a space or a horizontal tab.

 curses.ascii.iscntrl(*c*)

Tests for an ASCII control character (falling within 0x00 to 0x1f, or 0x7f).

 curses.ascii.isdigit(*c*)

Tests for an ASCII decimal digit running `'0'` through `'9'`. It comes to the same thing as `c in string.digits`.

 curses.ascii.isgraph(*c*)

Tests for any printable ASCII character other than space.

[Subject index](INDEX.md) · [Continue](curses-ascii-islower-to-curses-ascii-controlnames.md)
