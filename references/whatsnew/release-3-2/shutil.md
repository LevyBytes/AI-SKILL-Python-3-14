# What's New In Python 3.2 / shutil - os, shutil

### shutil

A pair of fresh options arrive on the [`shutil.copytree()`](https://docs.python.org/3.14/library/shutil.html#shutil.copytree) function:

- *ignore_dangling_symlinks*: relevant when `symlinks=False`, where the function copies the target a symlink points at rather than the link itself. Setting this suppresses the error that would otherwise fire if the target is missing.

- *copy_function*: a callable invoked to copy files. The default choice is [`shutil.copy2()`](https://docs.python.org/3.14/library/shutil.html#shutil.copy2).

(Contributed by Tarek Ziadé.)

Beyond that, the [`shutil`](https://docs.python.org/3.14/library/shutil.html#module-shutil) module now offers [archiving operations](https://docs.python.org/3.14/library/shutil.html#archiving-operations) covering zipfiles, uncompressed tarfiles, gzipped tarfiles, and bzipped tarfiles. Functions also exist that let you register extra archiving formats (for instance xz compressed tarfiles or formats of your own).

At the center sit [`make_archive()`](https://docs.python.org/3.14/library/shutil.html#shutil.make_archive) and [`unpack_archive()`](https://docs.python.org/3.14/library/shutil.html#shutil.unpack_archive). Out of the box each works against the current directory (adjustable via [`os.chdir()`](https://docs.python.org/3.14/library/os.html#os.chdir)) together with whatever sub-directories sit beneath it. You give the archive filename as a full pathname. Because the archiving pass is non-destructive, the source files stay as they were.

```python
>>> import shutil, pprint

>>> os.chdir('mydata')  # change to the source directory
>>> f = shutil.make_archive('/var/backup/mydata',
...                         'zip')      # archive the current directory
>>> f                                   # show the name of archive
'/var/backup/mydata.zip'
>>> os.chdir('tmp')                     # change to an unpacking
>>> shutil.unpack_archive('/var/backup/mydata.zip')  # recover the data

>>> pprint.pprint(shutil.get_archive_formats())  # display known formats
[('bztar', "bzip2'ed tar-file"),
 ('gztar', "gzip'ed tar-file"),
 ('tar', 'uncompressed tar file'),
 ('zip', 'ZIP file')]

>>> shutil.register_archive_format(     # register a new archive format
...     name='xz',
...     function=xz.compress,           # callable archiving function
...     extra_args=[('level', 8)],      # arguments to the function
...     description='xz compression'
... )

```

(Contributed by Tarek Ziadé.)

[Subject index](INDEX.md) · [Previous source section](os.md) · [Next source section](sqlite3.md) · [Release/subject declaration](pep-384-defining-a-stable-abi.md)
