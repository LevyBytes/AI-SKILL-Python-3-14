# pathlib: `PurePath.with_suffix()`, `PurePath.with_segments()`

PurePath.with_suffix(*suffix*)

Return a new path with the `suffix` changed. When the original path has no suffix, the new *suffix* gets appended instead. When the *suffix* is an empty string, the original suffix gets removed:

```python
>>> p = PureWindowsPath('c:/Downloads/pathlib.tar.gz')
>>> p.with_suffix('.bz2')
PureWindowsPath('c:/Downloads/pathlib.tar.bz2')
>>> p = PureWindowsPath('README')
>>> p.with_suffix('.txt')
PureWindowsPath('README.txt')
>>> p = PureWindowsPath('README.txt')
>>> p.with_suffix('')
PureWindowsPath('README')

```

Changed in version 3.14: A lone dot (”`.`”) now counts as a valid suffix. In earlier versions, [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised when a single dot is supplied.

 PurePath.with_segments(**pathsegments*)

Construct, by combining the given *pathsegments*, a fresh path object that shares this type. Whenever a derivative path is built, such as from `parent` and `relative_to()`, this method gets invoked. Subclasses may override it so they can pass information to derivative paths, for instance:

```python
from pathlib import PurePosixPath

class MyPath(PurePosixPath):
    def __init__(self, *pathsegments, session_id):
        super().__init__(*pathsegments)
        self.session_id = session_id

    def with_segments(self, *pathsegments):
        return type(self)(*pathsegments, session_id=self.session_id)

etc = MyPath('/etc', session_id=42)
hosts = etc / 'hosts'
print(hosts.session_id)  # 42

```

Added in version 3.12.

[Subject index](INDEX.md) · [Previous](purepath-relative-to-to-purepath-with-stem.md) · [Continue](pathlib-path-class.md) · [Owning module, declaration or section: pathlib](pathlib-object-oriented-filesystem-paths.md) · [Owning module, declaration or section: Methods and properties](purepath-parser-to-purepath-root.md)
