# 2.3.3. Reserved classes of identifiers

### 2.3.3. Reserved classes of identifiers

A few classes of identifiers (apart from keywords) carry special meanings. The patterns of leading and trailing underscore characters mark out these classes:

`_*`

Not imported by `from module import *`.

`_`

Within a `case` pattern in a [`match`](https://docs.python.org/3.14/reference/compound_stmts.html#match) statement, `_` is a soft keyword standing for a [wildcard](https://docs.python.org/3.14/reference/compound_stmts.html#wildcard-patterns).

Apart from that, the interactive interpreter exposes the most recent evaluation's result through the variable `_`. (That value resides in the [`builtins`](https://docs.python.org/3.14/library/builtins.html#module-builtins) module, next to built-in functions such as `print`.)

In every other setting, `_` is just a normal identifier. It frequently labels “special” items, though Python itself attaches no special meaning to it.

Note

Frequently the name `_` appears together with internationalization; for more on this convention, consult the documentation of the [`gettext`](https://docs.python.org/3.14/library/gettext.html#module-gettext) module.

It also sees common use for variables that go unused.

`__*__`

System-defined names, casually called “dunder” names. The interpreter together with its implementation (the standard library included) defines these names. The present system names get covered in the [Special method names](https://docs.python.org/3.14/reference/datamodel.html#specialnames) section as well as elsewhere. Future Python versions will probably define more. *Any* use of `__*__` names — in any context — straying from explicitly documented use risks breaking without warning.

`__*`

Class-private names. When names of this kind appear inside a class definition, they are rewritten into a mangled form that helps prevent name clashes between the “private” attributes of base and derived classes. Consult section [Identifiers (Names)](https://docs.python.org/3.14/reference/expressions.html#atom-identifiers).

[Subject index](INDEX.md) · [Owning language section](lexical-analysis.md) · [Owning language section](names.md) · [Previous source section](soft-keywords.md) · [Following source section](non-ascii-characters-in-names.md)
