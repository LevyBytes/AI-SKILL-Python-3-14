# What’s New in Python 2.6 / The `plistlib` module: A Property-List Parser — plistlib

### The [`plistlib`](https://docs.python.org/3.14/library/plistlib.html#module-plistlib) module: A Property-List Parser

On Mac OS X the `.plist` format sees wide use for storing elementary values — among them numbers, strings, lists, and dictionaries — which it serializes into a layout built on XML. It bears a likeness to the way XML-RPC serializes data types.

Although it mostly turns up on Mac OS X, there is nothing Mac-specific in the format itself, and the Python implementation runs on every platform Python supports; for that reason the [`plistlib`](https://docs.python.org/3.14/library/plistlib.html#module-plistlib) module has graduated into the standard library.

The module is straightforward to use:

```python
import sys
import plistlib
import datetime as dt

# Create data structure
data_struct = dict(lastAccessed=dt.datetime.now(),
                   version=1,
                   categories=('Personal','Shared','Private'))

# Create string containing XML.
plist_str = plistlib.writePlistToString(data_struct)
new_struct = plistlib.readPlistFromString(plist_str)
print data_struct
print new_struct

# Write data structure to a file and read it back.
plistlib.writePlist(data_struct, '/tmp/customizations.plist')
new_struct = plistlib.readPlist('/tmp/customizations.plist')

# read/writePlist accepts file-like objects as well as paths.
plistlib.writePlist(data_struct, sys.stdout)

```

[Subject index](INDEX.md) · [Previous source section](the-json-module-javascript-object-notation.md) · [Next source section](ctypes-enhancements.md) · [Release/subject declaration](python-3-0.md)
