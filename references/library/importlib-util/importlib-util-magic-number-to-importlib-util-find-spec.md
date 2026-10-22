# importlib.util: `importlib.util.MAGIC_NUMBER`, `importlib.util.cache_from_source()`, `importlib.util.source_from_cache()`, `importlib.util.decode_source()`, `importlib.util.resolve_name()`, `importlib.util.find_spec()`

### `importlib.util` – Utility code for importers

**Source code:** [Lib/importlib/util.py](https://github.com/python/cpython/tree/3.14/Lib/importlib/util.py)

---

The objects collected in this module aid in putting together an [importer](https://docs.python.org/3.14/glossary.html#term-importer).

 importlib.util.MAGIC_NUMBER

The bytes that encode the bytecode version number. When you need assistance loading or writing bytecode, look to `importlib.abc.SourceLoader`.

Added in version 3.4.

 importlib.util.cache_from_source(*path*, *debug_override=None*, ***, *optimization=None*)

Return the [**PEP 3147**](https://peps.python.org/pep-3147/)/[**PEP 488**](https://peps.python.org/pep-0488/) path of the byte-compiled file tied to the source *path*. As an illustration, when *path* is `/foo/bar/baz.py` the result would be `/foo/bar/__pycache__/baz.cpython-32.pyc` under Python 3.2. The `cpython-32` portion derives from the present magic tag (see `get_tag()`; when `sys.implementation.cache_tag` is undefined, [`NotImplementedError`](https://docs.python.org/3.14/library/exceptions.html#NotImplementedError) is raised).

The *optimization* parameter sets the optimization level for the bytecode file. An empty string stands for no optimization, so `/foo/bar/baz.py` together with an *optimization* of `''` produces a bytecode path of `/foo/bar/__pycache__/baz.cpython-32.pyc`. Passing `None` adopts the interpreter's own optimization level. The string form of any other value is used, so `/foo/bar/baz.py` with an *optimization* of `2` yields the bytecode path `/foo/bar/__pycache__/baz.cpython-32.opt-2.pyc`. The string form of *optimization* must be alphanumeric only, or [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised.

The *debug_override* parameter is deprecated; it lets you override the system's value for `__debug__`. A `True` value matches setting *optimization* to the empty string, while a `False` value matches setting *optimization* to `1`. When both *debug_override* and *optimization* are something other than `None`, [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) is raised.

Added in version 3.4.

Changed in version 3.5: The *optimization* parameter arrived, while *debug_override* became deprecated.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

 importlib.util.source_from_cache(*path*)

Given the *path* of a [**PEP 3147**](https://peps.python.org/pep-3147/) file name, return the path of the source code file it corresponds to. As an example, when *path* is `/foo/bar/__pycache__/baz.cpython-32.pyc` the returned path would be `/foo/bar/baz.py`. The *path* need not actually exist, yet if it fails to follow the [**PEP 3147**](https://peps.python.org/pep-3147/) or [**PEP 488**](https://peps.python.org/pep-0488/) format, a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised. When `sys.implementation.cache_tag` is undefined, [`NotImplementedError`](https://docs.python.org/3.14/library/exceptions.html#NotImplementedError) is raised.

Added in version 3.4.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

 importlib.util.decode_source(*source_bytes*)

Decode the supplied bytes that represent source code and hand them back as a string carrying universal newlines (as `importlib.abc.InspectLoader.get_source()` requires).

Added in version 3.4.

 importlib.util.resolve_name(*name*, *package*)

Resolve a relative module name to an absolute one.

When **name** carries no leading dots, **name** is given straight back. That permits usage like `importlib.util.resolve_name('sys', __spec__.parent)` without first checking whether the **package** argument matters.

[`ImportError`](https://docs.python.org/3.14/library/exceptions.html#ImportError) is raised when **name** is a relative module name yet **package** holds a false value (for example `None` or the empty string). `ImportError` is likewise raised when a relative name would break out past its enclosing package (for example asking for `..bacon` from inside the `spam` package).

Added in version 3.3.

Changed in version 3.9: For better alignment with import statements, an invalid relative import now triggers [`ImportError`](https://docs.python.org/3.14/library/exceptions.html#ImportError) rather than [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError).

 importlib.util.find_spec(*name*, *package=None*)

[Subject index](INDEX.md) · [Previous](../importlib-machinery/importlib-machinery-appleframeworkloader-class.md) · [Required continuation of the source contract](module-spec-creation-and-extension-restrictions.md)
