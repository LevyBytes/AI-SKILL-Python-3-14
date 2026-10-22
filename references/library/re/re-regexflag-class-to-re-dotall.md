# re: `re.RegexFlag`, `re.A`, `re.ASCII`, `re.DEBUG`, `re.I`, `re.IGNORECASE`, `re.L`, `re.LOCALE`, `re.M`, `re.MULTILINE`, `re.NOFLAG`, `re.S`, `re.DOTALL`

### Flags

Changed in version 3.6: each flag constant is now an instance of `RegexFlag`, a subclass derived from [`enum.IntFlag`](https://docs.python.org/3.14/library/enum.html#enum.IntFlag).

 *class *re.RegexFlag

An [`enum.IntFlag`](https://docs.python.org/3.14/library/enum.html#enum.IntFlag) class that holds the regex options enumerated below.

Added in version 3.11: - added to `__all__`

 re.A

 re.ASCII

Force `\w`, `\W`, `\b`, `\B`, `\d`, `\D`, `\s` and `\S` to do ASCII-only matching rather than full Unicode matching. The flag carries weight only for Unicode (str) patterns and has no effect on bytes patterns.

Corresponds to the inline flag `(?a)`.

Note

Although the `U` flag remains for backward compatibility, it serves no purpose in Python 3 because `str` patterns match as Unicode by default, while bytes patterns disallow Unicode matching. The same redundancy applies to `UNICODE` and to the inline flag `(?u)`.

 re.DEBUG

Display debug information about compiled expression.

No corresponding inline flag.

 re.I

 re.IGNORECASE

Run matching without regard to case; for instance, `[A-Z]` will also catch lowercase letters. Full Unicode matching (for example, `Ü` lining up with `ü`) applies too, except when the `ASCII` flag turns off non-ASCII matches. This flag's behavior is unaffected by the active locale unless `LOCALE` is also supplied.

Corresponds to the inline flag `(?i)`.

Bear in mind that pairing the Unicode patterns `[a-z]` or `[A-Z]` with the `IGNORECASE` flag causes them to match the 52 ASCII letters along with these 4 added characters outside ASCII: the glyph ‘İ’ (U+0130, Latin capital letter I with dot above); next, ‘ı’ (U+0131, Latin small letter dotless i); also ‘ſ’ (U+017F, Latin small letter long s); and finally ‘K’ (U+212A, Kelvin sign). When the `ASCII` flag is supplied, the match narrows to the letters ‘a’ through ‘z’ and ‘A’ through ‘Z’ only.

 re.L

 re.LOCALE

Tie `\w`, `\W`, `\b`, `\B` and case-insensitive matching to the active locale. Only bytes patterns may use this flag.

Corresponds to the inline flag `(?L)`.

Warning

Steer clear of this flag and reach for Unicode matching instead. The locale machinery is highly unreliable, because it copes with a single “culture” at a time and functions only with 8-bit locales. Unicode matching, on by default for Unicode (str) patterns, can deal with varied locales and languages.

Changed in version 3.6: `LOCALE` works solely with bytes patterns and cannot be combined with `ASCII`.

Changed in version 3.7: a compiled regular expression object carrying the `LOCALE` flag is no longer tied to the locale present at compile time. The matching outcome is governed purely by the locale in force during matching.

 re.M

 re.MULTILINE

Once set, the pattern character `'^'` matches both at the string's start and at the start of every line (right after each newline); likewise `'$'` matches at the string's end and at every line's end (right before each newline). Otherwise, `'^'` matches at the string's start alone, while `'$'` matches only at the string's end and just ahead of the trailing newline (if there is one) at the string's end.

Corresponds to the inline flag `(?m)`.

 re.NOFLAG

Signals that no flag applies; its value is `0`. You can hand this flag to a function keyword argument as its default, or treat it as a starting value to be ORed conditionally with additional flags. Here is an example of it serving as a default value:

```python
def myfunc(text, flag=re.NOFLAG):
    return re.match(text, flag)

```

Added in version 3.11.

 re.S

 re.DOTALL

Let the `'.'` special character match absolutely any character, the newline included; with the flag absent, `'.'` matches everything *except* a newline.

Corresponds to the inline flag `(?s)`.

[Subject index](INDEX.md) · [Previous](module-contents.md) · [Continue](re-u-to-re-verbose.md) · [Owning module, declaration or section: re](re-regular-expression-operations.md)
