# pathlib: `pathlib.Path`

### Concrete paths

Concrete paths are subclasses of the pure path classes. On top of the operations the latter supply, they additionally supply methods to perform system calls on path objects. Concrete paths can be instantiated in three ways:

 *class *pathlib.Path(**pathsegments*)

A subclass of `PurePath`, this class stands for concrete paths of the system's path flavour (instantiating it yields either a `PosixPath` or a `WindowsPath`):

```python
>>> Path('setup.py')
PosixPath('setup.py')

```

*pathsegments* is specified similarly to `PurePath`.

[Subject index](INDEX.md) · [Previous](purepath-with-suffix-to-purepath-with-segments.md) · [Continue](pathlib-posixpath-class.md) · [Owning module, declaration or section: pathlib](pathlib-object-oriented-filesystem-paths.md)
