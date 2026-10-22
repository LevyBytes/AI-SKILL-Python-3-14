# 6.16. Evaluation order

### 6.16. Evaluation order

Expressions are evaluated by Python in left-to-right order. Observe that during an assignment, the right-hand side gets evaluated before the left-hand side does.

Throughout the lines below, the expressions are evaluated following the arithmetic order of their suffixes:

```python
expr1, expr2, expr3, expr4
(expr1, expr2, expr3, expr4)
{expr1: expr2, expr3: expr4}
expr1 + expr2 * (expr3 - expr4)
expr1(expr2, expr3, *expr4, **expr5)
expr3, expr4 = expr1, expr2

```

[Subject index](INDEX.md) · [Owning language section](expressions.md) · [Previous source section](expression-lists.md) · [Following source section](operator-precedence.md)
