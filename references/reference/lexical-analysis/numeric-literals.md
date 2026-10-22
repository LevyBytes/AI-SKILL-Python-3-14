# 2.6. Numeric literals

### 2.6. Numeric literals

Numeric literals are represented by [`NUMBER`](https://docs.python.org/3.14/library/token.html#token.NUMBER) tokens, and they fall into three categories: integers, floating-point numbers, and imaginary numbers.

```text

NUMBER: integer | floatnumber | imagnumber
```

A numeric literal's numeric value matches what you would get by handing its string form to the [`int`](https://docs.python.org/3.14/library/functions.html#int), [`float`](https://docs.python.org/3.14/library/functions.html#float) or [`complex`](https://docs.python.org/3.14/library/functions.html#complex) class constructor, in that order. Bear in mind that not every input those constructors accept is likewise a valid literal.

A sign forms no part of a numeric literal; something written as `-1` is in fact an expression built from the unary operator ‘`-`’ together with the literal `1`.

[Subject index](INDEX.md) · [Owning language section](lexical-analysis.md) · [Previous source section](formal-grammar-for-f-strings.md) · [Following source section](integer-literals.md)
