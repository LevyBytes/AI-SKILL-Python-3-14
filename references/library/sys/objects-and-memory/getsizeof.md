# sys.getsizeof

sys.getsizeof(*object*[, *default*])

Report an object's size in bytes. The argument may be an object of any type. Every built-in object yields a correct figure, though third-party extensions need not, because the behavior is implementation specific.

Only memory charged directly to the object itself is counted, never the memory used by whatever other objects it points to.

When supplied, *default* is handed back if the object offers no way to report its size. Failing that, a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) is raised.

`getsizeof()` invokes the object's `__sizeof__` method and tacks on extra garbage collector overhead whenever the garbage collector manages the object.

Refer to the [recursive sizeof recipe](https://code.activestate.com/recipes/577504-compute-memory-footprint-of-an-object-and-its-cont/) for a worked example applying `getsizeof()` recursively to measure containers together with all that they hold.

[API family](INDEX.md) · [sys context index](../INDEX.md).
