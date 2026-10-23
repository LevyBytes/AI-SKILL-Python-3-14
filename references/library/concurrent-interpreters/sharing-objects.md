# concurrent.interpreters - “Sharing” Objects

### “Sharing” Objects

Whatever data genuinely gets shared across interpreters forfeits the thread-safety the [GIL](https://docs.python.org/3.14/glossary.html#term-GIL) would otherwise grant. Extension modules have several ways to cope with that. From Python code, however, the missing thread-safety means objects can’t truly be shared, save for a handful of exceptions. A copy has to be made instead, so mutable objects drift out of sync.

When an object travels to another interpreter, by default it’s copied through [`pickle`](https://docs.python.org/3.14/library/pickle.html#module-pickle). Almost every immutable builtin object is either shared outright or copied cheaply. To illustrate:

- [`None`](https://docs.python.org/3.14/library/constants.html#None)

- [`bool`](https://docs.python.org/3.14/library/functions.html#bool) ([`True`](https://docs.python.org/3.14/library/constants.html#True) and [`False`](https://docs.python.org/3.14/library/constants.html#False))

- [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes)

- [`str`](https://docs.python.org/3.14/library/stdtypes.html#str)

- [`int`](https://docs.python.org/3.14/library/functions.html#int)

- [`float`](https://docs.python.org/3.14/library/functions.html#float)

- [`tuple`](https://docs.python.org/3.14/library/stdtypes.html#tuple) (of similarly supported objects)

A handful of Python types do, in fact, share mutable data across interpreters:

- [`memoryview`](https://docs.python.org/3.14/library/stdtypes.html#memoryview)

- `Queue`

[Subject index](INDEX.md) · [Previous](communication-between-interpreters.md) · [Continue](interpreter-discovery-and-queue-creation.md) · [Owning module, declaration or section: concurrent.interpreters](multiple-interpreters-overview.md)
