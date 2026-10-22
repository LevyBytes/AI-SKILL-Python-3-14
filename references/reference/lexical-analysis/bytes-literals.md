# 2.5.5. Bytes literals

### 2.5.5. Bytes literals

*Bytes literals* invariably carry the ‘`b`’ or ‘`B`’ prefix; what they yield is an instance of the [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) type rather than the [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) type. Only ASCII characters are permitted inside them; any byte whose numeric value reaches 128 or beyond has to be written through escape sequences (commonly Hexadecimal character or Octal character):

```pycon
>>> b'\x89PNG\r\n\x1a\n'
b'\x89PNG\r\n\x1a\n'
>>> list(b'\x89PNG\r\n\x1a\n')
[137, 80, 78, 71, 13, 10, 26, 10]

```

In like manner, a zero byte has to be written through an escape sequence (commonly `\0` or `\x00`).

[Subject index](INDEX.md) · [Owning language section](lexical-analysis.md) · [Owning language section](string-and-bytes-literals.md) · [Previous source section](unrecognized-escape-sequences.md) · [Following source section](raw-string-literals.md)
