# What's New In Python 3.2 / tarfile — tarfile

### tarfile

You can now employ the [`TarFile`](https://docs.python.org/3.14/library/tarfile.html#tarfile.TarFile) class as a context manager. Its [`add()`](https://docs.python.org/3.14/library/tarfile.html#tarfile.TarFile.add) method also gained a *filter* option, which governs which files land in the archive and lets the file metadata be modified.

That new *filter* option supersedes the older and less capable *exclude* parameter, now deprecated. When given, the optional *filter* parameter must be passed as a [keyword argument](https://docs.python.org/3.14/glossary.html#term-keyword-argument). Your supplied filter function receives a [`TarInfo`](https://docs.python.org/3.14/library/tarfile.html#tarfile.TarInfo) object and hands back a revised `TarInfo` object; alternatively, to leave a file out, the function may return `None`:

```python
>>> import tarfile, glob

>>> def myfilter(tarinfo):
...     if tarinfo.isfile():             # only save real files
...         tarinfo.uname = 'monty'      # redact the user name
...         return tarinfo

>>> with tarfile.open(name='myarchive.tar.gz', mode='w:gz') as tf:
...     for filename in glob.glob('*.txt'):
...         tf.add(filename, filter=myfilter)
...     tf.list()
-rw-r--r-- monty/501        902 2011-01-26 17:59:11 annotations.txt
-rw-r--r-- monty/501        123 2011-01-26 17:59:11 general_questions.txt
-rw-r--r-- monty/501       3514 2011-01-26 17:59:11 prion.txt
-rw-r--r-- monty/501        124 2011-01-26 17:59:11 py_todo.txt
-rw-r--r-- monty/501       1399 2011-01-26 17:59:11 semaphore_notes.txt

```

(Proposed by Tarek Ziad? and implemented by Lars Gustäbel in [bpo-6856](https://bugs.python.org/issue?@action=redirect&bpo=6856).)

[Subject index](INDEX.md) · [Previous source section](gzip-and-zipfile.md) · [Next source section](hashlib.md) · [Release/subject declaration](pep-384-defining-a-stable-abi.md)
