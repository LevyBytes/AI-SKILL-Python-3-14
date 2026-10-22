# pickle / Module Interface: `pickle.Unpickler`, `load()`, `persistent_load()`, `find_class()`

*class *pickle.Unpickler(*file*, ***, *fix_imports=True*, *encoding='ASCII'*, *errors='strict'*, *buffers=None*)

This takes a binary file for reading a pickle data stream.

The pickle's protocol version is detected on its own, so no protocol argument is required.

The *file* argument has to expose three methods: a read() method that accepts an integer argument, a readinto() method that accepts a buffer argument, and a readline() method that takes no arguments, matching the [`io.BufferedIOBase`](https://docs.python.org/3.14/library/io.html#io.BufferedIOBase) interface. Hence *file* could be a disk file opened in binary read mode, an [`io.BytesIO`](https://docs.python.org/3.14/library/io.html#io.BytesIO) object, or any other custom object satisfying that interface.

The optional arguments *fix_imports*, *encoding* and *errors* govern compatibility support for a pickle stream that Python 2 produced. When *fix_imports* is true, pickle attempts to map the old Python 2 names onto the new Python 3 names. The *encoding* and *errors* arguments instruct pickle on decoding the 8-bit string instances Python 2 pickled; their defaults are 'ASCII' and 'strict'. Passing 'bytes' for *encoding* makes those 8-bit string instances come back as bytes objects. You must set `encoding='latin1'` when unpickling NumPy arrays and instances of [`datetime`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime), [`date`](https://docs.python.org/3.14/library/datetime.html#datetime.date) and [`time`](https://docs.python.org/3.14/library/datetime.html#datetime.time) that Python 2 pickled.

When *buffers* is `None` (the default), all the data needed for deserialization has to live within the pickle stream. That means the *buffer_callback* argument was `None` when the `Pickler` was created (or when `dump()` or `dumps()` was called).

When *buffers* is not `None`, it should be an iterable of buffer-enabled objects consumed each time the pickle stream refers to an out-of-band buffer view. Such buffers were given, in order, to the *buffer_callback* of a Pickler object.

Changed in version 3.8: The *buffers* argument was added.

 load()

Read an object's pickled form from the open file object handed to the constructor, then return the object hierarchy that it describes. Any bytes sitting beyond the pickled form of the object are disregarded.

 persistent_load(*pid*)

Raises an `UnpicklingError` by default.

Where it is defined, `persistent_load()` should return the object named by the persistent ID *pid*. When an invalid persistent ID turns up, an `UnpicklingError` should be raised.

See Persistence of External Objects for details and examples of uses.

Changed in version 3.13: A default implementation of this method was added to the C implementation of `Unpickler`.

 find_class(*module*, *name*)

Import *module* when needed and return the object named *name* from it, where the *module* and *name* arguments are [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) objects. Note that, despite what its name suggests, `find_class()` is used for finding functions too.

Subclasses can override this to take charge of which types of objects load and how, which can cut down on security risks. Refer to Restricting Globals for details.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `pickle.find_class` with arguments `module`, `name`.

[Subject index](INDEX.md) · [Previous](pickle-pickler-class-to-pickle-pickler-clear-memo.md) · [Continue](pickle-picklebuffer-class-to-pickle-picklebuffer-release.md) · [Owning module, declaration or section: pickle](pickle-python-object-serialization.md) · [Owning module, declaration or section: Module Interface](pickle-highest-protocol-to-pickle-unpicklingerror.md)
