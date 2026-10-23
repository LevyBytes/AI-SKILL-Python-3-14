# re - Regular Expression Syntax - Code example: >>> m = re.search(r'(?<=-)\w+', 'spam-egg')

```python
>>> m = re.search(r'(?<=-)\w+', 'spam-egg')
>>> m.group(0)
'egg'

```

Changed in version 3.5: fixed-length group references gained support.

`(?<!...)`

Matches when the current position in the string has no match for `...` directly before it. This goes by the name *negative lookbehind assertion*. As with positive lookbehind assertions, the inner pattern must match only strings of some fixed length. A pattern opening with a negative lookbehind assertion may match at the start of the string under search.

`(?(id/name)yes-pattern|no-pattern)`

Will attempt a match with `yes-pattern` when the group of the supplied *id* or *name* exists, and with `no-pattern` when it doesn't. Being optional, `no-pattern` may be left out. For instance, `(<)?(\w+@\w+(?:\.\w+)+)(?(1)>|$)` is a weak email-matching pattern, matching `'<user@host.com>'` and `'user@host.com'` alike, yet neither `'<user@host.com'` nor `'user@host.com>'`.

Changed in version 3.12: a group *id* may hold nothing but ASCII digits. Within [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) patterns, a group *name* may hold nothing but bytes drawn from the ASCII range (`b'\x00'`-`b'\x7f'`).

The special sequences are made of `'\'` plus a character drawn from the list below. Where the ordinary character is neither an ASCII digit nor an ASCII letter, the resulting RE matches that second character. For example, `\$` matches the character `'$'`.

`\number`

Matches the contents of the group bearing the same number. Numbering of groups starts at 1. For example, `(.+) \1` matches `'the the'` or `'55 55'`, but not `'thethe'` (mind the space after the group). Only one of the first 99 groups can be matched through this special sequence. Where *number* opens with the digit 0, or where *number* runs 3 octal digits long, it isn't read as a group match but as the character whose octal value is *number*. Within the `'['` and `']'` of a character class, every numeric escape is taken as a character.

`\A`

Matches solely at the string's start.

`\b`

Matches the empty string, but only at a word's beginning or end. A word here means a run of word characters. Note that formally `\b` is the boundary lying between a `\w` and a `\W` character (or the reverse), or between `\w` and the string's beginning or end. Hence `r'\bat\b'` matches `'at'`, `'at.'`, `'(at)'`, and `'as at ay'` yet neither `'attempt'` nor `'atlas'`.

In Unicode (str) patterns the default word characters are the Unicode alphanumerics plus the underscore, though the `ASCII` flag can alter this. Should the `LOCALE` flag be used, the current locale settles word boundaries.

Note

Within a character range, `\b` stands for the backspace character, to stay compatible with Python's string literals.

`\B`

Matches the empty string, but only where it is *not* at a word's beginning or end. Hence `r'at\B'` matches `'athens'`, `'atom'`, `'attorney'`, yet neither `'at'`, `'at.'`, nor `'at!'`. As the inverse of `\b`, `\B` makes word characters in Unicode (str) patterns the Unicode alphanumerics or the underscore, though the `ASCII` flag can alter this. Should the `LOCALE` flag be used, the current locale settles word boundaries.

Changed in version 3.14: `\B` now matches empty input string.

`\d`

For Unicode (str) patterns:

Matches every Unicode decimal digit: meaning whatever character sits in the Unicode character category [[Nd]](https://www.unicode.org/versions/Unicode15.0.0/ch04.pdf#G134153). Covered here are `[0-9]` along with plenty of other digit characters.

Matches `[0-9]` if the `ASCII` flag is used.

For 8-bit (bytes) patterns:

Matches any decimal digit within the ASCII character set; this comes to `[0-9]`.

`\D`

Matches any character that is not a decimal digit. This is the inverse of `\d`.

Matches `[^0-9]` if the `ASCII` flag is used.

`\s`

For Unicode (str) patterns:

Matches Unicode whitespace characters (in the sense of [`str.isspace()`](https://docs.python.org/3.14/library/stdtypes.html#str.isspace)). This takes in `[ \t\n\r\f\v]`, plus many more characters, among them the non-breaking spaces required by the typography rules of numerous languages.

Matches `[ \t\n\r\f\v]` if the `ASCII` flag is used.

For 8-bit (bytes) patterns:

Matches the characters treated as whitespace within the ASCII character set; this comes to `[ \t\n\r\f\v]`.

`\S`

Matches any character that is not a whitespace character. This is the inverse of `\s`.

Matches `[^ \t\n\r\f\v]` if the `ASCII` flag is used.

`\w`

[Subject index](INDEX.md) · [Previous](re-i-to-re-x.md) · [Continue](regular-expression-syntax-contract-for-unicode-str-patterns.md) · [Owning module, declaration or section: re](re-regular-expression-operations.md) · [Owning module, declaration or section: Regular Expression Syntax](regular-expression-syntax-overview.md)
