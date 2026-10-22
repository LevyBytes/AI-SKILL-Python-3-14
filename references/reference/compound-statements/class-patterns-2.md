# compound statements: Class-pattern positional arguments and match_args

[Customizing positional arguments in class pattern matching](https://docs.python.org/3.14/reference/datamodel.html#class-pattern-matching)

  2.

After every positional pattern has been turned into a keyword pattern, matching continues as though only keyword patterns had been given.

Positional subpatterns are handled differently for the following built-in types:

  - [`bool`](https://docs.python.org/3.14/library/functions.html#bool)

  - [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray)

  - [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes)

  - [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict)

  - [`float`](https://docs.python.org/3.14/library/functions.html#float)

  - [`frozenset`](https://docs.python.org/3.14/library/stdtypes.html#frozenset)

  - [`int`](https://docs.python.org/3.14/library/functions.html#int)

  - [`list`](https://docs.python.org/3.14/library/stdtypes.html#list)

  - [`set`](https://docs.python.org/3.14/library/stdtypes.html#set)

  - [`str`](https://docs.python.org/3.14/library/stdtypes.html#str)

  - [`tuple`](https://docs.python.org/3.14/library/stdtypes.html#tuple)

A single positional argument is accepted by these classes, and its pattern matches the whole object rather than one attribute. For instance `int(0|1)` matches the value `0`, yet not the value `0.0`.

Put simply, `CLS(P1, attr=P2)` matches only when the following hold:

- `isinstance(<subject>, CLS)`

- convert `P1` to a keyword pattern using `CLS.__match_args__`

- For each keyword argument `attr=P2`:

  - `hasattr(<subject>, "attr")`

  - `P2` matches `<subject>.attr`

- ? and so on across each corresponding keyword argument/pattern pair.

See also

-

[**PEP 634**](https://peps.python.org/pep-0634/) - Structural Pattern Matching: Specification

- [**PEP 636**](https://peps.python.org/pep-0636/) - Structural Pattern Matching: Tutorial

[Subject index](INDEX.md) · [Owning language section](compound-statements.md) · [Owning language section](the-match-statement.md) · [Owning language section](patterns.md) · [Owning language section](class-pattern-matching.md) · [Contract or procedure setup](class-pattern-matching.md) · [Previous source section](class-pattern-matching.md) · [Following source section](function-definitions-func-and-func.md)
