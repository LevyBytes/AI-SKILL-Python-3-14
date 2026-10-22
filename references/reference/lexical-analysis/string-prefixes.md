# 2.5.2. String prefixes

### 2.5.2. String prefixes

An optional *prefix* may attach to string literals, shaping how the literal's content gets parsed, as an example:

```python
b"data"
f'{result=}'

```

These are the prefixes that are allowed:

- `b`: Bytes literal

- `r`: Raw string

- `f`: Formatted string literal (“f-string”)

- `t`: Template string literal (“t-string”)

- `u`: No effect (allowed for backwards compatibility)

For details on each type, see the linked sections.

The prefixes ignore case (for instance, ‘`B`’ behaves the same as ‘`b`’). Joining the ‘`r`’ prefix with ‘`f`’, ‘`t`’ or ‘`b`’ is allowed, and so ‘`fr`’, ‘`rf`’, ‘`tr`’, ‘`rt`’, ‘`br`’, and ‘`rb`’ count as valid prefixes too.

Added in version 3.3: For raw bytes literals, the `'rb'` prefix arrived as an equivalent alternative to `'br'`.

The unicode legacy literal (`u'value'`) regained support to make keeping dual Python 2.x and 3.x codebases easier to maintain. For more information see [**PEP 414**](https://peps.python.org/pep-0414/).

[Subject index](INDEX.md) · [Owning language section](lexical-analysis.md) · [Owning language section](string-and-bytes-literals.md) · [Previous source section](triple-quoted-strings.md) · [Following source section](formal-grammar.md)
