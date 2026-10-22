# 6.10. Comparisons

### 6.10. Comparisons

Differing from C, every comparison operation in Python carries the same priority, which sits below that of any arithmetic, shifting or bitwise operation. Also differing from C, expressions such as `a < b < c` carry the interpretation that is conventional in mathematics:

```text

comparison:    or_expr (comp_operator or_expr)*
comp_operator: "<" | ">" | "==" | ">=" | "<=" | "!="
               | "is" ["not"] | ["not"] "in"
```

Comparisons produce boolean values: `True` or `False`. Custom *rich comparison methods* are free to return non-boolean values. When that happens, Python calls [`bool()`](https://docs.python.org/3.14/library/functions.html#bool) on such a value in boolean contexts.

Comparisons can be chained however you like — for instance, `x < y <= z` amounts to `x < y and y <= z`, with the difference that `y` gets evaluated just once (though in both formulations `z` goes unevaluated entirely once `x < y` turns out false).

Stated formally, take *a*, *b*, *c*, …, *y*, *z* to be expressions while *op1*, *op2*, …, *opN* stand for comparison operators; then `a op1 b op2 c ... y opN z` amounts to `a op1 b and b op2 c and ... y opN z`, with the difference that each expression gets evaluated at most once.

Be aware that `a op1 b op2 c` carries no implied comparison between *a* and *c*, so, for instance, `x < y > z` is entirely legal (even if it is perhaps not pretty).

[Subject index](INDEX.md) · [Owning language section](expressions.md) · [Previous source section](binary-bitwise-operations.md) · [Following source section](value-comparisons.md)
