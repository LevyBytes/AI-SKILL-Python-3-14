# symtable: `symtable.SymbolTableType`

### Examining Symbol Tables

 *class *symtable.SymbolTableType

An enumeration whose members tell you what kind a given `SymbolTable` object is.

 MODULE* = "module"*

Applies to a module's symbol table.

 FUNCTION* = "function"*

Applies to a function's symbol table.

 CLASS* = "class"*

Applies to a class's symbol table.

The members listed next correspond to the various kinds of [annotation scopes](https://docs.python.org/3.14/reference/executionmodel.html#annotation-scopes).

 ANNOTATION* = "annotation"*

Covers annotations whenever `from __future__ import annotations` is in effect.

 TYPE_ALIAS* = "type alias"*

Applies to the symbol table of [`type`](https://docs.python.org/3.14/reference/simple_stmts.html#type) constructions.

 TYPE_PARAMETERS* = "type parameters"*

Applies to the symbol table of [generic functions](https://docs.python.org/3.14/reference/compound_stmts.html#generic-functions) or [generic classes](https://docs.python.org/3.14/reference/compound_stmts.html#generic-classes).

 TYPE_VARIABLE* = "type variable"*

Marks the symbol table tied to the bound, the constraint tuple, or the default of one type variable taken in the strict sense — that is, a TypeVar, a TypeVarTuple, or a ParamSpec object, where the last two of these accept neither a bound nor a constraint tuple.

Added in version 3.13.

[Subject index](INDEX.md) · [Previous](symtable-symtable.md) · [Continue](symbol-table-inspection-and-children.md) · [Owning module, declaration or section: symtable](symtable-access-to-the-compiler-s-symbol-tables.md)
