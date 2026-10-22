# 2.1.2. Physical lines

### 2.1.2. Physical lines

A physical line consists of characters closed off by one of the end-of-line sequences below:

- the Unix form using ASCII LF (linefeed),

- the Windows convention, where the ASCII pair CR LF is used (a return character trailed by a linefeed),

- the ‘[Classic Mac OS](https://en.wikipedia.org/wiki/Classic_Mac_OS)’ form using the ASCII CR (return) character.

No matter the platform, every one of these sequences becomes a single ASCII LF (linefeed) character. (Even within string literals this happens.) A file may freely mix the sequences line by line; consistency throughout a file is not required.

The close of input likewise acts as an implicit terminator for the last physical line.

Formally:

```text

newline: <ASCII LF> | <ASCII CR> <ASCII LF> | <ASCII CR>
```

[Subject index](INDEX.md) · [Owning language section](lexical-analysis.md) · [Owning language section](line-structure.md) · [Previous source section](logical-lines.md) · [Following source section](comments.md)
