# Python 3.12.0 alpha 5 / library / ctypes

[gh-99266](https://github.com/python/cpython/issues/99266): Keep richer error messages around within [`ctypes`](https://docs.python.org/3.14/library/ctypes.html#module-ctypes).

[gh-60580](https://github.com/python/cpython/issues/60580): To align with the Windows SDK, the `ctypes.wintypes.BYTE` definition shifts from [`c_byte`](https://docs.python.org/3.14/library/ctypes.html#ctypes.c_byte) to [`c_ubyte`](https://docs.python.org/3.14/library/ctypes.html#ctypes.c_ubyte). Anatoly Techtonik and Oleg Iarygin supplied the patch.

[gh-77772](https://github.com/python/cpython/issues/77772): The classes [`ctypes.CDLL`](https://docs.python.org/3.14/library/ctypes.html#ctypes.CDLL), [`ctypes.OleDLL`](https://docs.python.org/3.14/library/ctypes.html#ctypes.OleDLL), [`ctypes.WinDLL`](https://docs.python.org/3.14/library/ctypes.html#ctypes.WinDLL), and [`ctypes.PyDLL`](https://docs.python.org/3.14/library/ctypes.html#ctypes.PyDLL) now take [path-like objects](https://docs.python.org/3.14/glossary.html#term-path-like-object) for the `name` argument. Robert Hoelzl supplied the patch.

[bpo-32780](https://bugs.python.org/issue?@action=redirect&bpo=32780): The PEP3118 format strings produced from [`ctypes.Structure`](https://docs.python.org/3.14/library/ctypes.html#ctypes.Structure) objects now carry inter-field padding, mirroring how those objects truly sit in memory.

[gh-99952](https://github.com/python/cpython/issues/99952): Correct a reference undercounting flaw in [`ctypes.Structure`](https://docs.python.org/3.14/library/ctypes.html#ctypes.Structure) when `from_param()` produces results bigger than a C pointer.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
