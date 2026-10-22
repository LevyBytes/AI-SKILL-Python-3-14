# zipfile: `ZipFile.close()`, `ZipFile.getinfo()`, `ZipFile.infolist()`, `ZipFile.namelist()`, `ZipFile.open()`, `ZipFile.extract()`, `ZipFile.extractall()`, `ZipFile.printdir()`, `ZipFile.setpassword()`

ZipFile.close()

Close the archive file. Be sure to invoke `close()` prior to your program exiting, or vital records won't get written out.

 ZipFile.getinfo(*name*)

Hand back a `ZipInfo` object describing the archive member *name*. Invoking `getinfo()` for a name not presently held in the archive raises a [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError).

 ZipFile.infolist()

Hand back a list holding one `ZipInfo` object per archive member. When an existing archive has been opened, those objects keep the same ordering as the entries within the real on-disk ZIP file.

 ZipFile.namelist()

Give back a list naming each member of the archive.

 ZipFile.open(*name*, *mode='r'*, *pwd=None*, ***, *force_zip64=False*)

Reach a member of the archive as a binary file-like object. The *name* argument is either a file's name inside the archive or a `ZipInfo` object. If supplied, *mode* has to be `'r'` (the default) or `'w'`. The *pwd* argument, a [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) object, holds the password that decrypts encrypted ZIP files.

`open()` is also a context manager and therefore supports the [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement:

```python
with ZipFile('spam.zip') as myzip:
    with myzip.open('eggs.txt') as myfile:
        print(myfile.read())

```

Under *mode* `'r'`, the file-like object (`ZipExtFile`) is read-only and offers these methods: [`read()`](https://docs.python.org/3.14/library/io.html#io.BufferedIOBase.read), [`readline()`](https://docs.python.org/3.14/library/io.html#io.IOBase.readline), [`readlines()`](https://docs.python.org/3.14/library/io.html#io.IOBase.readlines), [`seek()`](https://docs.python.org/3.14/library/io.html#io.IOBase.seek), [`tell()`](https://docs.python.org/3.14/library/io.html#io.IOBase.tell), [`__iter__()`](https://docs.python.org/3.14/library/stdtypes.html#container.__iter__), [`__next__()`](https://docs.python.org/3.14/library/stdtypes.html#iterator.__next__). Such objects function on their own, separately from the ZipFile.

Under `mode='w'`, a writable file handle comes back, and it supports the [`write()`](https://docs.python.org/3.14/library/io.html#io.BufferedIOBase.write) method. As long as that writable handle stays open, any attempt to read from or write to other files inside the ZIP file raises a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError).

Either way, the file-like object additionally carries the attributes `name`, matching the name of a file inside the archive, and `mode`, which is `'rb'` or `'wb'` according to the input mode.

While writing a file, when its size isn't known up front but might top 2 GiB, supply `force_zip64=True` so the header format can accommodate large files. When the size is known up front, build a `ZipInfo` object whose `file_size` is set and feed that as the *name* parameter.

Note

A filename or a `ZipInfo` object can be handed to the `open()`, `read()`, and `extract()` methods. This proves handy whenever you read a ZIP file holding members whose names collide.

Changed in version 3.6: Dropped `mode='U'`. To read compressed text files in [universal newlines](https://docs.python.org/3.14/glossary.html#term-universal-newlines) mode, reach for [`io.TextIOWrapper`](https://docs.python.org/3.14/library/io.html#io.TextIOWrapper) instead.

Changed in version 3.6: With the `mode='w'` option, `ZipFile.open()` is now able to write files into the archive.

Changed in version 3.6: Invoking `open()` against a closed ZipFile now produces a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError); formerly the result was a [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError).

Changed in version 3.13: The writeable file-like object gained `name` and `mode` attributes. For the readable file-like object, the `mode` attribute's value shifted from `'r'` to `'rb'`.

 ZipFile.extract(*member*, *path=None*, *pwd=None*)

Pull a member out of the archive into the current working directory; *member* has to be its complete name or a `ZipInfo` object. Its file metadata is reproduced as faithfully as it can be. A different target directory is chosen via *path*. The *member* value may be a filename or a `ZipInfo` object. The *pwd* argument, a [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) object, supplies the password for encrypted files.

Returns the normalized path created (a directory or new file).

Note

When a member filename is an absolute path, any drive/UNC sharepoint plus leading (back)slashes get removed — for instance, `///foo/bar` turns into `foo/bar` on Unix and `C:\foo\bar` turns into `foo\bar` on Windows. Every `".."` segment in a member filename is also dropped — for instance, `../../foo../../ba..r` turns into `foo../ba..r`. On Windows the illegal characters (`:`, `<`, `>`, `|`, `"`, `?`, and `*`) become an underscore (`_`).

Changed in version 3.6: Running `extract()` on a closed ZipFile now yields a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError); in earlier versions it gave a [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError).

Changed in version 3.6.2: The *path* parameter accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

 ZipFile.extractall(*path=None*, *members=None*, *pwd=None*)

Pull every member out of the archive into the current working directory. A different target directory is chosen via *path*. The *members* argument is optional and has to be a subset of whatever `namelist()` returns. The *pwd* argument, a [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) object, supplies the password for encrypted files.

Warning

Don't ever extract archives originating from untrusted sources unless you've inspected them beforehand. Files may end up created outside *path* — for example, through members carrying absolute filenames or filenames containing “..” segments. The module tries to block this. Refer to the `extract()` note.

Changed in version 3.6: Using `extractall()` on a closed ZipFile now surfaces a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError); the prior behavior was a [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError).

Changed in version 3.6.2: The *path* parameter accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

 ZipFile.printdir()

Write the archive's table of contents out to `sys.stdout`.

 ZipFile.setpassword(*pwd*)

Make *pwd* (a [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) object) the default password applied when extracting encrypted files.

[Subject index](INDEX.md) · [Previous](zipfile-zipfile-class.md) · [Continue](zipfile-read-to-zipfile-comment.md) · [Owning module, declaration or section: zipfile](zipfile-badzipfile-to-zipfile-largezipfile.md) · [Owning module, declaration or section: zipfile.ZipFile](zipfile-zipfile-class.md) · [Owning module, declaration or section: ZipFile objects](zipfile-zipfile-class.md)
