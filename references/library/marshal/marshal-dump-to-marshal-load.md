# marshal: `marshal.dump()`, `marshal.load()`

## marshal - Internal Python object serialization

### `marshal` - Internal Python object serialization

---

Within this module sit functions for reading and writing Python values in a binary form. While that form ties itself to Python, it stays clear of machine architecture concerns (so, for instance, you can write a Python value to a file on a PC, carry the file over to a Mac, and read it back from there). The format's inner workings are left undocumented deliberately; across Python versions it can shift, though that seldom happens. [1]

Treat this as something other than a general “persistence” module. When you need general persistence plus the transfer of Python objects via RPC calls, turn instead to the [`pickle`](https://docs.python.org/3.14/library/pickle.html#module-pickle) and [`shelve`](https://docs.python.org/3.14/library/shelve.html#module-shelve) modules. Chiefly, the `marshal` module is here to back the reading and writing of the “pseudo-compiled” code for the Python modules inside `.pyc` files. For that reason, the Python maintainers keep the freedom to alter the marshal format in backward-incompatible ways whenever it becomes necessary. Code objects don't keep a compatible format across Python versions, even where the format version itself matches. Trying to de-serialize a code object under the wrong Python version yields undefined behavior. Whenever you're serializing and de-serializing Python objects, reach for the `pickle` module in its place — its speed is on par, it guarantees version independence, and pickle copes with a far broader spread of objects than marshal.

Warning

The `marshal` module makes no claim of being safe against faulty or deliberately hostile data. You should never unmarshal data that arrived from an untrusted or unauthenticated source.

The module offers some functions that read and write files, plus others that act on bytes-like objects.

Support does not extend to every Python object type; broadly, only those objects whose value stays independent of any one Python invocation can be written out and read back by this module. Here are the supported types:

- Numeric types: [`int`](https://docs.python.org/3.14/library/functions.html#int), [`bool`](https://docs.python.org/3.14/library/functions.html#bool), [`float`](https://docs.python.org/3.14/library/functions.html#float), [`complex`](https://docs.python.org/3.14/library/functions.html#complex).

- Strings ([`str`](https://docs.python.org/3.14/library/stdtypes.html#str)) and [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes). [Bytes-like objects](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) like [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) are marshalled as `bytes`.

- Containers: [`tuple`](https://docs.python.org/3.14/library/stdtypes.html#tuple), [`list`](https://docs.python.org/3.14/library/stdtypes.html#list), [`set`](https://docs.python.org/3.14/library/stdtypes.html#set), [`frozenset`](https://docs.python.org/3.14/library/stdtypes.html#frozenset), and (as of `version` 5), [`slice`](https://docs.python.org/3.14/library/functions.html#slice). Bear in mind these carry support only when the values held inside them are themselves supported. Containers that recurse have been supported as of `version` 3.

- The singletons [`None`](https://docs.python.org/3.14/library/constants.html#None), [`Ellipsis`](https://docs.python.org/3.14/library/constants.html#Ellipsis) and [`StopIteration`](https://docs.python.org/3.14/library/exceptions.html#StopIteration).

- [`code`](https://docs.python.org/3.14/library/code.html#module-code) objects, if *allow_code* is true. See note above about version dependence.

Changed in version 3.4:

- Added format version 3, which supports marshalling recursive lists, sets and dictionaries.

- Added format version 4, which supports efficient representations of short strings.

Changed in version 3.14: along came format version 5, which makes it possible to marshal slices.

The module makes these functions available:

 marshal.dump(*value*, *file*, *version=version*, */*, ***, *allow_code=True*)

Write the value out to the open file. That value has to be a supported type, and the file has to be a writeable [binary file](https://docs.python.org/3.14/glossary.html#term-binary-file).

Where the value is (or wraps an object that is) of an unsupported type, a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) exception gets raised — yet garbage data lands in the file as well. The object won't read back correctly through `load()`. [Code objects](https://docs.python.org/3.14/reference/datamodel.html#code-objects) are only supported if *allow_code* is true.

By way of the *version* argument you pick which data format `dump` ought to apply (see below).

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `marshal.dumps` with arguments `value`, `version`.

Changed in version 3.13: Added the *allow_code* parameter.

 marshal.load(*file*, */*, ***, *allow_code=True*)

Pull a single value off the open file and hand it back. Where no valid value can be read (for instance because the data carries another Python version's incompatible marshal format), raise [`EOFError`](https://docs.python.org/3.14/library/exceptions.html#EOFError), [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) or [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError). Support for [Code objects](https://docs.python.org/3.14/reference/datamodel.html#code-objects) holds only when *allow_code* is true. A readable [binary file](https://docs.python.org/3.14/glossary.html#term-binary-file) is required for the file.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `marshal.load` with no arguments.

Note

Where an object holding an unsupported type was marshalled via `dump()`, `load()` swaps in `None` in place of that unmarshallable type.

Changed in version 3.10: Previously this call fired a `code.__new__` audit event per code object. These days it fires just one `marshal.load` event spanning the whole load operation.

Changed in version 3.13: Added the *allow_code* parameter.

[Subject index](INDEX.md) · [Continue](marshal-dumps-to-marshal-version.md)
