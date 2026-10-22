# importlib.metadata — `importlib.metadata` – Accessing package metadata

# Importlib.Metadata

### `importlib.metadata` – Accessing package metadata

Added in version 3.8.

Changed in version 3.10: `importlib.metadata` is no longer provisional.

**Source code:** [Lib/importlib/metadata/__init__.py](https://github.com/python/cpython/tree/3.14/Lib/importlib/metadata/__init__.py)

`importlib.metadata` is a library that exposes the metadata belonging to an installed [Distribution Package](https://packaging.python.org/en/latest/glossary/#term-Distribution-Package) — for instance its entry points or its top-level names ([Import Package](https://packaging.python.org/en/latest/glossary/#term-Import-Package)s, modules, where present). Constructed partly atop Python’s import system, the library offers the entry point and metadata APIs formerly delivered by the now-removed `pkg_resources` package. Together with [`importlib.resources`](https://docs.python.org/3.14/library/importlib.resources.html#module-importlib.resources), it takes the place of `pkg_resources`.

`importlib.metadata` acts on third-party *distribution packages* placed into Python’s `site-packages` directory by tooling like [pip](https://pypi.org/project/pip/). More precisely, it handles distributions that have discoverable `dist-info` or `egg-info` directories, plus metadata laid out by the [Core metadata specifications](https://packaging.python.org/en/latest/specifications/core-metadata/#core-metadata).

Important

These do *not* always match up or correspond 1:1 with the top-level *import package* names you can import from within Python code. A single *distribution package* may bundle several *import packages* (and standalone modules), and a single top-level *import package* might span several *distribution packages* when it is a namespace package. To obtain a mapping linking the two, call packages_distributions().

Out of the box, distribution metadata may reside on the file system or inside zip archives on [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path). Via an extension mechanism, that metadata can be stored almost anywhere.

See also

[https://importlib-metadata.readthedocs.io/](https://importlib-metadata.readthedocs.io/)

Documentation for `importlib_metadata`, which delivers a backport of `importlib.metadata`. It carries an [API reference](https://importlib-metadata.readthedocs.io/en/latest/api.html) covering this module’s classes and functions, plus a [migration guide](https://importlib-metadata.readthedocs.io/en/latest/migration.html) for those already relying on `pkg_resources`.

### Overview

Suppose you wished to retrieve the version string of a [Distribution Package](https://packaging.python.org/en/latest/glossary/#term-Distribution-Package) you have installed with `pip`. Begin by building a virtual environment and installing something inside it:

```shell
$ python -m venv example
$ source example/bin/activate
(example) $ python -m pip install wheel

```

To obtain the version string for `wheel`, run this:

```pycon
(example) $ python
>>> from importlib.metadata import version
>>> version('wheel')
'0.32.3'

```

You may likewise fetch a set of entry points chosen by attributes of the EntryPoint (commonly ‘group’ or ‘name’), for example `console_scripts`, `distutils.commands` and so on. Every group holds a set of EntryPoint objects.

You can retrieve the metadata for a distribution:

```python
>>> list(metadata('wheel'))
['Metadata-Version', 'Name', 'Version', 'Summary', 'Home-page', 'Author', 'Author-email', 'Maintainer', 'Maintainer-email', 'License', 'Project-URL', 'Project-URL', 'Project-URL', 'Keywords', 'Platform', 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Requires-Python', 'Provides-Extra', 'Requires-Dist', 'Requires-Dist']

```

You may additionally fetch a distribution’s version number, enumerate the files it comprises, and obtain a list of that distribution’s Distribution requirements.

 *exception *importlib.metadata.PackageNotFoundError

Subclass of [`ModuleNotFoundError`](https://docs.python.org/3.14/library/exceptions.html#ModuleNotFoundError) that several functions in this module raise when asked about a distribution package not installed in the current Python environment.

[Subject index](INDEX.md) · [Continue](functional-api.md)
