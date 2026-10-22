# importlib.machinery — `importlib.machinery` – Importers and path hooks

### `importlib.machinery` – Importers and path hooks

**Source code:** [Lib/importlib/machinery.py](https://github.com/python/cpython/tree/3.14/Lib/importlib/machinery.py)

---

The objects gathered in this module assist [`import`](https://docs.python.org/3.14/reference/simple_stmts.html#import) as it locates and loads modules.

 importlib.machinery.SOURCE_SUFFIXES

A list of strings giving the file suffixes that are recognized for source modules.

Added in version 3.3.

 importlib.machinery.DEBUG_BYTECODE_SUFFIXES

A list of strings giving the file suffixes used by non-optimized bytecode modules.

Added in version 3.3.

Deprecated since version 3.5: Use `BYTECODE_SUFFIXES` instead.

 importlib.machinery.OPTIMIZED_BYTECODE_SUFFIXES

A list of strings giving the file suffixes used by optimized bytecode modules.

Added in version 3.3.

Deprecated since version 3.5: Use `BYTECODE_SUFFIXES` instead.

 importlib.machinery.BYTECODE_SUFFIXES

A list of strings giving the file suffixes recognized for bytecode modules (the leading dot included).

Added in version 3.3.

Changed in version 3.5: The value is no longer dependent on `__debug__`.

 importlib.machinery.EXTENSION_SUFFIXES

A list of strings giving the file suffixes that are recognized for extension modules.

Added in version 3.3.

 importlib.machinery.all_suffixes()

Returns one merged list of strings covering every file suffix that the standard import machinery recognizes for modules. It serves as a convenience for code that only has to decide whether some filesystem path might denote a module, without caring about which module variety is involved (for instance, [`inspect.getmodulename()`](https://docs.python.org/3.14/library/inspect.html#inspect.getmodulename)).

Added in version 3.3.

[Subject index](INDEX.md) · [Previous](../importlib/abstract-source-loader-code-and-package-contract.md) · [Continue](importlib-machinery-builtinimporter-class.md)
