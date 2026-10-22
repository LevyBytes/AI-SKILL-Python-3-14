# Language and standard library pending removal in 3.15: types; typing; wave; zipimport

- [`types`](https://docs.python.org/3.14/library/types.html#module-types):

  - [`types.CodeType`](https://docs.python.org/3.14/library/types.html#types.CodeType): Reading [`co_lnotab`](https://docs.python.org/3.14/reference/datamodel.html#codeobject.co_lnotab) became deprecated under [**PEP 626**](https://peps.python.org/pep-0626/) back in 3.10 and was slated for removal in 3.12, yet a real [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning) only arrived in 3.12. Removal may land in 3.15. (Contributed by Nikita Sobolev in [gh-101866](https://github.com/python/cpython/issues/101866).)

- [`typing`](https://docs.python.org/3.14/library/typing.html#module-typing):

  - Deprecated since Python 3.13: the undocumented keyword-argument form for building [`NamedTuple`](https://docs.python.org/3.14/library/typing.html#typing.NamedTuple) classes (such as `Point = NamedTuple("Point", x=int, y=int)`). Reach for the class-based or functional syntax in its place.

  - With the functional form of [`TypedDict`](https://docs.python.org/3.14/library/typing.html#typing.TypedDict)s, omitting a value for the *fields* parameter (`TD = TypedDict("TD")`) or supplying `None` (`TD = TypedDict("TD", None)`) has been deprecated since Python 3.13. To build a TypedDict with no field, write `class TD(TypedDict): pass` or `TD = TypedDict("TD", {})`.

  - Deprecated since Python 3.13, the [`typing.no_type_check_decorator()`](https://docs.python.org/3.14/library/typing.html#typing.no_type_check_decorator) decorator function has spent eight years in the [`typing`](https://docs.python.org/3.14/library/typing.html#module-typing) module and still lacks support from any major type checker.

- [`wave`](https://docs.python.org/3.14/library/wave.html#module-wave):

  - Since Python 3.13, the [`getmark()`](https://docs.python.org/3.14/library/wave.html#wave.Wave_read.getmark), `setmark()`, and [`getmarkers()`](https://docs.python.org/3.14/library/wave.html#wave.Wave_read.getmarkers) methods on the [`Wave_read`](https://docs.python.org/3.14/library/wave.html#wave.Wave_read) and [`Wave_write`](https://docs.python.org/3.14/library/wave.html#wave.Wave_write) classes have carried deprecations.

- [`zipimport`](https://docs.python.org/3.14/library/zipimport.html#module-zipimport):

  - Deprecated since Python 3.10, [`load_module()`](https://docs.python.org/3.14/library/zipimport.html#zipimport.zipimporter.load_module) should be swapped for [`exec_module()`](https://docs.python.org/3.14/library/zipimport.html#zipimport.zipimporter.exec_module). (Contributed by Jiahao Li in [gh-125746](https://github.com/python/cpython/issues/125746).)

[Subject index](INDEX.md) · [Previous source section](import-system-through-threading.md) · [Next source section](../python-3-16/import-system-through-builtins.md)
