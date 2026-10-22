# Language and standard library pending removal in 3.19: ctypes

### Pending removal in Python 3.19

- [`ctypes`](https://docs.python.org/3.14/library/ctypes.html#module-ctypes):

  - On non-Windows platforms, silently adopting the MSVC-compatible struct layout when [`_pack_`](https://docs.python.org/3.14/library/ctypes.html#ctypes.Structure._pack_) is set but [`_layout_`](https://docs.python.org/3.14/library/ctypes.html#ctypes.Structure._layout_) is not.

## Pending removal in Python 3.19

### Pending removal in Python 3.19

- [`ctypes`](https://docs.python.org/3.14/library/ctypes.html#module-ctypes):

  - On non-Windows platforms, implicitly switching to the MSVC-compatible struct layout by setting [`_pack_`](https://docs.python.org/3.14/library/ctypes.html#ctypes.Structure._pack_) without [`_layout_`](https://docs.python.org/3.14/library/ctypes.html#ctypes.Structure._layout_).

[Subject index](INDEX.md) · [Previous source section](../python-3-18/decimal.md) · [Next source section](../unscheduled/argparse-through-importlib.md)
