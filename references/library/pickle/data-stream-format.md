# pickle — Data stream format

### Data stream format

The data format that `pickle` uses is Python-specific. The upside is that no external standards (such as JSON, which can't represent pointer sharing) impose restrictions; the downside is that non-Python programs may be unable to reconstruct pickled Python objects.

By default the `pickle` data format relies on a fairly compact binary representation. When you need the best possible size, you can efficiently [compress](https://docs.python.org/3.14/library/archiving.html) pickled data.

The [`pickletools`](https://docs.python.org/3.14/library/pickletools.html#module-pickletools) module holds tools for examining data streams that `pickle` produces. The `pickletools` source code carries extensive comments covering the opcodes that pickle protocols use.

At present, pickling can use 6 different protocols. The higher the protocol chosen, the more recent the Python version required to read the resulting pickle.

- Protocol version 0 is the original "human-readable" protocol, and it remains backwards compatible with older Python releases.

- Protocol version 1 is an early binary format that is likewise compatible with older Python releases.

- Protocol version 2 arrived with Python 2.3. It pickles [new-style classes](https://docs.python.org/3.14/glossary.html#term-new-style-class) far more efficiently. See [**PEP 307**](https://peps.python.org/pep-0307/) for details on what protocol 2 improves.

- Protocol version 3 arrived with Python 3.0. It explicitly supports [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) objects and cannot be read back by Python 2.x. It was the default protocol across Python 3.0–3.7.

- Protocol version 4 arrived with Python 3.4. It adds support for very large objects, can pickle a wider range of objects, and brings some data-format optimizations. It was the default protocol across Python 3.8–3.13. See [**PEP 3154**](https://peps.python.org/pep-3154/) for details on what protocol 4 improves.

- Protocol version 5 arrived with Python 3.8. It adds support for out-of-band data plus a speedup for in-band data. Beginning with Python 3.14 it is the default protocol. See [**PEP 574**](https://peps.python.org/pep-0574/) for details on what protocol 5 improves.

Note

Serialization is a lower-level idea than persistence; although `pickle` reads and writes file objects, it does not address how to name persistent objects, nor the (still trickier) matter of concurrent access to persistent objects. The `pickle` module can turn a complex object into a byte stream, and it can turn that byte stream back into an object with the same internal structure. Writing those byte streams to a file is perhaps the most obvious use, but it is equally conceivable to ship them across a network or stash them in a database. The [`shelve`](https://docs.python.org/3.14/library/shelve.html#module-shelve) module gives you a simple way to pickle and unpickle objects on DBM-style database files.

[Subject index](INDEX.md) · [Previous](comparison-with-json.md) · [Continue](pickle-highest-protocol-to-pickle-unpicklingerror.md) · [Owning module, declaration or section: pickle](pickle-python-object-serialization.md)
