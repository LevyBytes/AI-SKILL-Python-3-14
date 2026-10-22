# 2.1.5. Explicit line joining

### 2.1.5. Explicit line joining

Backslash characters (`\`) let you fold two or more physical lines together into logical lines this way: where a physical line finishes with a backslash that belongs to neither a string literal nor a comment, that line merges with the next into one logical line, dropping the backslash plus the end-of-line character that trails it. As an example:

```python
if 1900 < year < 2100 and 1 <= month <= 12 \
   and 1 <= day <= 31 and 0 <= hour < 24 \
   and 0 <= minute < 60 and 0 <= second < 60:   # Looks like a valid date
        return 1

```

No comment may sit on a line that ends with a backslash. Comments are not continued by a backslash. Apart from string literals, a backslash continues no token (that is, except for string literals, tokens may not be broken across physical lines with a backslash). Outside a string literal, a backslash anywhere else on a line is illegal.

[Subject index](INDEX.md) · [Owning language section](lexical-analysis.md) · [Owning language section](line-structure.md) · [Previous source section](encoding-declarations.md) · [Following source section](implicit-line-joining.md)
