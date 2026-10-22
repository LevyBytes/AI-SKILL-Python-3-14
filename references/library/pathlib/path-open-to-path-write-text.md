# pathlib: `Path.open()`, `Path.read_text()`, `Path.read_bytes()`, `Path.write_text()`

### Reading and writing files

 Path.open(*mode='r'*, *buffering=-1*, *encoding=None*, *errors=None*, *newline=None*)

Open the file the path points at, the way the built-in [`open()`](https://docs.python.org/3.14/library/functions.html#open) function does:

```python
>>> p = Path('setup.py')
>>> with p.open() as f:
...     f.readline()
...
'#!/usr/bin/env python3\n'

```

 Path.read_text(*encoding=None*, *errors=None*, *newline=None*)

Return the decoded contents of the pointed-to file as a string:

```python
>>> p = Path('my_text_file')
>>> p.write_text('Text file contents')
18
>>> p.read_text()
'Text file contents'

```

The file gets opened and then closed afterward. The optional parameters carry the same meaning they do in [`open()`](https://docs.python.org/3.14/library/functions.html#open).

Added in version 3.5.

Changed in version 3.13: The *newline* parameter was added.

 Path.read_bytes()

Hand back, as a bytes object, the binary contents of the file being pointed to:

```python
>>> p = Path('my_binary_file')
>>> p.write_bytes(b'Binary file contents')
20
>>> p.read_bytes()
b'Binary file contents'

```

Added in version 3.5.

 Path.write_text(*data*, *encoding=None*, *errors=None*, *newline=None*)

Open the pointed-to file in text mode, write *data* into it, then close the file:

```python
>>> p = Path('my_text_file')
>>> p.write_text('Text file contents')
18
>>> p.read_text()
'Text file contents'

```

Any existing file bearing the same name gets overwritten. The optional parameters carry the same meaning they do in [`open()`](https://docs.python.org/3.14/library/functions.html#open).

Added in version 3.5.

Changed in version 3.10: The *newline* parameter was added.

[Subject index](INDEX.md) · [Previous](path-is-socket-to-path-info.md) · [Continue](path-write-bytes.md) · [Owning module, declaration or section: pathlib](pathlib-object-oriented-filesystem-paths.md)
