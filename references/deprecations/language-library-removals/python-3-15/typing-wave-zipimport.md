# Language and standard library pending removal in 3.15: typing; wave; zipimport

- [`typing`](https://docs.python.org/3.14/library/typing.html#module-typing):

  - Deprecated since Python 3.13 is the undocumented keyword-argument form for building [`NamedTuple`](https://docs.python.org/3.14/library/typing.html#typing.NamedTuple) classes (for example, `Point = NamedTuple("Point", x=int, y=int)`). Use the class-based syntax or the functional syntax instead.

  - With the functional form of [`TypedDict`](https://docs.python.org/3.14/library/typing.html#typing.TypedDict)s, two patterns have carried a deprecation since Python 3.13: omitting a value for the *fields* parameter (`TD = TypedDict("TD")`), and handing it `None` (`TD = TypedDict("TD", None)`). For a TypedDict holding zero fields, write `class TD(TypedDict): pass` or `TD = TypedDict("TD", {})`.

  - The decorator function [`typing.no_type_check_decorator()`](https://docs.python.org/3.14/library/typing.html#typing.no_type_check_decorator) has been deprecated since Python 3.13. Eight years on within the [`typing`](https://docs.python.org/3.14/library/typing.html#module-typing) module, no major type checker has ever supported it.

- [`wave`](https://docs.python.org/3.14/library/wave.html#module-wave):

  - On the [`Wave_read`](https://docs.python.org/3.14/library/wave.html#wave.Wave_read) and [`Wave_write`](https://docs.python.org/3.14/library/wave.html#wave.Wave_write) classes, the [`getmark()`](https://docs.python.org/3.14/library/wave.html#wave.Wave_read.getmark), `setmark()`, and [`getmarkers()`](https://docs.python.org/3.14/library/wave.html#wave.Wave_read.getmarkers) methods have been deprecated since Python 3.13.

- [`zipimport`](https://docs.python.org/3.14/library/zipimport.html#module-zipimport):

  - Deprecated since Python 3.10, [`load_module()`](https://docs.python.org/3.14/library/zipimport.html#zipimport.zipimporter.load_module) should be replaced with [`exec_module()`](https://docs.python.org/3.14/library/zipimport.html#zipimport.zipimporter.exec_module). (Contributed by Jiahao Li in [gh-125746](https://github.com/python/cpython/issues/125746).)

[Subject index](INDEX.md) · [Previous source section](import-system-through-types.md) · [Next source section](../python-3-16/import-system-through-builtins.md)
