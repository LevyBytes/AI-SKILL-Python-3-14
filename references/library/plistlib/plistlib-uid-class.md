# plistlib: `plistlib.UID`

*class *plistlib.UID(*data*)

Encloses an [`int`](https://docs.python.org/3.14/library/functions.html#int). It comes into play while reading or writing NSKeyedArchiver-encoded data, which carries UID (consult the PList manual).

 data

The UID's integer value. It has to lie within the range `0 <= data < 2**64`.

Added in version 3.8.

These are the constants on offer:

[Subject index](INDEX.md) · [Previous](plistlib-dump-to-plistlib-dumps.md) · [Continue](plistlib-fmt-xml-to-plistlib-invalidfileexception.md) · [Owning module, declaration or section: plistlib](plistlib-load-to-plistlib-loads.md)
