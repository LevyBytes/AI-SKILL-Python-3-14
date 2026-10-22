# pathlib: `Path.rglob()`

Path.rglob(*pattern*, ***, *case_sensitive=None*, *recurse_symlinks=False*)

Glob the given relative *pattern* recursively. This amounts to calling `Path.glob()` with "`**/`" prepended to the *pattern*.

Note

The paths come back in no particular order. When you need a specific order, sort the results.

Note

Every [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) exception arising from the filesystem scan gets suppressed. That covers [`PermissionError`](https://docs.python.org/3.14/library/exceptions.html#PermissionError) when reaching directories without read permission.

See also

Pattern language and `Path.glob()` documentation.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `pathlib.Path.rglob` with arguments `self`, `pattern`.

Changed in version 3.12: The *case_sensitive* parameter was added.

Changed in version 3.13: The *recurse_symlinks* parameter was added.

Changed in version 3.13: The *pattern* parameter accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

[Subject index](INDEX.md) · [Previous](path-iterdir-to-path-glob.md) · [Continue](path-walk.md) · [Owning module, declaration or section: pathlib](pathlib-object-oriented-filesystem-paths.md) · [Owning module, declaration or section: Reading directories](path-iterdir-to-path-glob.md)
