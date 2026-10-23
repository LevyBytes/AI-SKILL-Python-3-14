# shutil - Archiving example with *base_dir*

### Archiving example with *base_dir*

This example, much like the previous one, demonstrates `make_archive()`, except here we bring *base_dir* into play. Suppose our directory layout is now:

```shell
$ tree tmp
tmp
└── root
    └── structure
        ├── content
            └── please_add.txt
        └── do_not_add.txt

```

We want `please_add.txt` in the finished archive while keeping `do_not_add.txt` out. To that end we run:

```python
>>> from shutil import make_archive
>>> import os
>>> archive_name = os.path.expanduser(os.path.join('~', 'myarchive'))
>>> make_archive(
...     archive_name,
...     'tar',
...     root_dir='tmp/root',
...     base_dir='structure/content',
... )
'/Users/tarek/myarchive.tar'

```

Listing out the files in the archive we built yields:

```shell
$ python -m tarfile -l /Users/tarek/myarchive.tar
structure/content/
structure/content/please_add.txt

```

[Subject index](INDEX.md) · [Previous](archiving-example.md) · [Continue](shutil-get-terminal-size.md) · [Owning module, declaration or section: shutil](shutil-high-level-file-operations.md)
