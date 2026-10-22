# -b

### 1.1.3. Miscellaneous options

 -b

Emit a warning when a [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) or [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) is turned into a [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) without an encoding being named, or when `bytes` or `bytearray` is compared against `str`, or `bytes` against [`int`](https://docs.python.org/3.14/library/functions.html#int). Give the option twice (`-bb`) to turn that into an error instead.

Changed in version 3.5: Affects also comparisons of [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) with [`int`](https://docs.python.org/3.14/library/functions.html#int).

[Subject index](INDEX.md) · [Previous source section](v-version.md) · [Following source section](disable-bytecode-files.md)
