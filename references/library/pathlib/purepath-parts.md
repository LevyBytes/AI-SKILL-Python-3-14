# pathlib — Accessing individual parts

### Accessing individual parts

To reach the individual "parts" (components) of a path, use the property below:

 PurePath.parts

A tuple granting access to the path's separate components:

```python
>>> p = PurePath('/usr/bin/python3')
>>> p.parts
('/', 'usr', 'bin', 'python3')

>>> p = PureWindowsPath('c:/Program Files/PSF')
>>> p.parts
('c:\\', 'Program Files', 'PSF')

```

(note how the drive and local root get grouped together into a single part)

[Subject index](INDEX.md) · [Previous](operators.md) · [Continue](purepath-parser-to-purepath-root.md) · [Owning module, declaration or section: pathlib](pathlib-object-oriented-filesystem-paths.md)
