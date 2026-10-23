# Boolean Operations`and`, `or`, `not`

### Boolean Operations`and`, `or`, `not`

Here are the Boolean operations, listed from lowest to highest priority:

| Operation | Result | Notes |
| --- | --- | --- |
| `x or y` | if *x* is true, then *x*, else *y* | (1) |
| `x and y` | if *x* is false, then *x*, else *y* | (2) |
| `not x` | if *x* is false, then `True`, else `False` | (3) |

Notes:

1.

Being a short-circuit operator, it evaluates its second argument only when the first one is false.

2.

Being a short-circuit operator, it evaluates its second argument only when the first one is true.

3.

Because `not` ranks below the non-Boolean operators in priority, `not a == b` parses as `not (a == b)`, whereas `a == not b` is a syntax error.

[Subject index](INDEX.md) · [Previous](truth-value-testing.md) · [Continue](comparisons.md)
