# Import discovery

Open when checking Python definitions for import discovery.

## importing

The mechanism whereby Python code residing in one module becomes available to Python code in a different module.

## importer

An object that locates and loads a module alike; both a finder and loader object.

## module spec

A namespace that holds the import-related information employed when loading a module. It is an instance of [`importlib.machinery.ModuleSpec`](https://docs.python.org/3.14/library/importlib.html#importlib.machinery.ModuleSpec).

See also [Module specs](https://docs.python.org/3.14/reference/import.html#module-specs).

## import path

A roster of locations (the path entries) that the path based finder scans when importing modules. Typically this roster originates from [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path) during import, yet for subpackages it can instead derive from the parent package's `__path__` attribute.

## finder

An object whose job is to locate the loader for a module undergoing import.

Finders come in two flavors: meta path finders meant for [`sys.meta_path`](https://docs.python.org/3.14/library/sys.html#sys.meta_path), and path entry finders meant for [`sys.path_hooks`](https://docs.python.org/3.14/library/sys.html#sys.path_hooks).

For a great deal more detail, see [Finders and loaders](https://docs.python.org/3.14/reference/import.html#finders-and-loaders) and [`importlib`](https://docs.python.org/3.14/library/importlib.html#module-importlib).

## loader

An object whose job is loading a module. To satisfy the [`Loader`](https://docs.python.org/3.14/library/importlib.html#importlib.abc.Loader) interface it has to define the `exec_module()` and `create_module()` methods. Typically a finder is what hands back a loader. See also:

- [Finders and loaders](https://docs.python.org/3.14/reference/import.html#finders-and-loaders)

- [`importlib.abc.Loader`](https://docs.python.org/3.14/library/importlib.html#importlib.abc.Loader)

- [**PEP 302**](https://peps.python.org/pep-0302/)

## meta path finder

A finder yielded by searching [`sys.meta_path`](https://docs.python.org/3.14/library/sys.html#sys.meta_path). Meta path finders bear a relationship to path entry finders yet remain distinct from them.

Refer to [`importlib.abc.MetaPathFinder`](https://docs.python.org/3.14/library/importlib.html#importlib.abc.MetaPathFinder) for the methods that meta path finders implement.

## path based finder

One of the default meta path finders, which scans an import path looking for modules.

## path entry

One spot on the import path that the path based finder examines when locating modules to import.

## path entry finder

A finder yielded by a callable on [`sys.path_hooks`](https://docs.python.org/3.14/library/sys.html#sys.path_hooks) (that is, a path entry hook) that understands how to locate modules from a given path entry.

Refer to [`importlib.abc.PathEntryFinder`](https://docs.python.org/3.14/library/importlib.html#importlib.abc.PathEntryFinder) for the methods that path entry finders implement.

## path entry hook

A callable sitting on the [`sys.path_hooks`](https://docs.python.org/3.14/library/sys.html#sys.path_hooks) list that returns a path entry finder whenever it understands how to find modules on a particular path entry.

## hash-based pyc

A bytecode cache file relying on the hash, instead of the last-modified time, of its matching source file to judge whether it is still valid. See [Cached bytecode invalidation](https://docs.python.org/3.14/reference/import.html#pyc-invalidation).

[Glossary context index](INDEX.md).
