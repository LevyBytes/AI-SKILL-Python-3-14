# glob: `glob.translate()`

glob.translate(*pathname*, ***, *recursive=False*, *include_hidden=False*, *seps=None*)

Turn the supplied path specification into a regular expression suited for [`re.match()`](https://docs.python.org/3.14/library/re.html#re.match). That path specification may carry shell-style wildcards.

By way of illustration:

```python
>>> import glob, re
>>>
>>> regex = glob.translate('**/*.txt', recursive=True, include_hidden=True)
>>> regex
'(?s:(?:.+/)?[^/]*\\.txt)\\z'
>>> reobj = re.compile(regex)
>>> reobj.match('foo/bar/baz.txt')
<re.Match object; span=(0, 15), match='foo/bar/baz.txt'>

```

In contrast to [`fnmatch.translate()`](https://docs.python.org/3.14/library/fnmatch.html#fnmatch.translate), this function treats path separators and segments as significant. By default a wildcard does not match across path separators, and a `*` pattern segment matches exactly one path segment.

When *recursive* is true, the “`**`” pattern segment matches any quantity of path segments.

When *include_hidden* is true, wildcards are allowed to match path segments opening with a dot (`.`).

You can hand a sequence of path separators to the *seps* argument. When it is omitted, [`os.sep`](https://docs.python.org/3.14/library/os.html#os.sep) and [`altsep`](https://docs.python.org/3.14/library/os.html#os.altsep) (where available) are used.

See also

The [`pathlib.PurePath.full_match()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.PurePath.full_match) and [`pathlib.Path.glob()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.glob) methods, both of which invoke this function to carry out pattern matching and globbing.

Added in version 3.13.

[Subject index](INDEX.md) · [Previous](glob-glob-to-glob-escape.md) · [Continue](examples.md) · [Owning module, declaration or section: glob](glob-glob-to-glob-escape.md)
