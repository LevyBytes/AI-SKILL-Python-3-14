# importlib.resources — `importlib.resources` – Package resource reading, opening and access

## importlib.resources – Package resource reading, opening and access

### `importlib.resources` – Package resource reading, opening and access

**Source code:** [Lib/importlib/resources/__init__.py](https://github.com/python/cpython/tree/3.14/Lib/importlib/resources/__init__.py)

---

Added in version 3.7.

This module taps Python’s import machinery to make *resources* inside *packages* reachable.

In Python, “resources” are file-like resources tied to a module or package. A resource might sit directly within a package, inside a subdirectory of that package, or next to modules outside any package. Resources come as either text or binary. It follows that, within a given package, its Python module sources (.py), along with compilation artifacts (pycache) and installation artifacts (for example [`reserved filenames`](https://docs.python.org/3.14/library/os.path.html#os.path.isreserved) sitting in directories), all qualify, strictly speaking, as de-facto resources of that package. Day to day, though, resources chiefly mean the non-Python artifacts the package author has deliberately exposed.

You may open or read resources in binary mode or text mode alike.

Loosely, resources resemble files held inside directories, but do bear in mind that this is only a metaphor. Neither resources nor packages **need** exist as actual files and directories on the file system: a package together with its resources can, for instance, be imported straight out of a zip file via [`zipimport`](https://docs.python.org/3.14/library/zipimport.html#module-zipimport).

Warning

`importlib.resources` abides by the same security model as the built-in [`open()`](https://docs.python.org/3.14/library/functions.html#open) function. Feeding untrusted inputs to this module's functions is unsafe.

Note

The standalone backport of this module provides more information on [using importlib.resources](https://importlib-resources.readthedocs.io/en/latest/using.html) and [migrating from pkg_resources to importlib.resources](https://importlib-resources.readthedocs.io/en/latest/migration.html).

Any [`Loaders`](https://docs.python.org/3.14/library/importlib.html#importlib.abc.Loader) wanting to back resource reading ought to implement a `get_resource_reader(fullname)` method along the lines laid out by [`importlib.resources.abc.ResourceReader`](https://docs.python.org/3.14/library/importlib.resources.abc.html#importlib.resources.abc.ResourceReader).

 *class *importlib.resources.Anchor

Stands for a resource anchor — supplied as either a [`module object`](https://docs.python.org/3.14/library/types.html#types.ModuleType) or a module name given as a string. Its definition is `Union[str, ModuleType]`.

 importlib.resources.files(*anchor: Anchor | [None](https://docs.python.org/3.14/library/constants.html#None) = None*)

Hands back a [`Traversable`](https://docs.python.org/3.14/library/importlib.resources.abc.html#importlib.resources.abc.Traversable) object standing for the resource container (picture a directory) plus its resources (picture files). One Traversable can itself hold further containers (picture subdirectories).

The *anchor* is an optional `Anchor`. When it is a package, resources get resolved out of that package. When it is a module, resources get resolved beside that module (within the same package or at the package root). Omit the anchor and the caller’s module stands in.

Added in version 3.9.

Changed in version 3.12: the *package* parameter became *anchor*. From here on *anchor* may be a non-package module, and leaving it out makes it default to the caller’s module. For compatibility *package* is still taken, yet it triggers a [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning). Think about handing the anchor in positionally, or lean on `importlib_resources >= 5.10` to get a compatible interface on older Pythons.

 importlib.resources.as_file(*traversable*)

Hand it a [`Traversable`](https://docs.python.org/3.14/library/importlib.resources.abc.html#importlib.resources.abc.Traversable) object standing for a file or directory — usually one from `importlib.resources.files()` — and it returns a context manager to be used inside a [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement. That context manager yields a [`pathlib.Path`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path) object.

Leaving the context manager tidies up whatever temporary file or directory was made while pulling the resource out of, say, a zip file.

Turn to `as_file` whenever the Traversable methods (`read_text`, etc) fall short and you genuinely need a real file or directory present on the file system.

Added in version 3.9.

Changed in version 3.12: Added support for *traversable* representing a directory.

[Subject index](INDEX.md) · [Continue](resource-binary-and-text-opening.md)
