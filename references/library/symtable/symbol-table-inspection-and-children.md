# symtable / Examining Symbol Tables: `symtable.SymbolTable`, `get_type()`, `get_id()`, `get_name()`, `get_lineno()`, `is_optimized()`, `is_nested()`, `has_children()`, `get_identifiers()`, `lookup()`, `get_symbols()`, `get_children()`

*class *symtable.SymbolTable

Holds the namespace table for a block. Its constructor is not part of the public interface.

 get_type()

Hands back the symbol table's type; whatever it returns is one of the `SymbolTableType` enumeration members.

Changed in version 3.12: Added `'annotation'`, `'TypeVar bound'`, `'type alias'`, and `'type parameter'` as possible return values.

Changed in version 3.13: Return values are members of the `SymbolTableType` enumeration.

Because the precise string values returned could shift in later releases, you are advised to rely on `SymbolTableType` members rather than on hard-coded strings.

 get_id()

Hands back the identifier belonging to the table.

 get_name()

Hands back the name attached to the table. When the table belongs to a class it is that class's name, when it belongs to a function it is that function's name, and when the table is global it is `'top'` (in which case `get_type()` yields `'module'`). Within type parameter scopes — the ones serving generic classes, generic functions, and type aliases — the value is the name of the class, function, or type alias underneath. Within a type alias scope it is the type alias's own name, and within a [`TypeVar`](https://docs.python.org/3.14/library/typing.html#typing.TypeVar) bound scope it is the name of the `TypeVar`.

 get_lineno()

Hands back the line number where the block that this table stands for begins.

 is_optimized()

Yields `True` when the locals held in this table are eligible for optimization.

 is_nested()

Yields `True` when the block is a class or function nested inside another.

 has_children()

Yields `True` when the block contains namespaces nested inside it; you can retrieve those through `get_children()`.

 get_identifiers()

Hands back a view object that holds the names of the table's symbols. Refer to the [documentation of view objects](https://docs.python.org/3.14/library/stdtypes.html#dict-views).

 lookup(*name*)

Searches the table for *name* and gives back a `Symbol` instance.

 get_symbols()

Hands back a list of `Symbol` instances, one per name in the table.

 get_children()

Hands back a list of the symbol tables nested inside.

[Subject index](INDEX.md) · [Previous](symtable-symboltabletype-class.md) · [Continue](symtable-function-class-to-symtable-function-get-frees.md) · [Owning module, declaration or section: symtable](symtable-access-to-the-compiler-s-symbol-tables.md) · [Owning module, declaration or section: Examining Symbol Tables](symtable-symboltabletype-class.md)
