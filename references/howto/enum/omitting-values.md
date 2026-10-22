# Omitting values

### Omitting values

For plenty of use-cases, the actual value of an enumeration is irrelevant to you. This kind of simple enumeration can be defined in a few ways:

- use instances of [`auto`](https://docs.python.org/3.14/library/enum.html#enum.auto) for the value

- use instances of [`object`](https://docs.python.org/3.14/library/functions.html#object) as the value

- use a descriptive string as the value

- supply a tuple for the value plus a custom [`__new__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__new__) that swaps that tuple out for an [`int`](https://docs.python.org/3.14/library/functions.html#int) value

Adopting any of these approaches tells the reader that the values carry no significance, and additionally lets you add, drop, or rearrange members without renumbering the rest.

[Subject index](INDEX.md) · [Previous source context](enum-cookbook.md) · [Following source context](using-auto.md)
