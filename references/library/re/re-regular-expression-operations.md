# re`re` - Regular expression operations

### `re` - Regular expression operations

**Source code:** [Lib/re/](https://github.com/python/cpython/tree/3.14/Lib/re/)

---

The matching operations for regular expressions offered by this module resemble those available in Perl.

The patterns, and the strings they search through, may be either Unicode strings ([`str`](https://docs.python.org/3.14/library/stdtypes.html#str)) or 8-bit strings ([`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes)). That said, Unicode strings and 8-bit strings cannot be combined: a bytes pattern won't match a Unicode string and the reverse fails too; in the same way, for a substitution the replacement text has to share the type of both the pattern and the string being searched.

To mark special forms, or to let special characters appear without their special meaning being triggered, regular expressions rely on the backslash character (`'\'`). Because Python employs that very character for the identical role inside string literals, a conflict arises; for instance, matching one literal backslash may require writing the pattern string as `'\\\\'`, since the regular expression itself has to be `\\`, and within an ordinary Python string literal every backslash has to be written `\\`. Be aware too that invalid escape sequences within Python's backslash handling in string literals will now emit a [`SyntaxWarning`](https://docs.python.org/3.14/library/exceptions.html#SyntaxWarning), and later releases will promote that to a [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError). That holds true even where the sequence is legitimate as a regular expression escape.

What fixes this is Python's raw string notation for the pattern text; inside a string literal carrying the `'r'` prefix, backslashes receive no special treatment at all. Hence `r"\n"` is a string of two characters, `'\'` together with `'n'`, whereas `"\n"` is a single-character string holding a newline. Most often you'll write patterns in Python using this raw string notation.

Note that the great majority of regular expression operations come both as module-level functions and as methods on compiled regular expressions. Acting as shortcuts, the functions spare you from first compiling a regex object, though they lack a few of the fine-tuning parameters.

See also

The third-party [regex](https://pypi.org/project/regex/) module, whose API matches that of the standard library `re` module, while adding extra capabilities and richer Unicode support.

[Subject index](INDEX.md) · [Continue](regular-expression-syntax-overview.md)
