# zipfile - PyZipFile objects

writepy(*pathname*, *basename=''*, *filterfunc=None*)

Search for files `*.py` and add the corresponding file to the archive.

Where the *optimize* parameter to `PyZipFile` was either omitted or `-1`, the matching file is a `*.pyc` file, compiled where needed.

Where the *optimize* parameter to `PyZipFile` was `0`, `1` or `2`, only files at that optimization level (refer to [`compile()`](https://docs.python.org/3.14/library/functions.html#compile)) join the archive, compiled where needed.

Where *pathname* points to a file, its filename has to close with `.py`, and just the (matching `*.pyc`) file lands at the top level (carrying no path information). Where *pathname* points to a file not closing with `.py`, a [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError) gets raised. Where it points to a directory that is not a package directory, then every one of the files `*.pyc` lands at the top level. Where the directory is a package directory, then all `*.pyc` land beneath the package name as a file path, and should any subdirectories themselves be package directories, all of those get added recursively in sorted order.

*basename* is intended for internal use only.

*filterfunc*, where given, has to be a function accepting a single string argument. It receives each path (each individual full file path included) ahead of that path joining the archive. Where *filterfunc* returns a false value, the path stays out, and where it points to a directory its contents get disregarded. As an example, where our test files all sit either within `test` directories or open with the string `test_`, we can apply a *filterfunc* to leave them out:

```python
>>> zf = PyZipFile('myprog.zip')
>>> def notests(s):
...     fn = os.path.basename(s)
...     return (not (fn == 'test' or fn.startswith('test_')))
...
>>> zf.writepy('myprog', filterfunc=notests)

```

The `writepy()` method produces archives whose file names look like this:

```python
string.pyc                   # Top level name
test/__init__.pyc            # Package directory
test/testall.pyc             # Module test.testall
test/bogus/__init__.pyc      # Subpackage directory
test/bogus/myfile.pyc        # Submodule test.bogus.myfile

```

Changed in version 3.4: Added the *filterfunc* parameter.

Changed in version 3.6.2: The *pathname* parameter accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

Changed in version 3.7: Recursion sorts directory entries.

[Subject index](INDEX.md) · [Previous](zipfile-pyzipfile-class.md) · [Continue](zipinfo-is-dir-to-zipinfo-extract-version.md) · [Owning module, declaration or section: zipfile](zipfile-badzipfile-to-zipfile-largezipfile.md) · [Owning module, declaration or section: zipfile.PyZipFile](zipfile-pyzipfile-class.md) · [Owning module, declaration or section: PyZipFile objects](zipfile-pyzipfile-class.md)
