# tempfile - Deprecated functions and variables

### Deprecated functions and variables

One old approach to making temporary files was to first conjure a file name via the `mktemp()` function, then create a file under that name. Sadly that is insecure: in the gap between the `mktemp()` call and the first process's later attempt to create the file, some other process could create a file bearing the same name. The fix is to fold the two steps together and create the file at once. That is exactly what `mkstemp()` and the other functions covered above do.

 tempfile.mktemp(*suffix=''*, *prefix='tmp'*, *dir=None*)

Deprecated since version 2.3: Use `mkstemp()` instead.

Hands back an absolute pathname for a file that was absent at the moment the call ran. Its *prefix*, *suffix*, and *dir* arguments resemble those of `mkstemp()`, with the difference that bytes file names, `suffix=None` and `prefix=None` get no support here.

Warning

Calling this function may open a security hole in your code. In the interval before you actually do anything with the name it returns, someone else might slip in ahead of you. You can swap out `mktemp()` painlessly for `NamedTemporaryFile()`, handing it the `delete=False` parameter:

```python
>>> f = NamedTemporaryFile(delete=False)
>>> f.name
'/tmp/tmptjujjt'
>>> f.write(b"Hello World!\n")
13
>>> f.close()
>>> os.unlink(f.name)
>>> os.path.exists(f.name)
False

```

[Subject index](INDEX.md) · [Previous](examples.md) · [Owning module, declaration or section: tempfile](tempfile-generate-temporary-files-and-directories.md)
