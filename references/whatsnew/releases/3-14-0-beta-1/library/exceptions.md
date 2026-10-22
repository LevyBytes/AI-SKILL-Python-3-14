# Python 3.14.0 beta 1 / library / exceptions

[gh-132673](https://github.com/python/cpython/issues/132673): Resolve the [`AssertionError`](https://docs.python.org/3.14/library/exceptions.html#AssertionError) thrown for a [`ctypes.Structure`](https://docs.python.org/3.14/library/ctypes.html#ctypes.Structure) declared with `_align_ = 0` together with `_fields_ = []`.

[gh-130402](https://github.com/python/cpython/issues/130402): When a still-running daemon thread is joined while the interpreter is shutting down, [`PythonFinalizationError`](https://docs.python.org/3.14/library/exceptions.html#PythonFinalizationError) is now raised.

[gh-82129](https://github.com/python/cpython/issues/82129): A [`NameError`](https://docs.python.org/3.14/library/exceptions.html#NameError) is fixed that occurred when [`typing.get_type_hints()`](https://docs.python.org/3.14/library/typing.html#typing.get_type_hints) ran on a [`dataclasses.dataclass()`](https://docs.python.org/3.14/library/dataclasses.html#dataclasses.dataclass) produced by [`dataclasses.make_dataclass()`](https://docs.python.org/3.14/library/dataclasses.html#dataclasses.make_dataclass) when fields lacked annotations.

[gh-122559](https://github.com/python/cpython/issues/122559): The `__reduce__()` and `__reduce_ex__()` methods, which always raised [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) in the C versions of [`io.FileIO`](https://docs.python.org/3.14/library/io.html#io.FileIO), [`io.BufferedReader`](https://docs.python.org/3.14/library/io.html#io.BufferedReader), [`io.BufferedWriter`](https://docs.python.org/3.14/library/io.html#io.BufferedWriter) and [`io.BufferedRandom`](https://docs.python.org/3.14/library/io.html#io.BufferedRandom), have been removed; default `__getstate__()` methods that raise `TypeError` take their place. The finer behavioral details of Python 3.11 and earlier are thereby restored.

[gh-132250](https://github.com/python/cpython/issues/132250): Resolved the [`SystemError`](https://docs.python.org/3.14/library/exceptions.html#SystemError) within [`cProfile`](https://docs.python.org/3.14/library/profile.html#module-cProfile) that arose whenever pinpointing a method's underlying C function threw an exception.

[gh-85702](https://github.com/python/cpython/issues/85702): When `zoneinfo._common.load_tzdata` receives a package that has no resource, a `ZoneInfoNotFoundError` gets raised in place of an [`IsADirectoryError`](https://docs.python.org/3.14/library/exceptions.html#IsADirectoryError).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
