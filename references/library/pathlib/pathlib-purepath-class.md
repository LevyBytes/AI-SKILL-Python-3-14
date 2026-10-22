# pathlib: `pathlib.PurePath`

### Pure paths

Pure path objects offer path-handling operations that never actually touch a filesystem. These classes can be reached in three ways, which we also term *flavours*:

 *class *pathlib.PurePath(**pathsegments*)

A generic class standing for the system's path flavour (instantiating it yields either a `PurePosixPath` or a `PureWindowsPath`):

```python
>>> PurePath('setup.py')      # Running on a Unix machine
PurePosixPath('setup.py')

```

Every element of *pathsegments* may be either a string standing for a path segment, or an object implementing the [`os.PathLike`](https://docs.python.org/3.14/library/os.html#os.PathLike) interface whose [`__fspath__()`](https://docs.python.org/3.14/library/os.html#os.PathLike.__fspath__) method returns a string, such as another path object:

```python
>>> PurePath('foo', 'some/path', 'bar')
PurePosixPath('foo/some/path/bar')
>>> PurePath(Path('foo'), Path('bar'))
PurePosixPath('foo/bar')

```

Where *pathsegments* is empty, the current directory is taken:

```python
>>> PurePath()
PurePosixPath('.')

```

Should a segment be an absolute path, every earlier segment is dropped (much like [`os.path.join()`](https://docs.python.org/3.14/library/os.path.html#os.path.join)):

```python
>>> PurePath('/etc', '/usr', 'lib64')
PurePosixPath('/usr/lib64')
>>> PureWindowsPath('c:/Windows', 'd:bar')
PureWindowsPath('d:bar')

```

On Windows, the drive does not reset upon meeting a rooted relative path segment (such as `r'\foo'`):

```python
>>> PureWindowsPath('c:/Windows', '/Program Files')
PureWindowsPath('c:/Program Files')

```

Spurious slashes and single dots get collapsed, while double dots (`'..'`) and leading double slashes (`'//'`) do not, since doing so would alter the meaning of a path for several reasons (such as symbolic links, UNC paths):

```python
>>> PurePath('foo//bar')
PurePosixPath('foo/bar')
>>> PurePath('//foo/bar')
PurePosixPath('//foo/bar')
>>> PurePath('foo/./bar')
PurePosixPath('foo/bar')
>>> PurePath('foo/../bar')
PurePosixPath('foo/../bar')

```

(a naïve approach would treat `PurePosixPath('foo/../bar')` as the same as `PurePosixPath('bar')`, which is wrong when `foo` is a symbolic link to another directory)

Pure path objects implement the [`os.PathLike`](https://docs.python.org/3.14/library/os.html#os.PathLike) interface, so they can be used anywhere that interface is accepted.

Changed in version 3.6: Added support for the [`os.PathLike`](https://docs.python.org/3.14/library/os.html#os.PathLike) interface.

[Subject index](INDEX.md) · [Previous](pathlib-unsupportedoperation.md) · [Continue](pathlib-pureposixpath-class.md) · [Owning module, declaration or section: pathlib](pathlib-object-oriented-filesystem-paths.md)
