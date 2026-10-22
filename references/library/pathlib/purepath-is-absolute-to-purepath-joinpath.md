# pathlib: `PurePath.is_absolute()`, `PurePath.is_relative_to()`, `PurePath.is_reserved()`, `PurePath.joinpath()`

PurePath.is_absolute()

Return whether or not the path is absolute. A path counts as absolute once it carries both a root and (where the flavour permits) a drive:

```python
>>> PurePosixPath('/a/b').is_absolute()
True
>>> PurePosixPath('a/b').is_absolute()
False

>>> PureWindowsPath('c:/a/b').is_absolute()
True
>>> PureWindowsPath('/a/b').is_absolute()
False
>>> PureWindowsPath('c:').is_absolute()
False
>>> PureWindowsPath('//some/share').is_absolute()
True

```

 PurePath.is_relative_to(*other*)

Return whether or not this path is relative to the *other* path.

```python
>>> p = PurePath('/etc/passwd')
>>> p.is_relative_to('/etc')
True
>>> p.is_relative_to('/usr')
False

```

This method works on strings; it neither touches the filesystem nor handles "`..`" segments in any special way. The code below is equivalent:

```python
>>> u = PurePath('/usr')
>>> u == p or u in p.parents
False

```

Added in version 3.9.

Deprecated since version 3.12, removed in version 3.14: Supplying extra arguments is deprecated; when given, they get joined with *other*.

 PurePath.is_reserved()

With `PureWindowsPath`, return `True` when the path counts as reserved under Windows, otherwise `False`. With `PurePosixPath`, `False` always comes back.

Changed in version 3.13: Windows path names holding a colon, or ending with a dot or a space, count as reserved. UNC paths may be reserved.

Deprecated since version 3.13, will be removed in version 3.15: Treat this method as deprecated; rely on [`os.path.isreserved()`](https://docs.python.org/3.14/library/os.path.html#os.path.isreserved) to detect reserved paths on Windows.

 PurePath.joinpath(**pathsegments*)

Invoking this method amounts to combining the path with each of the given *pathsegments* one after another:

```python
>>> PurePosixPath('/etc').joinpath('passwd')
PurePosixPath('/etc/passwd')
>>> PurePosixPath('/etc').joinpath(PurePosixPath('passwd'))
PurePosixPath('/etc/passwd')
>>> PurePosixPath('/etc').joinpath('init.d', 'apache2')
PurePosixPath('/etc/init.d/apache2')
>>> PureWindowsPath('c:').joinpath('/Program Files')
PureWindowsPath('c:/Program Files')

```

[Subject index](INDEX.md) · [Previous](purepath-name-to-purepath-as-posix.md) · [Continue](purepath-full-match-to-purepath-match.md) · [Owning module, declaration or section: pathlib](pathlib-object-oriented-filesystem-paths.md) · [Owning module, declaration or section: Methods and properties](purepath-parser-to-purepath-root.md)
