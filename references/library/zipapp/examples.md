# zipapp - Examples

### Examples

Bundle a directory into an archive, then launch it.

```shell
$ python -m zipapp myapp
$ python myapp.pyz
<output from myapp>

```

You can achieve the same result through the `create_archive()` function:

```python
>>> import zipapp
>>> zipapp.create_archive('myapp', 'myapp.pyz')

```

So the application runs directly on POSIX, name an interpreter for it to use.

```shell
$ python -m zipapp myapp -p "/usr/bin/env python"
$ ./myapp.pyz
<output from myapp>

```

To swap out the shebang line of an archive that already exists, build a revised archive via the `create_archive()` function:

```python
>>> import zipapp
>>> zipapp.create_archive('old_archive.pyz', 'new_archive.pyz', '/usr/bin/python3')

```

To revise the file in place, carry out the swap in memory with a [`BytesIO`](https://docs.python.org/3.14/library/io.html#io.BytesIO) object, then write back over the source. Bear in mind that overwriting a file in place runs the risk that a failure mid-way loses the original. The snippet here guards against no such failure, though production code ought to. On top of that, this approach only holds up when the archive fits in memory:

```python
>>> import zipapp
>>> import io
>>> temp = io.BytesIO()
>>> zipapp.create_archive('myapp.pyz', temp, '/usr/bin/python2')
>>> with open('myapp.pyz', 'wb') as f:
>>>     f.write(temp.getvalue())

```

[Subject index](INDEX.md) · [Previous](zipapp-create-archive-to-zipapp-get-interpreter.md) · [Continue](specifying-the-interpreter.md) · [Owning module, declaration or section: zipapp](zipapp-manage-executable-python-zip-archives.md)
