# 4.9.3. Special parameters

### 4.9.3. Special parameters

Out of the box, you can hand arguments to a Python function by their position or by naming them explicitly with a keyword. Both for clarity and for speed, it can be worthwhile to limit how arguments get supplied, so that someone only has to read the definition to tell whether each item is positional, positional-or-keyword, or keyword.

A definition might take this shape:

```none
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      -----------    ----------     ----------
        |             |                  |
        |        Positional or keyword   |
        |                                - Keyword only
         -- Positional only

```

in which `/` and `*` may be omitted. When present, those markers declare each parameter's category according to the manner in which its argument can reach the function: positional-only, positional-or-keyword, and keyword-only. Another label for keyword parameters is named parameters.

[Subject index](INDEX.md) · [Previous source section](keyword-arguments.md) · [Following source section](positional-or-keyword-arguments.md)
