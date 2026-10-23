# plistlib: `plistlib.load()`, `plistlib.loads()`

## plistlib - Generate and parse Apple .plist files

### `plistlib` - Generate and parse Apple `.plist` files

**Source code:** [Lib/plistlib.py](https://github.com/python/cpython/tree/3.14/Lib/plistlib.py)

---

This module gives you a way to read and write the “property list” files Apple relies on, chiefly on macOS and iOS. Both binary and XML plist files are handled.

A property list (`.plist`) file uses a straightforward serialization format that covers elementary object types — dictionaries, lists, numbers and strings. As a rule, the outermost object is a dictionary.

For writing a plist file out and for parsing one in, call the `dump()` and `load()` functions.

For handling plist data held in bytes or string objects, call `dumps()` and `loads()`.

Permitted values are strings, integers, floats, booleans, tuples, lists, dictionaries (though their keys must be strings), [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes), [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) or [`datetime.datetime`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime) objects.

Changed in version 3.4: A new API arrived and the old one was deprecated. Binary-format plists gained support.

Changed in version 3.8: Reading and writing of `UID` tokens within binary plists — the kind NSKeyedArchiver and NSKeyedUnarchiver produce — became supported.

Changed in version 3.9: Old API removed.

See also

[PList manual page](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/)

Apple's own write-up describing this file format.

The functions this module defines are listed below:

 plistlib.load(*fp*, ***, *fmt=None*, *dict_type=dict*, *aware_datetime=False*)

Reads a plist file. The *fp* argument should be a binary file object opened for reading. Hands back the unpacked root object, which is generally a dictionary.

Here *fmt* names the file's format, and these are the values it accepts:

- [`None`](https://docs.python.org/3.14/library/constants.html#None): Autodetect the file format

- `FMT_XML`: XML file format

- `FMT_BINARY`: Binary plist format

The *dict_type* argument sets which type stands in for dictionaries pulled out of the plist file.

With *aware_datetime* set to true, any field of type `datetime.datetime` is built as an [aware object](https://docs.python.org/3.14/library/datetime.html#datetime-naive-aware) whose `tzinfo` is [`datetime.UTC`](https://docs.python.org/3.14/library/datetime.html#datetime.UTC).

For the `FMT_XML` format, the XML data goes through the Expat parser from [`xml.parsers.expat`](https://docs.python.org/3.14/library/pyexpat.html#module-xml.parsers.expat) – consult that module's documentation for the exceptions malformed XML can throw. Elements it does not recognize are merely passed over by the plist parser.

Should the file resist parsing, the parser throws `InvalidFileException`.

Added in version 3.4.

Changed in version 3.13: The keyword-only parameter *aware_datetime* has been added.

 plistlib.loads(*data*, ***, *fmt=None*, *dict_type=dict*, *aware_datetime=False*)

Loads a plist out of a bytes or string object. Turn to `load()` for a rundown of the keyword arguments.

Added in version 3.4.

Changed in version 3.13: *data* may be a string provided *fmt* is `FMT_XML`.

[Subject index](INDEX.md) · [Continue](plistlib-dump-to-plistlib-dumps.md)
