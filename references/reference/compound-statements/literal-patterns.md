# 8.6.4.3. Literal Patterns

#### 8.6.4.3. Literal Patterns

Most Python [literals](https://docs.python.org/3.14/reference/lexical_analysis.html#literals) have a corresponding literal pattern. Syntax:

```text

literal_pattern: signed_number
                 | signed_number "+" NUMBER
                 | signed_number "-" NUMBER
                 | strings
                 | "None"
                 | "True"
                 | "False"
signed_number:   ["-"] NUMBER
```

You will find the `strings` rule and the `NUMBER` token defined in the [standard Python grammar](https://docs.python.org/3.14/reference/grammar.html). Triple-quoted strings work here. Both raw strings and byte strings work too. By contrast, [f-strings](https://docs.python.org/3.14/reference/lexical_analysis.html#f-strings) and [t-strings](https://docs.python.org/3.14/reference/lexical_analysis.html#t-strings) are not supported.

The `signed_number '+' NUMBER` and `signed_number '-' NUMBER` shapes exist to express [complex numbers](https://docs.python.org/3.14/reference/lexical_analysis.html#imaginary); a real number is required on the left side and an imaginary number on the right. E.g. `3 + 4j`.

Put simply, `LITERAL` passes only when `<subject> == LITERAL`. The singletons `None`, `True` and `False` are instead compared with the [`is`](https://docs.python.org/3.14/reference/expressions.html#is) operator.

[Subject index](INDEX.md) · [Owning language section](compound-statements.md) · [Owning language section](the-match-statement.md) · [Owning language section](patterns.md) · [Previous source section](as-patterns.md) · [Following source section](capture-patterns.md)
