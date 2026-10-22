# 6.2. Atoms

### 6.2. Atoms

The building blocks at the lowest level of an expression are atoms. At their simplest, atoms are either [names](https://docs.python.org/3.14/reference/lexical_analysis.html#identifiers) or literals. Anything wrapped in parentheses, brackets, or braces also counts syntactically as an atom.

The atom syntax, stated formally, is:

```text

atom:
   | 'True'
   | 'False'
   | 'None'
   | '...'
   | identifier
   | literal
   | enclosure
enclosure:
   | parenth_form
   | list_display
   | dict_display
   | set_display
   | generator_expression
   | yield_atom
```

[Subject index](INDEX.md) · [Owning language section](expressions.md) · [Previous source section](arithmetic-conversions.md) · [Following source section](built-in-constants.md)
