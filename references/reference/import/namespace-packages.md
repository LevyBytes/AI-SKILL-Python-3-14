# 5.2.2. Namespace packages

### 5.2.2. Namespace packages

A namespace package is assembled from several [portions](https://docs.python.org/3.14/glossary.html#term-portion), with every portion adding a subpackage to the parent package. Different portions can live at different spots on the file system. Portions might equally turn up inside zip files, across the network, or anywhere else Python looks while importing. A namespace package need not line up one-to-one with anything on the file system; it can be a virtual module lacking any concrete form.

For their `__path__` attribute, namespace packages skip the plain list. Instead they rely on a bespoke iterable type that, on the next import attempt within the package, automatically launches a fresh search for package portions whenever the path of the parent package shifts (or [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path) shifts, for a top level package).

Namespace packages come without any `parent/__init__.py` file. Indeed, the import search might turn up several `parent` directories, each one supplied by a separate portion. Because of that, `parent/one` need not sit physically alongside `parent/two`. Under these circumstances, Python builds a namespace package for the top-level `parent` package the moment it, or any of its subpackages, gets imported.

A namespace package can also live nested within a regular package. While the import system walks a regular package’s `__path__` and runs into a subdirectory missing an `__init__.py` file, that subdirectory turns into a [portion](https://docs.python.org/3.14/glossary.html#term-portion) feeding a namespace subpackage of the surrounding regular package.

The namespace package specification is likewise found in [**PEP 420**](https://peps.python.org/pep-0420/).

[Subject index](INDEX.md) · [Owning language section](the-import-system.md) · [Owning language section](packages.md) · [Previous source section](regular-packages.md) · [Following source section](searching.md)
