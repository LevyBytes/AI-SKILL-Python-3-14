# symtable / Examining Symbol Tables: `symtable.Function`, `get_parameters()`, `get_locals()`, `get_globals()`, `get_nonlocals()`, `get_frees()`

*class *symtable.Function

Represents the namespace of a function or method. It derives from `SymbolTable`.

 get_parameters()

Hands back a tuple holding the names of this function's parameters.

 get_locals()

Hands back a tuple holding the names of this function's locals.

 get_globals()

Hands back a tuple holding the names of this function's globals.

 get_nonlocals()

Hands back a tuple holding the names of the nonlocals explicitly declared in this function.

 get_frees()

Hands back a tuple holding the names of this function's [free (closure) variables](https://docs.python.org/3.14/glossary.html#term-closure-variable).

[Subject index](INDEX.md) · [Previous](symbol-table-inspection-and-children.md) · [Continue](symtable-class-class-to-symtable-class-get-methods.md) · [Owning module, declaration or section: symtable](symtable-access-to-the-compiler-s-symbol-tables.md) · [Owning module, declaration or section: Examining Symbol Tables](symtable-symboltabletype-class.md)
