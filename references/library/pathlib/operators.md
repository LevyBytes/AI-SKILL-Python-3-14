# pathlib - Operators

### Operators

The slash operator assists in building child paths, like [`os.path.join()`](https://docs.python.org/3.14/library/os.path.html#os.path.join). Where the argument is an absolute path, the earlier path is dropped. On Windows, the drive does not reset when the argument is a rooted relative path (such as `r'\foo'`):

```python
>>> p = PurePath('/etc')
>>> p
PurePosixPath('/etc')
>>> p / 'init.d' / 'apache2'
PurePosixPath('/etc/init.d/apache2')
>>> q = PurePath('bin')
>>> '/usr' / q
PurePosixPath('/usr/bin')
>>> p / '/an_absolute_path'
PurePosixPath('/an_absolute_path')
>>> PureWindowsPath('c:/Windows', '/Program Files')
PureWindowsPath('c:/Program Files')

```

A path object can serve anywhere an object implementing [`os.PathLike`](https://docs.python.org/3.14/library/os.html#os.PathLike) is accepted:

```python
>>> import os
>>> p = PurePath('/etc')
>>> os.fspath(p)
'/etc'

```

When rendered as a string, a path becomes the raw filesystem path on its own (in native form, with backslashes under Windows for instance); you may hand that to any function expecting a file path as a string:

```python
>>> p = PurePath('/etc')
>>> str(p)
'/etc'
>>> p = PureWindowsPath('c:/Program Files')
>>> str(p)
'c:\\Program Files'

```

In the same vein, calling [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) on a path yields the raw filesystem path as a bytes object, encoded the way [`os.fsencode()`](https://docs.python.org/3.14/library/os.html#os.fsencode) encodes it:

```python
>>> bytes(p)
b'/etc'

```

Note

Calling [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) is advised on Unix alone. On Windows, filesystem paths are canonically represented in their unicode form.

[Subject index](INDEX.md) · [Previous](general-properties.md) · [Continue](purepath-parts.md) · [Owning module, declaration or section: pathlib](pathlib-object-oriented-filesystem-paths.md)
