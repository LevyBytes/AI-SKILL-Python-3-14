# Unicode filenames

### Unicode filenames

Nearly every operating system in widespread use these days allows filenames built from any Unicode characters. Typically this works by turning the Unicode string into an encoding that differs from one system to the next. These days Python is settling on UTF-8: on MacOS it has relied on UTF-8 across several releases, and with Python 3.6 it moved to UTF-8 on Windows too. Under Unix, a [filesystem encoding](https://docs.python.org/3.14/glossary.html#term-filesystem-encoding-and-error-handler). exists only when you have set the `LANG` or `LC_CTYPE` environment variables; absent those, the encoding once more defaults to UTF-8.

The [`sys.getfilesystemencoding()`](https://docs.python.org/3.14/library/sys.html#sys.getfilesystemencoding) function reports which encoding applies on the machine you’re running, should you wish to encode by hand, though there’s rarely cause to. For opening a file to read or write, you can ordinarily hand the Unicode string straight in as the filename and it gets converted to the proper encoding on your behalf:

```python
filename = 'filename\u4500abc'
with open(filename, 'w') as f:
    f.write('blah\n')

```

The [`os`](https://docs.python.org/3.14/library/os.html#module-os) module’s functions, [`os.stat()`](https://docs.python.org/3.14/library/os.html#os.stat) being one, take Unicode filenames as well.

Because the [`os.listdir()`](https://docs.python.org/3.14/library/os.html#os.listdir) function hands back filenames, a question comes up: ought it to give the Unicode form of the filenames, or bytes holding the encoded form? `os.listdir()` is capable of either, the choice hinging on whether you handed the directory path in as bytes or as a Unicode string. Supply a Unicode string for the path and the filenames get decoded with the filesystem’s encoding so a list of Unicode strings comes back; supply a byte path and the filenames come back as bytes. Suppose, for instance, that the default [filesystem encoding](https://docs.python.org/3.14/glossary.html#term-filesystem-encoding-and-error-handler) is UTF-8 and you run this program:

```python
fn = 'filename\u4500abc'
f = open(fn, 'w')
f.close()

import os
print(os.listdir(b'.'))
print(os.listdir('.'))

```

you'll get this as the result:

```shell
$ python listdir-test.py
[b'filename\xe4\x94\x80abc', ...]
['filename\u4500abc', ...]

```

UTF-8-encoded filenames fill the first list, while the Unicode forms fill the second.

Bear in mind that in the great majority of cases you can simply stay with Unicode across these APIs. Reserve the bytes APIs for systems that may hold undecodable file names — which today amounts to little more than Unix systems.

[Subject index](INDEX.md) · [Previous source context](reading-and-writing-unicode-data-continuation.md) · [Following source context](tips-for-writing-unicode-aware-programs.md)
