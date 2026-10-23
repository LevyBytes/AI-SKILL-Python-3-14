# re - Regular-expression escape syntax and version conditions

The regular expression parser also accepts most of the [escape sequences](https://docs.python.org/3.14/reference/lexical_analysis.html#escape-sequences) that Python string literals understand:

```python
\a      \b      \f      \n
\N      \r      \t      \u
\U      \v      \x      \\

```

(Keep in mind that `\b` denotes a word boundary here, and stands for “backspace” only when written inside character classes.)

The `'\u'`, `'\U'`, and `'\N'` escape sequences are honored exclusively within Unicode (str) patterns. Using them in bytes patterns raises an error. Unknown escapes formed from ASCII letters are held back for later use and therefore trigger errors.

Support for octal escapes is restricted. An octal escape is assumed when the leading digit is a 0, or whenever three octal digits appear; if neither condition holds, the sequence stands for a group reference. Matching the rule for string literals, octal escapes never exceed three digits.

Changed in version 3.3: introduced the `'\u'` and `'\U'` escape sequences.

Changed in version 3.6: an unknown escape built from `'\'` plus an ASCII letter is now treated as an error.

Changed in version 3.8: introduced the `'\N{*name*}'` escape sequence. Just as in string literals, it widens into the named Unicode character (for instance `'\N{EM DASH}'`).

[Subject index](INDEX.md) · [Previous](regular-expression-syntax.md) · [Continue](module-contents.md) · [Owning module, declaration or section: re](re-regular-expression-operations.md)
