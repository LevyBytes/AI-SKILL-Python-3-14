# 6.2.3. Literals

### 6.2.3. Literals

A *literal* writes out a value as text. Numeric, string, and bytes literals are all supported by Python. Both [format strings](https://docs.python.org/3.14/reference/lexical_analysis.html#f-strings) and [template strings](https://docs.python.org/3.14/reference/lexical_analysis.html#t-strings) count as string literals.

A numeric literal is a lone [`NUMBER`](https://docs.python.org/3.14/reference/lexical_analysis.html#grammar-token-python-grammar-NUMBER) token that designates an integer, a floating-point number, or an imaginary number. For the specifics, consult the [Numeric literals](https://docs.python.org/3.14/reference/lexical_analysis.html#numbers) section of the Lexical analysis documentation.

A string or bytes literal can span more than one token. The section String literal concatenation covers this.

Keep in mind that values such as `-3` or `3+4.2j` ? negative and complex numbers ? are not literals in the syntactic sense; rather they are unary or binary arithmetic operations built around the `-` or `+` operator.

Evaluating a literal produces an object of the corresponding type ([`int`](https://docs.python.org/3.14/library/functions.html#int), [`float`](https://docs.python.org/3.14/library/functions.html#float), [`complex`](https://docs.python.org/3.14/library/functions.html#complex), [`str`](https://docs.python.org/3.14/library/stdtypes.html#str), [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes), or [`Template`](https://docs.python.org/3.14/library/string.templatelib.html#string.templatelib.Template)) holding the stated value. For floating-point and imaginary literals, that value may only be approximate.

Stated as formal grammar, literals are:

```text

literal: strings | NUMBER
```

[Subject index](INDEX.md) · [Owning language section](expressions.md) · [Owning language section](atoms.md) · [Previous source section](private-name-mangling.md) · [Following source section](literals-and-object-identity.md)
