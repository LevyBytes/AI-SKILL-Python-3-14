# pprint: `pprint.saferepr()`

`pprint.saferepr(*object*)`

Hands back a string representation of *object* that is guarded against recursion in a few common data structures — namely instances of [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict), [`list`](https://docs.python.org/3.14/library/stdtypes.html#list), and [`tuple`](https://docs.python.org/3.14/library/stdtypes.html#tuple), or subclasses that haven't overridden `__repr__`. Where the object's representation reveals a recursive entry, that recursive reference shows up as `<Recursion on typename with id=number>`. Beyond that, no further formatting is applied.

```python
>>> pprint.saferepr(stuff)
"[<Recursion on list with id=...>, 'spam', 'eggs', 'lumberjack', 'knights', 'ni']"

```

[Subject index](INDEX.md) · [Previous](pprint-pp-to-pprint-isrecursive.md) · [Continue](pprint-prettyprinter-class.md) · [Owning module, declaration or section: pprint](pprint-data-pretty-printer.md) · [Owning module, declaration or section: Functions](pprint-pp-to-pprint-isrecursive.md)
