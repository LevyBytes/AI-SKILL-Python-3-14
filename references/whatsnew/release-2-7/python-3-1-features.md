# What’s New in Python 2.7 / Python 3.1 Features - importlib, io

### Python 3.1 Features

In the same way that Python 2.6 pulled in features from Python 3.0, the 2.7 version brings over some of the fresh features found in Python 3.1. The 2.x line keeps offering tools to assist the move to the 3.x line.

Here is a partial list of the 3.1 features backported into 2.7:

- The syntax for set literals (`{1,2,3}` is a mutable set).

- Dictionary and set comprehensions (`{i: i*2 for i in range(3)}`).

- Multiple context managers in a single [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement.

- A new version of the [`io`](https://docs.python.org/3.14/library/io.html#module-io) library, rewritten in C for performance.

- The ordered-dictionary type covered by PEP 372: Adding an Ordered Dictionary to collections.

- The new `","` format specifier covered by PEP 378: Format Specifier for Thousands Separator.

- The [`memoryview`](https://docs.python.org/3.14/library/stdtypes.html#memoryview) object.

- A small subset of the [`importlib`](https://docs.python.org/3.14/library/importlib.html#module-importlib) module, described below.

- In many cases the [`repr()`](https://docs.python.org/3.14/library/functions.html#repr) of a float `x` is now shorter, since it relies on the briefest decimal string that is assured to round back into `x`. Just as in earlier Python releases, `float(repr(x))` is guaranteed to recover `x`.

- Conversions from float to string and from string to float now round correctly. The [`round()`](https://docs.python.org/3.14/library/functions.html#round) function likewise rounds correctly now.

- The [`PyCapsule`](https://docs.python.org/3.14/c-api/capsule.html#c.PyCapsule) type, used to provide a C API for extension modules.

- The [`PyLong_AsLongAndOverflow()`](https://docs.python.org/3.14/c-api/long.html#c.PyLong_AsLongAndOverflow) C API function.

Additional new Python3-mode warnings include:

- `operator.isCallable()` and `operator.sequenceIncludes()`, which 3.x does not support, now produce warnings.

- The `-3` switch now turns on the `-Qwarn` switch automatically, which raises warnings about employing classic division with integers and long integers.

[Subject index](INDEX.md) · [Previous source section](changes-to-the-handling-of-deprecation-warnings.md) · [Next source section](pep-372-adding-an-ordered-dictionary-to-collections.md) · [Release/subject declaration](the-future-for-python-2-x.md)
