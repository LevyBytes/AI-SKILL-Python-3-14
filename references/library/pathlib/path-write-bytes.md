# pathlib: `Path.write_bytes()`

Path.write_bytes(*data*)

Open the pointed-to file in bytes mode, write *data* into it, then close the file:

```python
>>> p = Path('my_binary_file')
>>> p.write_bytes(b'Binary file contents')
20
>>> p.read_bytes()
b'Binary file contents'

```

Any existing file bearing the same name gets overwritten.

Added in version 3.5.

[Subject index](INDEX.md) · [Previous](path-open-to-path-write-text.md) · [Continue](path-iterdir-to-path-glob.md) · [Owning module, declaration or section: pathlib](pathlib-object-oriented-filesystem-paths.md) · [Owning module, declaration or section: Reading and writing files](path-open-to-path-write-text.md)
