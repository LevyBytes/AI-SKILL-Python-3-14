# pathlib: `PurePath.parser`, `PurePath.drive`, `PurePath.root`

### Methods and properties

Pure paths offer the methods and properties below:

 PurePath.parser

The implementation of the [`os.path`](https://docs.python.org/3.14/library/os.path.html#module-os.path) module relied on for low-level path parsing and joining: either `posixpath` or `ntpath`.

Added in version 3.13.

 PurePath.drive

A string standing for the drive letter or name, where one exists:

```python
>>> PureWindowsPath('c:/Program Files/').drive
'c:'
>>> PureWindowsPath('/Program Files/').drive
''
>>> PurePosixPath('/etc').drive
''

```

UNC shares count as drives too:

```python
>>> PureWindowsPath('//host/share/foo.txt').drive
'\\\\host\\share'

```

 PurePath.root

A string standing for the (local or global) root, where one exists:

```python
>>> PureWindowsPath('c:/Program Files/').root
'\\'
>>> PureWindowsPath('c:Program Files/').root
''
>>> PurePosixPath('/etc').root
'/'

```

UNC shares always carry a root:

```python
>>> PureWindowsPath('//host/share').root
'\\'

```

Should the path open with more than two consecutive slashes, `PurePosixPath` collapses them:

```python
>>> PurePosixPath('//etc').root
'//'
>>> PurePosixPath('///etc').root
'/'
>>> PurePosixPath('////etc').root
'/'

```

Note

This behavior agrees with *The Open Group Base Specifications Issue 6*, paragraph [4.11 Pathname Resolution](https://pubs.opengroup.org/onlinepubs/009695399/basedefs/xbd_chap04.html#tag_04_11):

*“A pathname whose start has two successive slashes may receive an implementation-defined interpretation; however, any count of leading slashes above two shall be handled as though it were a single slash.”*

[Subject index](INDEX.md) · [Previous](purepath-parts.md) · [Continue](purepath-anchor-to-purepath-parent.md) · [Owning module, declaration or section: pathlib](pathlib-object-oriented-filesystem-paths.md)
