# Python 3.13.0 alpha 3 / library / pickle

[gh-89850](https://github.com/python/cpython/issues/89850): Add default implementations for the [`pickle.Pickler.persistent_id()`](https://docs.python.org/3.14/library/pickle.html#pickle.Pickler.persistent_id) and [`pickle.Unpickler.persistent_load()`](https://docs.python.org/3.14/library/pickle.html#pickle.Unpickler.persistent_load) methods within the C implementation. Invoking `super().persistent_id()` and `super().persistent_load()` from subclasses of the C implementation of the [`pickle.Pickler`](https://docs.python.org/3.14/library/pickle.html#pickle.Pickler) and [`pickle.Unpickler`](https://docs.python.org/3.14/library/pickle.html#pickle.Unpickler) classes no longer triggers infinite recursion.

[gh-113028](https://github.com/python/cpython/issues/113028): Whenever a second reference to a string shows up in the input to [`pickle`](https://docs.python.org/3.14/library/pickle.html#module-pickle), and the Python implementation is active, a single copy is guaranteed to be pickled and a single object is shared once reloaded. Formerly, under protocol 0, a string holding certain characters (newline, say) yielded duplicate objects.

[bpo-41422](https://bugs.python.org/issue?@action=redirect&bpo=41422): Patch memory leaks in [`pickle.Pickler`](https://docs.python.org/3.14/library/pickle.html#pickle.Pickler) and [`pickle.Unpickler`](https://docs.python.org/3.14/library/pickle.html#pickle.Unpickler) that came from cyclic references through the internal memo mapping.

[gh-85567](https://github.com/python/cpython/issues/85567): Resolved resource warnings about unclosed files within the [`pickle`](https://docs.python.org/3.14/library/pickle.html#module-pickle) and [`pickletools`](https://docs.python.org/3.14/library/pickletools.html#module-pickletools) command line interfaces.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
