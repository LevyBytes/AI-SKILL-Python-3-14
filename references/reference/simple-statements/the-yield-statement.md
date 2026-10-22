# 7.7. The `yield` statement

### 7.7. The `yield` statement

```text

yield_stmt: yield_expression
```

A `yield` statement carries the same semantics as a [yield expression](https://docs.python.org/3.14/reference/expressions.html#yieldexpr). The `yield` statement lets you drop the parentheses that the equivalent yield expression statement would otherwise demand. As an example, the yield statements

```python
yield <expr>
yield from <expr>

```

are the same as the yield expression statements

```python
(yield <expr>)
(yield from <expr>)

```

Yield expressions and statements come into play solely when defining a [generator](https://docs.python.org/3.14/glossary.html#term-generator) function, and solely inside the body of that generator function. Simply using `yield` somewhere in a function definition is enough to make that definition produce a generator function rather than an ordinary function.

For the complete account of `yield` semantics, see the [Yield expressions](https://docs.python.org/3.14/reference/expressions.html#yieldexpr) section.

[Subject index](INDEX.md) · [Owning language section](simple-statements.md) · [Previous source section](the-return-statement.md) · [Following source section](raise-statement.md)
