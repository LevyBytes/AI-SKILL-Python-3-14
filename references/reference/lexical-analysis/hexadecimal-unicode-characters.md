# 2.5.4.6. Hexadecimal Unicode characters

#### 2.5.4.6. Hexadecimal Unicode characters

The pair of sequences `\u*xxxx*` and `\U*xxxxxxxx*` each stand for the Unicode character holding the supplied hex (base 16) value. For `\u`, precisely four digits are needed; for `\U`, precisely eight digits are needed. Any Unicode character at all can be encoded by the latter.

```pycon
>>> '\u1234'
'ሴ'
>>> '\U0001f40d'
'🐍'

```

Bytes literals are not allowed to contain these sequences.

[Subject index](INDEX.md) · [Owning language section](lexical-analysis.md) · [Owning language section](string-and-bytes-literals.md) · [Owning language section](escape-sequences.md) · [Previous source section](named-unicode-character.md) · [Following source section](unrecognized-escape-sequences.md)
