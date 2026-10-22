# pathlib: `pathlib.WindowsPath`

*class *pathlib.WindowsPath(**pathsegments*)

A subclass of `Path` and `PureWindowsPath`, this class stands for concrete Windows filesystem paths:

```python
>>> WindowsPath('c:/', 'Users', 'Ximénez')
WindowsPath('c:/Users/Ximénez')

```

*pathsegments* is specified similarly to `PurePath`.

Changed in version 3.13: Raises `UnsupportedOperation` on non-Windows platforms. In earlier versions, [`NotImplementedError`](https://docs.python.org/3.14/library/exceptions.html#NotImplementedError) was raised instead.

You may only instantiate the class flavour matching your system (permitting system calls on non-compatible path flavours could spawn bugs or failures in your application):

```python
>>> import os
>>> os.name
'posix'
>>> Path('setup.py')
PosixPath('setup.py')
>>> PosixPath('setup.py')
PosixPath('setup.py')
>>> WindowsPath('setup.py')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "pathlib.py", line 798, in __new__
    % (cls.__name__,))
UnsupportedOperation: cannot instantiate 'WindowsPath' on your system

```

[Subject index](INDEX.md) · [Previous](pathlib-posixpath-class.md) · [Owning module, declaration or section: pathlib](pathlib-object-oriented-filesystem-paths.md) · [Owning module, declaration or section: Concrete paths](pathlib-path-class.md) · [Required continuation of the source contract](path-as-uri.md)
