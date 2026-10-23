# importlib.metadata - Mapping import to distribution packages

### Mapping import to distribution packages

 importlib.metadata.packages_distributions()

Return a mapping from the top level module and import package names discovered through [`sys.meta_path`](https://docs.python.org/3.14/library/sys.html#sys.meta_path) to the names of the distribution packages (if any) that furnish the matching files.

So as to accommodate namespace packages (whose members may originate from several distribution packages), every top level import name is mapped onto a list of distribution names instead of pointing straight at one name.

A convenience method for resolving the [Distribution Package](https://packaging.python.org/en/latest/glossary/#term-Distribution-Package) name (or names, for a namespace package) that supply each importable top-level Python module or [Import Package](https://packaging.python.org/en/latest/glossary/#term-Import-Package):

```python
>>> packages_distributions()
{'importlib_metadata': ['importlib-metadata'], 'yaml': ['PyYAML'], 'jaraco': ['jaraco.classes', 'jaraco.functools'], ...}

```

Certain editable installs [do not supply top-level names](https://github.com/pypa/packaging-problems/issues/609), so this function cannot be relied upon with such installs.

Added in version 3.10.

[Subject index](INDEX.md) · [Previous](importlib-metadata-requires.md) · [Continue](importlib-metadata-distribution.md) · [Owning module, declaration or section: importlib.metadata](importlib-metadata-packagenotfounderror.md)
