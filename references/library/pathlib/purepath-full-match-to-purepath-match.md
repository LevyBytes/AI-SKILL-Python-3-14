# pathlib: `PurePath.full_match()`, `PurePath.match()`

PurePath.full_match(*pattern*, ***, *case_sensitive=None*)

Match this path against the supplied glob-style pattern. Return `True` when the match succeeds, otherwise `False`. As an example:

```python
>>> PurePath('a/b.py').full_match('a/*.py')
True
>>> PurePath('a/b.py').full_match('*.py')
False
>>> PurePath('/a/b/c.py').full_match('/a/**')
True
>>> PurePath('/a/b/c.py').full_match('**/*.py')
True

```

See also

Pattern language documentation.

Just as with other methods, case-sensitivity tracks the platform defaults:

```python
>>> PurePosixPath('b.py').full_match('*.PY')
False
>>> PureWindowsPath('b.py').full_match('*.PY')
True

```

Set *case_sensitive* to `True` or `False` to override that behaviour.

Added in version 3.13.

 PurePath.match(*pattern*, ***, *case_sensitive=None*)

Match this path against the supplied non-recursive glob-style pattern. Return `True` when the match succeeds, otherwise `False`.

This method resembles `full_match()`, except that empty patterns are disallowed ([`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised), the recursive wildcard "`**`" is unsupported (it behaves like the non-recursive "`*`"), and when a relative pattern is supplied, matching proceeds from the right:

```python
>>> PurePath('a/b.py').match('*.py')
True
>>> PurePath('/a/b/c.py').match('b/*.py')
True
>>> PurePath('/a/b/c.py').match('a/*.py')
False

```

Changed in version 3.12: The *pattern* parameter accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

Changed in version 3.12: The *case_sensitive* parameter was added.

[Subject index](INDEX.md) · [Previous](purepath-is-absolute-to-purepath-joinpath.md) · [Continue](purepath-relative-to-to-purepath-with-stem.md) · [Owning module, declaration or section: pathlib](pathlib-object-oriented-filesystem-paths.md) · [Owning module, declaration or section: Methods and properties](purepath-parser-to-purepath-root.md)
