# pyclbr`pyclbr` - Python module browser support

## pyclbr - Python module browser support??

### `pyclbr` - Python module browser support

**Source code:** [Lib/pyclbr.py](https://github.com/python/cpython/tree/3.14/Lib/pyclbr.py)

---

The `pyclbr` module hands you limited information about the functions, classes, and methods defined inside a Python-coded module. That information suffices to build a module browser. It gets pulled straight from the Python source rather than through importing the module, so running this module against untrusted code stays safe. That restriction makes it impossible to apply this module to modules not implemented in Python, taking in all standard and optional extension modules.

 pyclbr.readmodule(*module*, *path=None*)

Hand back a dictionary mapping module-level class names to class descriptors. Where possible, descriptors for imported base classes get included. Parameter *module* is a string carrying which module to read by name; that may be a module nested inside a package. When given, *path* is a sequence of directory paths prepended to `sys.path`, used to track down the module source code.

This function is the original interface and survives only for back compatibility. It hands back a filtered version of the one below.

 pyclbr.readmodule_ex(*module*, *path=None*)

Hand back a dictionary-based tree holding a function or class descriptors for every function and class the module defines via a `def` or `class` statement. That returned dictionary ties module-level function and class names to their descriptors. Nested objects land inside the children dictionary belonging to their parent. Just as with readmodule, *module* picks which module gets read while *path* is prepended to sys.path. Should the module being read be a package, the returned dictionary carries a key `'__path__'` whose value is a list holding the package search path.

Added in version 3.7: Descriptors covering nested definitions. You reach them via the new children attribute. Each one carries a new parent attribute.

The descriptors these functions hand back are instances of Function and Class classes. Users aren't expected to build instances of these classes themselves.

[Subject index](INDEX.md) · [Continue](pyclbr-function-class.md)
