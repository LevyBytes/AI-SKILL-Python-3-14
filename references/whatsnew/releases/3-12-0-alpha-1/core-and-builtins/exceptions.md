# Python 3.12.0 alpha 1 / core and builtins / exceptions

[gh-95185](https://github.com/python/cpython/issues/95185): Avoid crashes in the AST constructor while compiling absurdly long expressions such as `"+0"*1000000`. A [`RecursionError`](https://docs.python.org/3.14/library/exceptions.html#RecursionError) is now raised in their place. Pablo Galindo wrote the patch

[gh-96352](https://github.com/python/cpython/issues/96352): Repair the [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError) that was missing its `name` and `obj` attributes in [`object.__getattribute__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getattribute__). Philip Georgi wrote the patch.

[gh-97922](https://github.com/python/cpython/issues/97922): Rather than firing on object allocations, the Garbage Collector now runs solely off the eval breaker mechanism of the Python bytecode evaluation loop. The GC may additionally fire whenever [`PyErr_CheckSignals()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_CheckSignals) gets called, so C extensions running a long while without any Python code in between still get a periodic chance to trigger the GC.

[gh-96670](https://github.com/python/cpython/issues/96670): Source code carrying null bytes now triggers a [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError) from the parser. Pablo Galindo wrote the patch

[gh-95778](https://github.com/python/cpython/issues/95778): The error message raised as a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) when an integer exceeds the limit now points to the [`sys.set_int_max_str_digits()`](https://docs.python.org/3.14/library/sys.html#sys.set_int_max_str_digits) function. Victor Stinner wrote the patch.

[gh-96864](https://github.com/python/cpython/issues/96864): Repair a possible assertion failure, fatal error, or [`SystemError`](https://docs.python.org/3.14/library/exceptions.html#SystemError) that arose when a line tracing event raised an exception while opcode tracing was switched on.

[gh-98254](https://github.com/python/cpython/issues/98254): When the interpreter raises an [`NameError`](https://docs.python.org/3.14/library/exceptions.html#NameError) at the top level, its error messages may now propose modules drawn from the standard library as candidates. Pablo Galindo wrote the patch

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
