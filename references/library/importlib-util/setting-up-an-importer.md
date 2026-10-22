# importlib.util — Setting up an importer

### Setting up an importer

When you need to customize import deeply, the usual route is building an [importer](https://docs.python.org/3.14/glossary.html#term-importer), which entails handling both the [finder](https://docs.python.org/3.14/glossary.html#term-finder) and [loader](https://docs.python.org/3.14/glossary.html#term-loader) ends. Two finder varieties are available depending on what you require: a [meta path finder](https://docs.python.org/3.14/glossary.html#term-meta-path-finder) or a [path entry finder](https://docs.python.org/3.14/glossary.html#term-path-entry-finder). You place the first one on [`sys.meta_path`](https://docs.python.org/3.14/library/sys.html#sys.meta_path), whereas the second is built through a [path entry hook](https://docs.python.org/3.14/glossary.html#term-path-entry-hook) on [`sys.path_hooks`](https://docs.python.org/3.14/library/sys.html#sys.path_hooks), which consults [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path) entries in order to perhaps spin up a finder. The example here walks through registering your own importers so that import picks them up (and to assemble an importer of your own, consult the documentation covering the relevant classes that this package defines):

```python
import importlib.machinery
import sys

# For illustrative purposes only.
SpamMetaPathFinder = importlib.machinery.PathFinder
SpamPathEntryFinder = importlib.machinery.FileFinder
loader_details = (importlib.machinery.SourceFileLoader,
                  importlib.machinery.SOURCE_SUFFIXES)

# Setting up a meta path finder.
# Make sure to put the finder in the proper location in the list in terms of
# priority.
sys.meta_path.append(SpamMetaPathFinder)

# Setting up a path entry finder.
# Make sure to put the path hook in the proper location in the list in terms
# of priority.
sys.path_hooks.append(SpamPathEntryFinder.path_hook(loader_details))

```

[Subject index](INDEX.md) · [Previous](implementing-lazy-imports.md) · [Continue](approximating-importlib-import-module.md) · [Owning module, declaration or section: importlib.util](importlib-util-magic-number-to-importlib-util-find-spec.md)
