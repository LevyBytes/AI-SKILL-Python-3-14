# plistlib: `plistlib.dump()`, `plistlib.dumps()`

plistlib.dump(*value*, *fp*, ***, *fmt=FMT_XML*, *sort_keys=True*, *skipkeys=False*, *aware_datetime=False*)

Writes *value* into a plist file. The *fp* argument should be a binary file object opened for writing.

Through the *fmt* argument you set the plist file's format, and it may take one of these values:

- `FMT_XML`: XML formatted plist file

- `FMT_BINARY`: Binary formatted plist file

With *sort_keys* true (its default), dictionary keys land in the plist sorted; otherwise they land in whatever order the dictionary iterates.

With *skipkeys* false (its default), the function throws [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) the moment a dictionary key is not a string; otherwise it quietly drops such keys.

With *aware_datetime* true, any field of type `datetime.datetime` that is set as an [aware object](https://docs.python.org/3.14/library/datetime.html#datetime-naive-aware) gets converted to the UTC timezone before being written.

A [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) gets thrown whenever the object is of an unsupported type, or is a container holding objects of unsupported types.

An [`OverflowError`](https://docs.python.org/3.14/library/exceptions.html#OverflowError) gets thrown for integer values too large to fit inside (binary) plist files.

Added in version 3.4.

Changed in version 3.13: The keyword-only parameter *aware_datetime* has been added.

 plistlib.dumps(*value*, ***, *fmt=FMT_XML*, *sort_keys=True*, *skipkeys=False*, *aware_datetime=False*)

Hands back *value* as a plist-formatted bytes object. For a rundown of this function's keyword arguments, turn to the `dump()` documentation.

Added in version 3.4.

These are the classes on offer:

[Subject index](INDEX.md) · [Previous](plistlib-load-to-plistlib-loads.md) · [Continue](plistlib-uid-class.md) · [Owning module, declaration or section: plistlib](plistlib-load-to-plistlib-loads.md)
