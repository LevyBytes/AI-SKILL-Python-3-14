# pathlib — General properties

### General properties

Paths are immutable and [hashable](https://docs.python.org/3.14/glossary.html#term-hashable). Paths sharing a flavour are comparable and orderable. These properties honor the flavour's case-folding semantics:

```python
>>> PurePosixPath('foo') == PurePosixPath('FOO')
False
>>> PureWindowsPath('foo') == PureWindowsPath('FOO')
True
>>> PureWindowsPath('FOO') in { PureWindowsPath('foo') }
True
>>> PureWindowsPath('C:') < PureWindowsPath('d:')
True

```

Paths of differing flavours compare unequal and resist ordering:

```python
>>> PureWindowsPath('foo') == PurePosixPath('foo')
False
>>> PureWindowsPath('foo') < PurePosixPath('foo')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '<' not supported between instances of 'PureWindowsPath' and 'PurePosixPath'

```

[Subject index](INDEX.md) · [Previous](pathlib-purewindowspath-class.md) · [Continue](operators.md) · [Owning module, declaration or section: pathlib](pathlib-object-oriented-filesystem-paths.md)
