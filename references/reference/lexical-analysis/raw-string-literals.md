# 2.5.6. Raw string literals

### 2.5.6. Raw string literals

String and bytes literals alike may carry an optional ‘`r`’ or ‘`R`’ prefix; constructs of this kind are termed *raw string literals* and *raw bytes literals* respectively, and they handle backslashes as plain characters. Consequently, escape sequences inside raw string literals receive no special handling:

```pycon
>>> r'\d{4}-\d{2}-\d{2}'
'\\d{4}-\\d{2}-\\d{2}'

```

Quotes may still be escaped with a backslash even within a raw literal, yet the backslash persists in the result; as an illustration, `r"\""` is a legitimate string literal made of two characters — a backslash plus a double quote — whereas `r"\"` is not legitimate (not even a raw string is permitted to finish with an odd count of backslashes). Put precisely, *a raw literal cannot end in a single backslash* (because that backslash would escape the quote character coming after it). Observe too that a lone backslash trailed by a newline is read as those two characters belonging to the literal, *not* as a continuation of the line.

[Subject index](INDEX.md) · [Owning language section](lexical-analysis.md) · [Owning language section](string-and-bytes-literals.md) · [Previous source section](bytes-literals.md) · [Following source section](f-strings-a-to-c.md)
