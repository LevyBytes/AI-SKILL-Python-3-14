# pathlib: `pathlib.PosixPath`

*class *pathlib.PosixPath(**pathsegments*)

A subclass of `Path` and `PurePosixPath`, this class stands for concrete non-Windows filesystem paths:

```python
>>> PosixPath('/etc/hosts')
PosixPath('/etc/hosts')

```

*pathsegments* is specified similarly to `PurePath`.

Changed in version 3.13: Raises `UnsupportedOperation` on Windows. In earlier versions, [`NotImplementedError`](https://docs.python.org/3.14/library/exceptions.html#NotImplementedError) was raised instead.

[Subject index](INDEX.md) · [Previous](pathlib-path-class.md) · [Continue](pathlib-windowspath-class.md) · [Owning module, declaration or section: pathlib](pathlib-object-oriented-filesystem-paths.md) · [Owning module, declaration or section: Concrete paths](pathlib-path-class.md)
