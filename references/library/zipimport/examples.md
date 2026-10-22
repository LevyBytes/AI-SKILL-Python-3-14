# zipimport — Examples

### Examples

The following walkthrough pulls a module out of a ZIP archive — observe that the `zipimport` module never appears explicitly.

```shell
$ unzip -l example_archive.zip
Archive:  example_archive.zip
  Length     Date   Time    Name
 --------    ----   ----    ----
     8467  01-01-00 12:30   example.py
 --------                   -------
     8467                   1 file

```

```pycon
>>> import sys
>>> # Add the archive to the front of the module search path
>>> sys.path.insert(0, 'example_archive.zip')
>>> import example
>>> example.__file__
'example_archive.zip/example.py'

```

[Subject index](INDEX.md) · [Previous](zip-importer-module-creation-and-caches.md) · [Continue](../zlib/zlib-error-to-zlib-crc32.md) · [Owning module, declaration or section: zipimport](zipimport-zipimporterror.md)
