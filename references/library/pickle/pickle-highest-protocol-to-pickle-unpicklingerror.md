# pickle: `pickle.HIGHEST_PROTOCOL`, `pickle.DEFAULT_PROTOCOL`, `pickle.dump()`, `pickle.dumps()`, `pickle.load()`, `pickle.loads()`, `pickle.PickleError`, `pickle.PicklingError`, `pickle.UnpicklingError`

### Module Interface

Serializing an object hierarchy is as easy as calling the `dumps()` function. In the same vein, de-serializing a data stream is a matter of calling the `loads()` function. Should you want finer control over serialization and de-serialization, however, you can build a `Pickler` or an `Unpickler` object, respectively.

The `pickle` module provides the following constants:

 pickle.HIGHEST_PROTOCOL

An integer giving the highest protocol version on offer. You can pass this value as a *protocol* to the `dump()` and `dumps()` functions and to the `Pickler` constructor.

 pickle.DEFAULT_PROTOCOL

An integer giving the default protocol version used for pickling. It may be below `HIGHEST_PROTOCOL`. The default protocol is currently 5, which appeared in Python 3.8 and is not compatible with earlier versions. This version brings support for out-of-band buffers, where [**PEP 3118**](https://peps.python.org/pep-3118/)-compatible data can travel apart from the main pickle stream.

Changed in version 3.0: The default protocol is 3.

Changed in version 3.8: The default protocol is 4.

Changed in version 3.14: The default protocol is 5.

For greater convenience while pickling, the `pickle` module offers these functions:

 pickle.dump(*obj*, *file*, *protocol=None*, ***, *fix_imports=True*, *buffer_callback=None*)

Write the pickled form of the object *obj* to the open [file object](https://docs.python.org/3.14/glossary.html#term-file-object) *file*. This amounts to `Pickler(file, protocol).dump(obj)`.

The *file*, *protocol*, *fix_imports* and *buffer_callback* arguments carry the meanings they have in the `Pickler` constructor.

Changed in version 3.8: The *buffer_callback* argument was added.

 pickle.dumps(*obj*, *protocol=None*, ***, *fix_imports=True*, *buffer_callback=None*)

Return the pickled form of the object *obj* as a [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) object, rather than writing it out to a file.

The *protocol*, *fix_imports* and *buffer_callback* arguments mean what they do in the `Pickler` constructor.

Changed in version 3.8: The *buffer_callback* argument was added.

 pickle.load(*file*, ***, *fix_imports=True*, *encoding='ASCII'*, *errors='strict'*, *buffers=None*)

Read the pickled form of an object out of the open [file object](https://docs.python.org/3.14/glossary.html#term-file-object) *file* and give back the object hierarchy it describes. This amounts to `Unpickler(file).load()`.

The pickle's protocol version is detected on its own, so no protocol argument is required. Any bytes that follow the pickled form of the object are ignored.

The *file*, *fix_imports*, *encoding*, *errors*, *strict* and *buffers* arguments take on the meanings they have in the `Unpickler` constructor.

Changed in version 3.8: The *buffers* argument was added.

 pickle.loads(*data*, */*, ***, *fix_imports=True*, *encoding='ASCII'*, *errors='strict'*, *buffers=None*)

Give back the object hierarchy described by the pickled form *data* of an object. *data* has to be a [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object).

The pickle's protocol version is detected on its own, so no protocol argument is required. Any bytes that follow the pickled form of the object are ignored.

The *fix_imports*, *encoding*, *errors*, *strict* and *buffers* arguments hold the same meanings they do in the `Unpickler` constructor.

Changed in version 3.8: The *buffers* argument was added.

The `pickle` module defines three exceptions:

 *exception *pickle.PickleError

The shared base class for the other pickling exceptions. It derives from [`Exception`](https://docs.python.org/3.14/library/exceptions.html#Exception).

 *exception *pickle.PicklingError

Raised when `Pickler` meets an unpicklable object. It derives from `PickleError`.

See What can be pickled and unpickled? to find out which kinds of objects can be pickled.

 *exception *pickle.UnpicklingError

Raised when unpickling an object runs into trouble, such as data corruption or a security violation. It derives from `PickleError`.

Keep in mind that unpickling can raise other exceptions too, among them (though not only) AttributeError, EOFError, ImportError, and IndexError.

The `pickle` module exports three classes, `Pickler`, `Unpickler` and `PickleBuffer`:

[Subject index](INDEX.md) · [Previous](data-stream-format.md) · [Continue](pickle-pickler-class-to-pickle-pickler-clear-memo.md) · [Owning module, declaration or section: pickle](pickle-python-object-serialization.md)
