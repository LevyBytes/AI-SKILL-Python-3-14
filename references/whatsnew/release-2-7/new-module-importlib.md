# What’s New in Python 2.7 / New module: importlib — importlib

### New module: importlib

Python 3.1 ships the [`importlib`](https://docs.python.org/3.14/library/importlib.html#module-importlib) package, a fresh implementation of the logic sitting beneath Python's [`import`](https://docs.python.org/3.14/reference/simple_stmts.html#import) statement. `importlib` serves both the implementers of Python interpreters and users who want to author new importers able to take part in the import process. Rather than the whole `importlib` package, Python 2.7 carries only a small slice of it, a lone function named [`import_module()`](https://docs.python.org/3.14/library/importlib.html#importlib.import_module).

`import_module(name, package=None)` brings in a module. *name* is a string holding the name of the module or package. Relative imports are possible by passing a string that opens with a `.` character, for instance `..utils.errors`. When doing a relative import, you must supply the *package* argument, which names the package serving as the anchor for that relative import. [`import_module()`](https://docs.python.org/3.14/library/importlib.html#importlib.import_module) places the imported module into `sys.modules` and also returns the module object.

A few examples follow:

```python
>>> from importlib import import_module
>>> anydbm = import_module('anydbm')  # Standard absolute import
>>> anydbm
<module 'anydbm' from '/p/python/Lib/anydbm.py'>
>>> # Relative import
>>> file_util = import_module('..file_util', 'distutils.command')
>>> file_util
<module 'distutils.file_util' from '/python/Lib/distutils/file_util.pyc'>

```

[`importlib`](https://docs.python.org/3.14/library/importlib.html#module-importlib) was written by Brett Cannon and first appeared in Python 3.1.

[Subject index](INDEX.md) · [Previous source section](zip-compression-overrides.md) · [Next source section](new-module-sysconfig.md) · [Release/subject declaration](the-future-for-python-2-x.md)
