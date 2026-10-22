# importlib.resources.abc: `importlib.resources.abc.ResourceReader`

### `importlib.resources.abc` – Abstract base classes for resources

**Source code:** [Lib/importlib/resources/abc.py](https://github.com/python/cpython/tree/3.14/Lib/importlib/resources/abc.py)

---

Added in version 3.11.

 *class *importlib.resources.abc.ResourceReader

*Superseded by TraversableResources*

An [abstract base class](https://docs.python.org/3.14/glossary.html#term-abstract-base-class) granting the capacity to read *resources*.

As this ABC sees things, a *resource* is a binary artifact bundled inside a package. Most often that means a data file sitting beside the package's `__init__.py` file. This class exists to abstract away how such data files get accessed, so it makes no difference whether the package and its data file(s) live, say, inside a zip file or out on the file system.

Whichever method of this class you call, its *resource* argument is meant to be a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object) standing in for, conceptually, nothing more than a file name. Put differently, no subdirectory paths belong in the *resource* argument. The reason is that the package the reader serves supplies the “directory” itself. So the metaphor maps packages onto directories and resources onto file names, respectively. That is likewise why each instance of this class is meant to line up one-to-one with a particular package (rather than possibly covering several packages or a module).

A loader that wants to back resource reading is meant to expose a method named `get_resource_reader(fullname)` that yields an object fulfilling this ABC’s interface. Should the module named by fullname not be a package, this method ought to return [`None`](https://docs.python.org/3.14/library/constants.html#None). Only when the named module really is a package should an object compatible with this ABC come back.

Deprecated since version 3.12: Use `importlib.resources.abc.TraversableResources` instead.

[Subject index](INDEX.md) · [Previous](importlib-resources-abc-abstract-base-classes-for-resources.md) · [Continue](importlib-resources-abc-abstract-base-classes-for-resources.md)
