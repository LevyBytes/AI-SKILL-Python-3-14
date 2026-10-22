# pathlib: `PurePath.name`, `PurePath.suffix`, `PurePath.suffixes`, `PurePath.stem`, `PurePath.as_posix()`

PurePath.name

A string standing for the last path component, leaving out the drive and root, where any exist:

```python
>>> PurePosixPath('my/library/setup.py').name
'setup.py'

```

UNC drive names are left out of account:

```python
>>> PureWindowsPath('//some/share/setup.py').name
'setup.py'
>>> PureWindowsPath('//some/share').name
''

```

 PurePath.suffix

The last dot-separated portion of the final component, where one exists:

```python
>>> PurePosixPath('my/library/setup.py').suffix
'.py'
>>> PurePosixPath('my/library.tar.gz').suffix
'.gz'
>>> PurePosixPath('my/library').suffix
''

```

This usually goes by the name file extension.

Changed in version 3.14: A lone dot (”`.`”) now counts as a valid suffix.

 PurePath.suffixes

A list of the path's suffixes, frequently termed file extensions:

```python
>>> PurePosixPath('my/library.tar.gar').suffixes
['.tar', '.gar']
>>> PurePosixPath('my/library.tar.gz').suffixes
['.tar', '.gz']
>>> PurePosixPath('my/library').suffixes
[]

```

Changed in version 3.14: A lone dot (”`.`”) now counts as a valid suffix.

 PurePath.stem

The final path component, stripped of its suffix:

```python
>>> PurePosixPath('my/library.tar.gz').stem
'library.tar'
>>> PurePosixPath('my/library.tar').stem
'library'
>>> PurePosixPath('my/library').stem
'library'

```

Changed in version 3.14: A lone dot (”`.`”) now counts as a valid suffix.

 PurePath.as_posix()

Return a string form of the path using forward slashes (`/`):

```python
>>> p = PureWindowsPath('c:\\windows')
>>> str(p)
'c:\\windows'
>>> p.as_posix()
'c:/windows'

```

[Subject index](INDEX.md) · [Previous](purepath-anchor-to-purepath-parent.md) · [Continue](purepath-is-absolute-to-purepath-joinpath.md) · [Owning module, declaration or section: pathlib](pathlib-object-oriented-filesystem-paths.md) · [Owning module, declaration or section: Methods and properties](purepath-parser-to-purepath-root.md)
