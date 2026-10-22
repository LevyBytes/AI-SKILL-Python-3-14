# pathlib: `PurePath.relative_to()`, `PurePath.with_name()`, `PurePath.with_stem()`

PurePath.relative_to(*other*, *walk_up=False*)

Work out a version of this path relative to the path that *other* stands for. When that proves impossible, [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised:

```python
>>> p = PurePosixPath('/etc/passwd')
>>> p.relative_to('/')
PurePosixPath('etc/passwd')
>>> p.relative_to('/etc')
PurePosixPath('passwd')
>>> p.relative_to('/usr')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "pathlib.py", line 941, in relative_to
    raise ValueError(error_message.format(str(self), str(formatted)))
ValueError: '/etc/passwd' is not in the subpath of '/usr' OR one path is relative and the other is absolute.

```

Where *walk_up* is false (the default), the path has to start with *other*. Where the argument is true, `..` entries may get added to form the relative path. In every other case, such as paths referencing different drives, [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised.:

```python
>>> p.relative_to('/usr', walk_up=True)
PurePosixPath('../etc/passwd')
>>> p.relative_to('foo', walk_up=True)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "pathlib.py", line 941, in relative_to
    raise ValueError(error_message.format(str(self), str(formatted)))
ValueError: '/etc/passwd' is not on the same drive as 'foo' OR one path is relative and the other is absolute.

```

Warning

This function belongs to `PurePath` and operates on strings. It neither checks nor touches the underlying file structure. That can affect the *walk_up* option, since it presumes no symlinks sit in the path; call `resolve()` first where needed to resolve symlinks.

Changed in version 3.12: The *walk_up* parameter was added (the old behavior matches `walk_up=False`).

Deprecated since version 3.12, removed in version 3.14: Supplying extra positional arguments is deprecated; when given, they get joined with *other*.

 PurePath.with_name(*name*)

Return a new path with the `name` changed. When the original path has no name, ValueError is raised:

```python
>>> p = PureWindowsPath('c:/Downloads/pathlib.tar.gz')
>>> p.with_name('setup.py')
PureWindowsPath('c:/Downloads/setup.py')
>>> p = PureWindowsPath('c:/')
>>> p.with_name('setup.py')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/antoine/cpython/default/Lib/pathlib.py", line 751, in with_name
    raise ValueError("%r has an empty name" % (self,))
ValueError: PureWindowsPath('c:/') has an empty name

```

 PurePath.with_stem(*stem*)

Return a new path with the `stem` changed. When the original path has no name, ValueError is raised:

```python
>>> p = PureWindowsPath('c:/Downloads/draft.txt')
>>> p.with_stem('final')
PureWindowsPath('c:/Downloads/final.txt')
>>> p = PureWindowsPath('c:/Downloads/pathlib.tar.gz')
>>> p.with_stem('lib')
PureWindowsPath('c:/Downloads/lib.gz')
>>> p = PureWindowsPath('c:/')
>>> p.with_stem('')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/antoine/cpython/default/Lib/pathlib.py", line 861, in with_stem
    return self.with_name(stem + self.suffix)
  File "/home/antoine/cpython/default/Lib/pathlib.py", line 851, in with_name
    raise ValueError("%r has an empty name" % (self,))
ValueError: PureWindowsPath('c:/') has an empty name

```

Added in version 3.9.

[Subject index](INDEX.md) · [Previous](purepath-full-match-to-purepath-match.md) · [Continue](purepath-with-suffix-to-purepath-with-segments.md) · [Owning module, declaration or section: pathlib](pathlib-object-oriented-filesystem-paths.md) · [Owning module, declaration or section: Methods and properties](purepath-parser-to-purepath-root.md)
