# symtable / Examining Symbol Tables: `symtable.Class`, `get_methods()`

*class *symtable.Class

Represents the namespace of a class. It derives from `SymbolTable`.

 get_methods()

Hands back a tuple with the names of the method-like functions the class declares.

In this context, ‘method’ stands for *any* function written inside the class body through [`def`](https://docs.python.org/3.14/reference/compound_stmts.html#def) or [`async def`](https://docs.python.org/3.14/reference/compound_stmts.html#async-def).

Any function sitting in a deeper scope, such as one inside an inner class, falls outside what `get_methods()` reports.

For example:

```pycon
>>> import symtable
>>> st = symtable.symtable('''
... def outer(): pass
...
... class A:
...    def f():
...        def w(): pass
...
...    def g(self): pass
...
...    @classmethod
...    async def h(cls): pass
...
...    global outer
...    def outer(self): pass
... ''', 'test', 'exec')
>>> class_A = st.get_children()[2]
>>> class_A.get_methods()
('f', 'g', 'h')

```

Even though calling `A().f()` triggers a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) at runtime, `A.f` still counts as a method-like function.

Deprecated since version 3.14, will be removed in version 3.16.

[Subject index](INDEX.md) · [Previous](symtable-function-class-to-symtable-function-get-frees.md) · [Continue](symtable-symbol-class-to-symtable-symbol-is-comp-iter.md) · [Owning module, declaration or section: symtable](symtable-access-to-the-compiler-s-symbol-tables.md) · [Owning module, declaration or section: Examining Symbol Tables](symtable-symboltabletype-class.md)
