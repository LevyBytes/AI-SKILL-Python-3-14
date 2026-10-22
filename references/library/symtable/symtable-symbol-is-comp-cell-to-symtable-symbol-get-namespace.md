# symtable.Symbol: `is_comp_cell()`, `is_namespace()`, `get_namespaces()`, `get_namespace()`

is_comp_cell()

Yields `True` when the symbol is a cell belonging to an inlined comprehension.

Added in version 3.14.

 is_namespace()

Yields `True` when binding the name brings a new namespace into existence.

Whenever the name serves as the target of a function or class statement, the result is true.

For example:

```python
>>> table = symtable.symtable("def some_func(): pass", "string", "exec")
>>> table.lookup("some_func").is_namespace()
True

```

Keep in mind that one name may be bound to several objects at once. Even when the result is `True`, that same name might also be bound to other objects — an int or a list, say — that bring no new namespace with them.

 get_namespaces()

Hands back a list of the namespaces bound to this name.

 get_namespace()

Hands back the namespace bound to this name. Should the name have several namespaces bound to it, or none at all, a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised.

[Subject index](INDEX.md) · [Previous](symtable-symbol-class-to-symtable-symbol-is-comp-iter.md) · [Continue](command-line-usage.md) · [Owning module, declaration or section: symtable](symtable-access-to-the-compiler-s-symbol-tables.md) · [Owning module, declaration or section: symtable.Symbol](symtable-symbol-class-to-symtable-symbol-is-comp-iter.md) · [Owning module, declaration or section: Examining Symbol Tables](symtable-symboltabletype-class.md)
