# Compilation flags

### Compilation flags

Compilation flags let you adjust certain facets of how regular expressions behave. Within the [`re`](https://docs.python.org/3.14/library/re.html#module-re) module each flag comes under two names, a long one like [`IGNORECASE`](https://docs.python.org/3.14/library/re.html#re.IGNORECASE) plus a terse single-letter one like [`I`](https://docs.python.org/3.14/library/re.html#re.I). (Should you know Perl’s pattern modifiers, the single-letter forms reuse the same letters; for instance the short form of [`re.VERBOSE`](https://docs.python.org/3.14/library/re.html#re.VERBOSE) is [`re.X`](https://docs.python.org/3.14/library/re.html#re.X).) You can hand over several flags at once by OR-ing them bitwise; `re.I | re.M`, for instance, switches on both the `I` and [`M`](https://docs.python.org/3.14/library/re.html#re.M) flags.

What follows is a table listing the flags on offer, after which each one gets a fuller writeup.

| Flag | Meaning |
| --- | --- |
| `ASCII`, `A` | Restricts a number of escapes such as `\w`, `\b`, `\s` and `\d` so they match solely ASCII characters carrying the relevant property. |
| `DOTALL`, `S` | Make `.` match any character, including newlines. |
| `IGNORECASE`, `I` | Do case-insensitive matches. |
| `LOCALE`, `L` | Do a locale-aware match. |
| `MULTILINE`, `M` | Multi-line matching, affecting `^` and `$`. |
| `VERBOSE`, `X` (for ‘extended’) | Enable verbose REs, which can be organized more cleanly and understandably. |

 re.I

 re.IGNORECASE

Run matching that ignores case; both character classes and literal strings will then match letters regardless of their case. So `[A-Z]` picks up lowercase letters too. Full Unicode matching also applies, except when the [`ASCII`](https://docs.python.org/3.14/library/re.html#re.ASCII) flag turns off matches outside ASCII. Should the Unicode patterns `[a-z]` or `[A-Z]` accompany the [`IGNORECASE`](https://docs.python.org/3.14/library/re.html#re.IGNORECASE) flag, they match the 52 ASCII letters plus 4 letters lying outside ASCII, namely ‘İ’ at code point U+0130, the Latin capital letter I with dot above; ‘ı’ at U+0131, the Latin small letter dotless i; ‘ſ’ at U+017F, the Latin small letter long s; and ‘K’ at U+212A, the Kelvin sign. Here `Spam` matches `'Spam'`, `'spam'`, `'spAM'`, or `'ſpam'` (that last one only under Unicode mode). The lowercasing ignores whatever locale is current; it stops doing so once you also turn on the [`LOCALE`](https://docs.python.org/3.14/library/re.html#re.LOCALE) flag.

[Subject index](INDEX.md) · [Following source continuation](re-l-re-locale-aliases-and-locale-matching-caveats.md) · [re.L / re.LOCALE aliases and locale matching caveats](re-l-re-locale-aliases-and-locale-matching-caveats.md) · [Previous source context](module-level-functions.md) · [Following source context](re-l-re-locale-aliases-and-locale-matching-caveats.md)
