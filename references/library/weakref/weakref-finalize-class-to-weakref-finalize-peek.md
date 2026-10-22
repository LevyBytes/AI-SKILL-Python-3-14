# weakref / Weak references: `weakref.finalize`, `__call__()`, `detach()`, `peek()`

*class *weakref.finalize(*obj*, *func*, */*, **args*, ***kwargs*)

Hand back a callable finalizer object that fires once *obj* is garbage collected. In contrast to an everyday weak reference, a finalizer is guaranteed to endure until the reference object is collected, which makes lifecycle management far easier.

A finalizer counts as *alive* up to the point it is called (whether explicitly or at garbage collection), and is *dead* thereafter. Calling a live finalizer hands back the outcome of evaluating `func(*arg, **kwargs)`, while calling a dead one hands back [`None`](https://docs.python.org/3.14/library/constants.html#None).

Any exception a finalizer callback throws during garbage collection is surfaced on the standard error output but cannot be propagated. Such exceptions are treated just as those thrown from an object's [`__del__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__del__) method or from a weak reference's callback.

As the program exits, every live finalizer still left is called unless its [`atexit`](https://docs.python.org/3.14/library/atexit.html#module-atexit) attribute has been set to false, and they run in the reverse of the order they were created.

A finalizer never triggers its callback during the latter stages of [interpreter shutdown](https://docs.python.org/3.14/glossary.html#term-interpreter-shutdown), the point at which module globals stand a good chance of having been swapped out for [`None`](https://docs.python.org/3.14/library/constants.html#None).

 __call__()

Should *self* be alive, flag it dead and hand back what calling `func(*args, **kwargs)` produces. Should *self* be dead, hand back [`None`](https://docs.python.org/3.14/library/constants.html#None).

 detach()

Should *self* be alive, flag it dead and hand back the tuple `(obj, func, args, kwargs)`. Should *self* be dead, hand back [`None`](https://docs.python.org/3.14/library/constants.html#None).

 peek()

Should *self* be alive, hand back the tuple `(obj, func, args, kwargs)` without changing its state. Should *self* be dead, hand back [`None`](https://docs.python.org/3.14/library/constants.html#None).

 alive

A property that reads true while the finalizer is alive and false once it is not.

 atexit

A writable boolean property defaulting to true. As the program exits, it runs every live finalizer still left whose `atexit` is true, in the reverse of the order they were created.

Note

Take care that *func*, *args*, and *kwargs* hold no references to *obj*, whether straight or roundabout, because otherwise *obj* will never be garbage collected. In particular, do not let *func* be a bound method of *obj*.

Added in version 3.4.

[Subject index](INDEX.md) · [Previous](weakref-weakmethod-class.md) · [Continue](weakref-referencetype-class.md) · [Owning module, declaration or section: weakref](weakref-ref-class.md)
