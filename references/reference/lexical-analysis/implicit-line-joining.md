# 2.1.6. Implicit line joining

### 2.1.6. Implicit line joining

Without any backslashes, expressions wrapped in parentheses, square brackets or curly braces may stretch across more than a single physical line. As an example:

```python
month_names = ['Januari', 'Februari', 'Maart',      # These are the
               'April',   'Mei',      'Juni',       # Dutch names
               'Juli',    'Augustus', 'September',  # for the months
               'Oktober', 'November', 'December']   # of the year

```

Comments may ride on implicitly continued lines. How far the continuation lines are indented makes no difference. Continuation lines that are blank are permitted. Between implicit continuation lines no NEWLINE token appears. Implicit continuation may likewise happen inside triple-quoted strings (described below); within those, comments are not allowed.

[Subject index](INDEX.md) · [Owning language section](lexical-analysis.md) · [Owning language section](line-structure.md) · [Previous source section](explicit-line-joining.md) · [Following source section](blank-lines.md)
