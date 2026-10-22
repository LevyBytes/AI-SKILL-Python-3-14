# curses.ascii: ASCII classification, control conversions and names

curses.ascii.islower(*c*)

Tests for an ASCII lower-case character.

 curses.ascii.isprint(*c*)

Tests for any printable ASCII character, space included.

 curses.ascii.ispunct(*c*)

Tests for a printable ASCII character that is neither a space nor alphanumeric.

 curses.ascii.isspace(*c*)

Tests for an ASCII white-space character: space, line feed, carriage return, form feed, horizontal tab, or vertical tab.

 curses.ascii.isupper(*c*)

Tests for an ASCII uppercase letter.

 curses.ascii.isxdigit(*c*)

Tests for an ASCII hexadecimal digit. It amounts to `c in string.hexdigits`.

 curses.ascii.isctrl(*c*)

Tests for an ASCII control character (ordinal values 0 to 31).

 curses.ascii.ismeta(*c*)

Tests for a non-ASCII character (ordinal values 0x80 and above).

You may feed these functions an integer or a one-character string; a string argument gets run through the built-in [`ord()`](https://docs.python.org/3.14/library/functions.html#ord) function first.

Bear in mind that every one of these functions works off the ordinal bit values pulled from the character you supply; none of them has any awareness of the character encoding on the host machine.

The next pair of functions accept either a one-character string or an integer byte value, and they give back a result of whichever type came in.

 curses.ascii.ascii(*c*)

Give back the ASCII value that the low 7 bits of *c* map to.

 curses.ascii.ctrl(*c*)

Give back the control character that the supplied character maps to (its bit value gets bitwise-anded with 0x1f).

 curses.ascii.alt(*c*)

Give back the 8-bit character that the supplied ASCII character maps to (its bit value gets bitwise-ored with 0x80).

This next function accepts either a one-character string or an integer value, and it gives back a string.

 curses.ascii.unctrl(*c*)

Give back a string form of the ASCII character *c*. Where *c* prints, that string is just the character on its own. Where it is a control character (0x00–0x1f), the string holds a caret (`'^'`) trailed by the matching uppercase letter. Where it is the ASCII delete (0x7f), the string comes out as `'^?'`. And where its meta bit (0x80) is set, that bit is dropped, the rules above kick in, and a `'!'` is tacked onto the front of the result.

 curses.ascii.controlnames

A string array of 33 elements holding, in sequence, the ASCII mnemonics for the thirty-two ASCII control characters spanning 0 (NUL) up to 0x1f (US), and rounding it out, the `SP` mnemonic standing for the space character.

[Subject index](INDEX.md) · [Previous](curses-ascii-isalnum-to-curses-ascii-isgraph.md) · [Owning module, declaration or section: curses.ascii](curses-ascii-isalnum-to-curses-ascii-isgraph.md)
