# pathlib: `PurePath.anchor`, `PurePath.parents`, `PurePath.parent`

PurePath.anchor

The drive and root joined together:

```python
>>> PureWindowsPath('c:/Program Files/').anchor
'c:\\'
>>> PureWindowsPath('c:Program Files/').anchor
'c:'
>>> PurePosixPath('/etc').anchor
'/'
>>> PureWindowsPath('//host/share').anchor
'\\\\host\\share\\'

```

 PurePath.parents

An immutable sequence granting access to the logical ancestors of the path:

```python
>>> p = PureWindowsPath('c:/foo/bar/setup.py')
>>> p.parents[0]
PureWindowsPath('c:/foo/bar')
>>> p.parents[1]
PureWindowsPath('c:/foo')
>>> p.parents[2]
PureWindowsPath('c:/')

```

Changed in version 3.10: The parents sequence gained support for [slices](https://docs.python.org/3.14/glossary.html#term-slice) along with negative index values.

 PurePath.parent

The logical parent of the path:

```python
>>> p = PurePosixPath('/a/b/c/d')
>>> p.parent
PurePosixPath('/a/b/c')

```

You cannot move past an anchor, or an empty path:

```python
>>> p = PurePosixPath('/')
>>> p.parent
PurePosixPath('/')
>>> p = PurePosixPath('.')
>>> p.parent
PurePosixPath('.')

```

Note

This is a purely lexical operation, which is why the behaviour below results:

```python
>>> p = PurePosixPath('foo/..')
>>> p.parent
PurePosixPath('foo')

```

When you want to walk an arbitrary filesystem path upwards, it is best to call `Path.resolve()` first so that symlinks are resolved and `".."` components are removed.

[Subject index](INDEX.md) · [Previous](purepath-parser-to-purepath-root.md) · [Continue](purepath-name-to-purepath-as-posix.md) · [Owning module, declaration or section: pathlib](pathlib-object-oriented-filesystem-paths.md) · [Owning module, declaration or section: Methods and properties](purepath-parser-to-purepath-root.md)
