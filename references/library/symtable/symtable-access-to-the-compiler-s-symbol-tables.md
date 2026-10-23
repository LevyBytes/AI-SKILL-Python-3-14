# symtable`symtable` - Access to the compiler’s symbol tables

## symtable - Access to the compiler’s symbol tables

### `symtable` - Access to the compiler’s symbol tables

**Source code:** [Lib/symtable.py](https://github.com/python/cpython/tree/3.14/Lib/symtable.py)

---

Working from the AST, the compiler builds symbol tables right before it emits bytecode. Each such table works out the scope of every identifier appearing in the code. To inspect these tables, you reach for the interface that `symtable` supplies.

[Subject index](INDEX.md) · [Continue](symtable-symtable.md)
