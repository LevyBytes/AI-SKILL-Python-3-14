# pathlib: `pathlib.PureWindowsPath`

*class *pathlib.PureWindowsPath(**pathsegments*)

A subclass of `PurePath`, this path flavour stands for Windows filesystem paths, [UNC paths](https://en.wikipedia.org/wiki/Path_(computing)#UNC) included:

```python
>>> PureWindowsPath('c:/', 'Users', 'Ximénez')
PureWindowsPath('c:/Users/Ximénez')
>>> PureWindowsPath('//server/share/file')
PureWindowsPath('//server/share/file')

```

*pathsegments* is specified similarly to `PurePath`.

No matter which system you run on, all of these classes can be instantiated, because none of them offers any operation that performs system calls.

[Subject index](INDEX.md) · [Previous](pathlib-pureposixpath-class.md) · [Continue](general-properties.md) · [Owning module, declaration or section: pathlib](pathlib-object-oriented-filesystem-paths.md) · [Owning module, declaration or section: Pure paths](pathlib-purepath-class.md)
