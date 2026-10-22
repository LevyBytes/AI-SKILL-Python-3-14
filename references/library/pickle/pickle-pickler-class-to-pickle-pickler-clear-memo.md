# pickle / Module Interface: `pickle.Pickler`, `dump()`, `persistent_id()`, `reducer_override()`, `clear_memo()`

*class *pickle.Pickler(*file*, *protocol=None*, ***, *fix_imports=True*, *buffer_callback=None*)

This takes a binary file for writing a pickle data stream.

The optional *protocol* argument, an integer, tells the pickler which protocol to use; the supported protocols run from 0 through `HIGHEST_PROTOCOL`. When unspecified, the default is `DEFAULT_PROTOCOL`. When a negative number is given, `HIGHEST_PROTOCOL` is selected.

The *file* argument has to provide a write() method that accepts a single bytes argument. Suitable candidates include a disk file opened in binary write mode, an [`io.BytesIO`](https://docs.python.org/3.14/library/io.html#io.BytesIO) instance, or any other custom object satisfying that interface.

When *fix_imports* is true and *protocol* is below 3, pickle attempts to map the new Python 3 names onto the old module names from Python 2, so that Python 2 can read the pickle data stream.

When *buffer_callback* is `None` (the default), buffer views get serialized into *file* as part of the pickle stream.

When *buffer_callback* is not `None`, it may be called any number of times with a buffer view. When the callback returns a false value (for example `None`), the given buffer is treated as out-of-band; otherwise the buffer is serialized in-band, that is, inside the pickle stream.

Supplying a non-`None` *buffer_callback* while *protocol* is `None` or below 5 is an error.

Changed in version 3.8: The *buffer_callback* argument was added.

 dump(*obj*)

Write *obj*'s pickled representation out to the open file object supplied to the constructor.

 persistent_id(*obj*)

Does nothing by default. It exists so that a subclass can override it.

When `persistent_id()` returns `None`, *obj* is pickled the usual way. Any other value makes `Pickler` emit the returned value as a persistent ID for *obj*. What that persistent ID means is up to `Unpickler.persistent_load()` to define. Keep in mind that the value `persistent_id()` returns cannot itself carry a persistent ID.

See Persistence of External Objects for details and examples of uses.

Changed in version 3.13: A default implementation of this method was added to the C implementation of `Pickler`.

 dispatch_table

A pickler object's dispatch table is a registry of *reduction functions*, the kind you can declare with [`copyreg.pickle()`](https://docs.python.org/3.14/library/copyreg.html#copyreg.pickle). It maps classes (the keys) to reduction functions (the values). Such a reduction function accepts a lone argument of the matching class and should follow the same interface as a `__reduce__()` method.

By default a pickler object carries no `dispatch_table` attribute, and instead falls back on the global dispatch table that the [`copyreg`](https://docs.python.org/3.14/library/copyreg.html#module-copyreg) module manages. To tailor the pickling of a particular pickler object, though, you can set its `dispatch_table` attribute to a dict-like object. Alternatively, when a subclass of `Pickler` carries a `dispatch_table` attribute, that becomes the default dispatch table for instances of the class.

See Dispatch Tables for usage examples.

Added in version 3.3.

 reducer_override(*obj*)

A special reducer you can define in `Pickler` subclasses. This method outranks any reducer in the `dispatch_table`. It should obey the same interface as a `__reduce__()` method, and it may optionally return [`NotImplemented`](https://docs.python.org/3.14/library/constants.html#NotImplemented) to fall back on `dispatch_table`-registered reducers for pickling `obj`.

A worked example appears under Custom Reduction for Types, Functions, and Other Objects.

Added in version 3.8.

 fast

Deprecated. Switch on fast mode by setting it to a true value. Fast mode turns off the use of the memo, thereby quickening the pickling process by avoiding superfluous PUT opcodes. Do not use it with self-referential objects; doing so will make `Pickler` recurse without end.

Use [`pickletools.optimize()`](https://docs.python.org/3.14/library/pickletools.html#pickletools.optimize) if you need more compact pickles.

 clear_memo()

Clears the pickler's "memo".

The memo is the data structure recording the objects the pickler has encountered already, which lets shared or recursive objects be pickled by reference instead of by value. This method is handy when you reuse picklers.

[Subject index](INDEX.md) · [Previous](pickle-highest-protocol-to-pickle-unpicklingerror.md) · [Continue](pickle-unpickler-class-to-pickle-unpickler-find-class.md) · [Owning module, declaration or section: pickle](pickle-python-object-serialization.md) · [Owning module, declaration or section: Module Interface](pickle-highest-protocol-to-pickle-unpicklingerror.md)
