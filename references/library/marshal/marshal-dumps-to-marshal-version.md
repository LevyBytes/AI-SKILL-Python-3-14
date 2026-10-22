# marshal: `marshal.dumps()`, `marshal.loads()`, `marshal.version`

marshal.dumps(*value*, *version=version*, */*, ***, *allow_code=True*)

Hand back the bytes object that `dump(value, file)` would have written to a file. The value has to be a supported type. Raise a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) exception where value is (or wraps an object that is) of an unsupported type. [Code objects](https://docs.python.org/3.14/reference/datamodel.html#code-objects) are only supported if *allow_code* is true.

By way of the *version* argument you pick which data format `dumps` ought to apply (see below).

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `marshal.dumps` with arguments `value`, `version`.

Changed in version 3.13: Added the *allow_code* parameter.

 marshal.loads(*bytes*, */*, ***, *allow_code=True*)

Turn the [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) into a value. Where no valid value turns up, raise [`EOFError`](https://docs.python.org/3.14/library/exceptions.html#EOFError), [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) or [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError). [Code objects](https://docs.python.org/3.14/reference/datamodel.html#code-objects) are only supported if *allow_code* is true. Any surplus bytes in the input get disregarded.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `marshal.loads` with argument `bytes`.

Changed in version 3.10: Previously this call fired a `code.__new__` audit event per code object. These days it fires just one `marshal.loads` event spanning the whole load operation.

Changed in version 3.13: Added the *allow_code* parameter.

On top of that, these constants are defined:

 marshal.version

Reports which format the module is using. Version 0 stands as the original first version, with each later version layering on new features. As a rule, a fresh version takes over as the default once it lands.

| Version | Available since | New features |
| --- | --- | --- |
| 1 | Python 2.4 | Sharing interned strings |
| 2 | Python 2.5 | Binary representation of floats |
| 3 | Python 3.4 | Support for object instancing and recursion |
| 4 | Python 3.4 | Efficient representation of short strings |
| 5 | Python 3.14 | Support for `slice` objects |

Footnotes

[Subject index](INDEX.md) · [Previous](marshal-dump-to-marshal-load.md) · [Owning module, declaration or section: marshal](marshal-dump-to-marshal-load.md)
