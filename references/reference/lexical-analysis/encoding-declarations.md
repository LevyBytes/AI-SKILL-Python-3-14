# 2.1.4. Encoding declarations

### 2.1.4. Encoding declarations

When a comment on the script's first or second line matches the regular expression `coding[=:]\s*([-\w.]+)`, that comment counts as an encoding declaration; the expression's first group gives the name of the source file's encoding. An encoding declaration has to sit on a line by itself. Should it land on the second line, then the first line is required to be a comment-only line too. The encoding expression is recommended in these forms:

```python
# -*- coding: <encoding-name> -*-

```

which GNU Emacs also recognizes, and

```python
# vim:fileencoding=<encoding-name>

```

which Bram Moolenaar’s VIM recognizes.

When no encoding declaration turns up, UTF-8 serves as the default encoding. Where a file's implicit or explicit encoding is UTF-8, a leading UTF-8 byte-order mark (`b'\xef\xbb\xbf'`) gets skipped rather than triggering a syntax error.

A declared encoding's name must be one Python recognizes (consult [Standard Encodings](https://docs.python.org/3.14/library/codecs.html#standard-encodings)). Every part of lexical analysis — string literals, comments, identifiers — uses that encoding.

The whole of lexical analysis (string literals, comments and identifiers included) operates on Unicode text that the source encoding decoded. Python source may carry any Unicode code point apart from the NUL control character.

```text

source_character:  <any Unicode code point, except NUL>
```

[Subject index](INDEX.md) · [Owning language section](lexical-analysis.md) · [Owning language section](line-structure.md) · [Previous source section](comments.md) · [Following source section](explicit-line-joining.md)
