# Python 3.14.0 alpha 1 / library / symtable

[gh-119698](https://github.com/python/cpython/issues/119698): Given how little interest [`symtable.Class.get_methods()`](https://docs.python.org/3.14/library/symtable.html#symtable.Class.get_methods) drew, the method now carries a deprecation marker and is set to disappear in Python 3.16. Patch by Bénédikt Tran.

[gh-120029](https://github.com/python/cpython/issues/120029): Make [`symtable.Symbol.is_type_parameter()`](https://docs.python.org/3.14/library/symtable.html#symtable.Symbol.is_type_parameter) accessible from the [`symtable`](https://docs.python.org/3.14/library/symtable.html#module-symtable) module. Bénédikt Tran wrote the patch.

[gh-119698](https://github.com/python/cpython/issues/119698): Repair [`symtable.Class.get_methods()`](https://docs.python.org/3.14/library/symtable.html#symtable.Class.get_methods) and write up its behaviour. Bénédikt Tran authored the patch.

[gh-119933](https://github.com/python/cpython/issues/119933): Introduce the [`symtable.SymbolTableType`](https://docs.python.org/3.14/library/symtable.html#symtable.SymbolTableType) enumeration that captures the possible return values of the [`symtable.SymbolTable.get_type`](https://docs.python.org/3.14/library/symtable.html#symtable.SymbolTable.get_type) method. Bénédikt Tran wrote the patch.

[gh-120029](https://github.com/python/cpython/issues/120029): Surface the [`symtable.Symbol`](https://docs.python.org/3.14/library/symtable.html#symtable.Symbol) methods [`is_free_class()`](https://docs.python.org/3.14/library/symtable.html#symtable.Symbol.is_free_class), [`is_comp_iter()`](https://docs.python.org/3.14/library/symtable.html#symtable.Symbol.is_comp_iter) and [`is_comp_cell()`](https://docs.python.org/3.14/library/symtable.html#symtable.Symbol.is_comp_cell). Bénédikt Tran supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
