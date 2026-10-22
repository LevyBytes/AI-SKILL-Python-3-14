# pathlib — Parsing and generating URIs

Certain concrete path methods may raise an [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) when a system call fails (say, because the path is absent).

### Parsing and generating URIs

Concrete path objects can be built from, and rendered as, 'file' URIs that conform to [**RFC 8089**](https://datatracker.ietf.org/doc/html/rfc8089.html).

Note

File URIs do not carry across machines whose [filesystem encodings](https://docs.python.org/3.14/library/os.html#filesystem-encoding) differ.

 *classmethod *Path.from_uri(*uri*)

Build a new path object by parsing a 'file' URI. As an example:

```python
>>> p = Path.from_uri('file:///etc/hosts')
PosixPath('/etc/hosts')

```

Under Windows, DOS device and UNC paths can be parsed out of URIs:

```python
>>> p = Path.from_uri('file:///c:/windows')
WindowsPath('c:/windows')
>>> p = Path.from_uri('file://server/share')
WindowsPath('//server/share')

```

A number of alternative forms work too:

```python
>>> p = Path.from_uri('file:////server/share')
WindowsPath('//server/share')
>>> p = Path.from_uri('file://///server/share')
WindowsPath('//server/share')
>>> p = Path.from_uri('file:c:/windows')
WindowsPath('c:/windows')
>>> p = Path.from_uri('file:/c|/windows')
WindowsPath('c:/windows')

```

[`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) gets raised when the URI fails to begin with `file:`, or when the parsed path is not absolute.

Added in version 3.13.

Changed in version 3.14: The URL authority is dropped when it matches the local hostname. Failing that, when the authority is neither empty nor `localhost`, a UNC path comes back on Windows (as it did before), whereas on other platforms a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised.

 Path.as_uri()

Render the path as a 'file' URI. [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) gets raised when the path is not absolute.

```pycon
>>> p = PosixPath('/etc/passwd')
>>> p.as_uri()
'file:///etc/passwd'
>>> p = WindowsPath('c:/Windows')
>>> p.as_uri()
'file:///c:/Windows'

```

Deprecated since version 3.14, will be removed in version 3.19: Invoking this method on `PurePath` rather than `Path` works but is deprecated. Because the method draws on [`os.fsencode()`](https://docs.python.org/3.14/library/os.html#os.fsencode), it is strictly impure.

[Subject index](INDEX.md) · [Continue](path-expanduser-to-path-resolve.md) · [Owning module, declaration or section: pathlib](pathlib-object-oriented-filesystem-paths.md) · [Owning module, declaration or section: Concrete path operations and OSError handling](pathlib-path-class.md) · [Preceding source contract and version conditions](pathlib-windowspath-class.md)
