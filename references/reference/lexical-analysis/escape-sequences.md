# 2.5.4. Escape sequences

### 2.5.4. Escape sequences

Where no ‘`r`’ or ‘`R`’ prefix is present, escape sequences within string and bytes literals get interpreted by rules close to those of Standard C. Here are the recognized escape sequences:

| Escape Sequence | Meaning |
| --- | --- |
| `\`&lt;newline&gt; | Ignored end of line |
| `\\` | Backslash |
| `\'` | Single quote |
| `\"` | Double quote |
| `\a` | ASCII Bell (BEL) |
| `\b` | ASCII Backspace (BS) |
| `\f` | ASCII Formfeed (FF) |
| `\n` | ASCII Linefeed (LF) |
| `\r` | ASCII Carriage Return (CR) |
| `\t` | ASCII Horizontal Tab (TAB) |
| `\v` | ASCII Vertical Tab (VT) |
| `\*ooo*` | Octal character |
| `\x*hh*` | Hexadecimal character |
| `\N{*name*}` | Named Unicode character |
| `\u*xxxx*` | Hexadecimal Unicode character |
| `\U*xxxxxxxx*` | Hexadecimal Unicode character |

[Subject index](INDEX.md) · [Owning language section](lexical-analysis.md) · [Owning language section](string-and-bytes-literals.md) · [Previous source section](formal-grammar.md) · [Following source section](ignored-end-of-line.md)
