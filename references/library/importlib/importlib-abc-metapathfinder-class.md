# importlib: `importlib.abc.MetaPathFinder`

### `importlib.abc` — Abstract base classes related to import

**Source code:** [Lib/importlib/abc.py](https://github.com/python/cpython/tree/3.14/Lib/importlib/abc.py)

---

Every one of the central abstract base classes that [`import`](https://docs.python.org/3.14/reference/simple_stmts.html#import) relies on lives in the `importlib.abc` module. Alongside them, a few subclasses of those central abstract base classes ship as well, to ease building the central ABCs.

ABC hierarchy:

```python
object
 +-- MetaPathFinder
 +-- PathEntryFinder
 +-- Loader
      +-- ResourceLoader --------+
      +-- InspectLoader          |
           +-- ExecutionLoader --+
                                 +-- FileLoader
                                 +-- SourceLoader

```

 *class *importlib.abc.MetaPathFinder

An abstract base class that stands for a [meta path finder](https://docs.python.org/3.14/glossary.html#term-meta-path-finder).

Added in version 3.3.

Changed in version 3.10: No longer a subclass of `Finder`.

[Subject index](INDEX.md) · [Previous](importlib-import-to-importlib-reload.md) · [Continue](meta-path-finder-spec-and-cache-contract.md)
