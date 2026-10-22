# What’s New in Python 2.6 / New and Improved Modules — zipfile

In the [`zipfile`](https://docs.python.org/3.14/library/zipfile.html#module-zipfile) module, the `ZipFile` class has gained `extract()` and `extractall()` methods. These let you pull out a single member or every member of an archive, dropping the result into the working directory or into a directory you name:

```python
z = zipfile.ZipFile('python-251.zip')

# Unpack a single file, writing it relative
# to the /tmp directory.
z.extract('Python/sysmodule.c', '/tmp')

# Unpack all the files in the archive.
z.extractall()

```

(Contributed by Alan McIntyre; [bpo-467924](https://bugs.python.org/issue?@action=redirect&bpo=467924).)

You may now hand either a filename or a `ZipInfo` object to the [`open()`](https://docs.python.org/3.14/library/functions.html#open), `read()` and `extract()` methods. That helps in the case where an archive has mistakenly ended up with two members sharing a name. (Contributed by Graham Horler; [bpo-1775025](https://bugs.python.org/issue?@action=redirect&bpo=1775025).)

On top of that, [`zipfile`](https://docs.python.org/3.14/library/zipfile.html#module-zipfile) can at last handle Unicode filenames for the entries it stores. (Contributed by Alexey Borzenkov; [bpo-1734346](https://bugs.python.org/issue?@action=redirect&bpo=1734346).)

[Subject index](INDEX.md) · [Next source section](the-ast-module.md) · [Release/subject declaration](python-3-0.md) · [Release/subject declaration](standard-library-module-changes.md) · [Preceding release/subject continuation](turtle-unicode-url-warning-and-xmlrpc-changes.md)
