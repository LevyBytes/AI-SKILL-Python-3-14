# 2.7. Operators and delimiters

### 2.7. Operators and delimiters

*Operator* and *delimiter* tokens — that is, the generic [`OP`](https://docs.python.org/3.14/library/token.html#token.OP) token type — are defined by the grammar that follows. The `token` module documentation additionally provides a [list of these tokens and their names](https://docs.python.org/3.14/library/token.html#token-operators-delimiters).

```text

OP:
   | assignment_operator
   | bitwise_operator
   | comparison_operator
   | enclosing_delimiter
   | other_delimiter
   | arithmetic_operator
   | "..."
   | other_op

assignment_operator:   "+=" | "-=" | "*=" | "**=" | "/="  | "//=" | "%=" |
                       "&=" | "|=" | "^=" | "<<=" | ">>=" | "@="  | ":="
bitwise_operator:      "&"  | "|"  | "^"  | "~"   | "<<"  | ">>"
comparison_operator:   "<=" | ">=" | "<"  | ">"   | "=="  | "!="
enclosing_delimiter:   "("  | ")"  | "["  | "]"   | "{"   | "}"
other_delimiter:       ","  | ":"  | "!"  | ";"   | "="   | "->"
arithmetic_operator:   "+"  | "-"  | "**" | "*"   | "//"  | "/"   | "%"
other_op:              "."  | "@"
```

Note

In general, *operators* combine [expressions](https://docs.python.org/3.14/reference/expressions.html#expressions) together, whereas *delimiters* fulfill different roles. Even so, no sharp, formal boundary divides the two groups.

A handful of tokens act as operators in one place and delimiters in another, according to how they are used. As an example, `*` is at once the multiplication operator and a delimiter applied to sequence unpacking, and `@` is at once the matrix multiplication and a delimiter that brings in decorators.

With certain tokens the line is blurry. As an example, some treat `.`, `(`, and `)` as delimiters, whereas others regard them as the [`getattr()`](https://docs.python.org/3.14/library/functions.html#getattr) operator and the function call operator(s).

A number of Python's operators — `and`, `or`, and `not in` among them — are built from keyword tokens in place of “symbols” (operator tokens).

A run of three periods in a row (`...`) carries a special significance as an [`Ellipsis`](https://docs.python.org/3.14/library/constants.html#Ellipsis) literal.

[Subject index](INDEX.md) · [Owning language section](lexical-analysis.md) · [Previous source section](imaginary-literals.md)
