# What's new in Python 3.14 / Pending removal in Python 3.19 - ctypes

### Pending removal in Python 3.19

- [`ctypes`](https://docs.python.org/3.14/library/ctypes.html#module-ctypes):

  - On platforms other than Windows, silently falling back to the MSVC-compatible struct layout by giving [`_pack_`](https://docs.python.org/3.14/library/ctypes.html#ctypes.Structure._pack_) without also giving [`_layout_`](https://docs.python.org/3.14/library/ctypes.html#ctypes.Structure._layout_).

[Subject index](INDEX.md) · [Previous source section](pending-removal-in-python-3-18.md) · [Next source section](undated-api-removals.md) · [Release/subject declaration](summary-release-highlights.md)
