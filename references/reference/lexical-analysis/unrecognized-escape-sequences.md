# 2.5.4.7. Unrecognized escape sequences

#### 2.5.4.7. Unrecognized escape sequences

In contrast with Standard C, every unrecognized escape sequence stays in the string as-is, meaning *the backslash is left in the result*:

```python
>>> print('\q')
\q
>>> list('\q')
['\\', 'q']

```

Keep in mind that, for bytes literals, those escape sequences recognized solely in string literals (`\N...`, `\u...`, `\U...`) count as unrecognized escapes themselves.

Changed in version 3.6: Any escape sequence that goes unrecognized now triggers a [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning).

Changed in version 3.12: Any escape sequence that goes unrecognized now triggers a [`SyntaxWarning`](https://docs.python.org/3.14/library/exceptions.html#SyntaxWarning). A later release of Python will instead make such sequences raise a [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError).

[Subject index](INDEX.md) · [Owning language section](lexical-analysis.md) · [Owning language section](string-and-bytes-literals.md) · [Owning language section](escape-sequences.md) · [Previous source section](hexadecimal-unicode-characters.md) · [Following source section](bytes-literals.md)
