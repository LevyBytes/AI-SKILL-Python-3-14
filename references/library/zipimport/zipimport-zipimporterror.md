# zipimport`zipimport` - Import modules from Zip archives

### `zipimport` - Import modules from Zip archives

**Source code:** [Lib/zipimport.py](https://github.com/python/cpython/tree/3.14/Lib/zipimport.py)

---

With this module you can load Python modules (`*.py`, `*.pyc`) along with packages straight out of archives in ZIP format. You rarely have to call on the `zipimport` module yourself; the standard [`import`](https://docs.python.org/3.14/reference/simple_stmts.html#import) machinery reaches for it automatically whenever entries in [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path) point at ZIP archives.

Ordinarily, [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path) holds a sequence of directory names given as strings. Here, though, an entry in `sys.path` may instead be a string that names a ZIP file archive. Such an archive may hold a nested folder layout so packages import correctly, and you can append a path inside the archive to restrict imports to one subfolder. As an illustration, writing `example.zip/lib/` confines imports to the `lib/` subfolder held in the archive.

A ZIP archive may hold any kind of file, yet importers only fire for `.py` and `.pyc` entries. Bringing in dynamic modules (`.pyd`, `.so`) through ZIP import is not permitted. Be aware that when an archive holds nothing but `.py` files, Python won't rewrite the archive to drop in the matching `.pyc` file, so an archive lacking `.pyc` files can make importing fairly sluggish.

Changed in version 3.13: ZIP64 is supported

Changed in version 3.8: Earlier releases gave no support to ZIP archives carrying an archive comment.

See also

[PKZIP Application Note](https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT)

Reference covering the ZIP file format, authored by Phil Katz, who devised both the format and its algorithms.

[**PEP 273**](https://peps.python.org/pep-0273/) - Import Modules from Zip Archives

Authored by James C. Ahlstrom, who also contributed an implementation. Python 2.3 conforms to the [**PEP 273**](https://peps.python.org/pep-0273/) specification, though it relies on code written by Just van Rossum that builds on the import hooks laid out in [**PEP 302**](https://peps.python.org/pep-0302/).

[`importlib`](https://docs.python.org/3.14/library/importlib.html#module-importlib) - The implementation of the import machinery

The package that supplies the protocols every importer is meant to implement.

An exception is defined by this module:

 *exception *zipimport.ZipImportError

The error that zipimporter objects throw. Because it derives from [`ImportError`](https://docs.python.org/3.14/library/exceptions.html#ImportError), you may also trap it as `ImportError`.

[Subject index](INDEX.md) · [Previous](import-modules-from-zip-archives.md) · [Continue](zipimport-zipimporter-class.md)
