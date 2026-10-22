# What's New In Python 3.0 / New Syntax

### New Syntax

- [**PEP 3107**](https://peps.python.org/pep-3107/): Annotations on function arguments and return values. This supplies a uniform mechanism for annotating the parameters and return value of a function. No semantics ride along with these annotations beyond the fact that you can introspect them while running through the [`__annotations__`](https://docs.python.org/3.14/reference/datamodel.html#object.__annotations__) attribute. The goal is to spur experimentation by way of metaclasses, decorators or frameworks.

- [**PEP 3102**](https://peps.python.org/pep-3102/): Keyword-only arguments. Any named parameter that comes after `*args` in the parameter list *must* be supplied with keyword syntax at the call site. A solitary `*` in the parameter list can also signal that you accept no variable-length argument list yet do carry keyword-only arguments.

- In a class definition, keyword arguments may follow the roster of base classes. The fresh convention for naming a metaclass relies on this (see the next section), though it's usable for other ends as well, provided the metaclass goes along with it.

- [**PEP 3104**](https://peps.python.org/pep-3104/): the [`nonlocal`](https://docs.python.org/3.14/reference/simple_stmts.html#nonlocal) statement. Writing `nonlocal x` lets you assign straight to a variable sitting in an enclosing (yet non-global) scope. `nonlocal` is a freshly reserved word.

- [**PEP 3132**](https://peps.python.org/pep-3132/): Extended Iterable Unpacking. Constructs such as `a, b, *rest = some_sequence` are writable now. And even `*rest, a = stuff`. That `rest` object is forever a list (perhaps empty); the right-hand side may be whatever iterable you like. Example:

```python
(a, *rest, b) = range(5)

```

This sets *a* to `0`, *b* to `4`, and *rest* to `[1, 2, 3]`.

- Dictionary comprehensions: `{k: v for k, v in stuff}` carries the same meaning as `dict(stuff)` while offering more flexibility. (Here's [**PEP 274**](https://peps.python.org/pep-0274/) vindicated. :-)

- Set literals, such as `{1, 2}`. Mind that `{}` denotes an empty dictionary; reach for `set()` to get an empty set. Set comprehensions ship too; for example `{x for x in stuff}` carries the same meaning as `set(stuff)` while offering more flexibility.

- Fresh octal literals, such as `0o720` (present already in 2.6). The former octal literals (`0720`) are gone.

- Fresh binary literals, such as `0b1010` (present already in 2.6), accompanied by a fresh matching built-in function, [`bin()`](https://docs.python.org/3.14/library/functions.html#bin).

- A leading `b` or `B` introduces bytes literals, accompanied by a fresh matching built-in function, [`bytes()`](https://docs.python.org/3.14/library/stdtypes.html#bytes).

[Subject index](INDEX.md) · [Previous source section](overview-of-syntax-changes.md) · [Next source section](changed-syntax.md) · [Release/subject declaration](common-stumbling-blocks.md)
