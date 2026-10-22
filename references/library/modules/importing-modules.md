# modulefinder — Importing Modules

## Importing Modules

### Importing Modules

The modules covered in this chapter add fresh means of importing other Python modules plus hooks for tailoring the import process.

The full list of modules described in this chapter is:

- [`zipimport` — Import modules from Zip archives](https://docs.python.org/3.14/library/zipimport.html)
  - [zipimporter Objects](https://docs.python.org/3.14/library/zipimport.html#zipimporter-objects)
  - [Examples](https://docs.python.org/3.14/library/zipimport.html#examples)

- [`pkgutil` — Package extension utility](https://docs.python.org/3.14/library/pkgutil.html)
- [`modulefinder` — Find modules used by a script](https://docs.python.org/3.14/library/modulefinder.html)
  - [Example usage of `ModuleFinder`](https://docs.python.org/3.14/library/modulefinder.html#example-usage-of-modulefinder)

- [`runpy` — Locating and executing Python modules](https://docs.python.org/3.14/library/runpy.html)
- [`importlib` — The implementation of `import`](https://docs.python.org/3.14/library/importlib.html)
  - [Introduction](https://docs.python.org/3.14/library/importlib.html#introduction)
  - [Functions](https://docs.python.org/3.14/library/importlib.html#functions)
  - [`importlib.abc` – Abstract base classes related to import](https://docs.python.org/3.14/library/importlib.html#module-importlib.abc)
  - [`importlib.machinery` – Importers and path hooks](https://docs.python.org/3.14/library/importlib.html#module-importlib.machinery)
  - [`importlib.util` – Utility code for importers](https://docs.python.org/3.14/library/importlib.html#module-importlib.util)
  - [Examples](https://docs.python.org/3.14/library/importlib.html#examples)
    - [Importing programmatically](https://docs.python.org/3.14/library/importlib.html#importing-programmatically)
    - [Checking if a module can be imported](https://docs.python.org/3.14/library/importlib.html#checking-if-a-module-can-be-imported)
    - [Importing a source file directly](https://docs.python.org/3.14/library/importlib.html#importing-a-source-file-directly)
    - [Implementing lazy imports](https://docs.python.org/3.14/library/importlib.html#implementing-lazy-imports)
    - [Setting up an importer](https://docs.python.org/3.14/library/importlib.html#setting-up-an-importer)
    - [Approximating `importlib.import_module()`](https://docs.python.org/3.14/library/importlib.html#approximating-importlib-import-module)

- [`importlib.resources` – Package resource reading, opening and access](https://docs.python.org/3.14/library/importlib.resources.html)
  - [Functional API](https://docs.python.org/3.14/library/importlib.resources.html#functional-api)

- [`importlib.resources.abc` – Abstract base classes for resources](https://docs.python.org/3.14/library/importlib.resources.abc.html)
- [`importlib.metadata` – Accessing package metadata](https://docs.python.org/3.14/library/importlib.metadata.html)
  - [Overview](https://docs.python.org/3.14/library/importlib.metadata.html#overview)
  - [Functional API](https://docs.python.org/3.14/library/importlib.metadata.html#functional-api)
    - [Entry points](https://docs.python.org/3.14/library/importlib.metadata.html#entry-points)
    - [Distribution metadata](https://docs.python.org/3.14/library/importlib.metadata.html#distribution-metadata)
    - [Distribution versions](https://docs.python.org/3.14/library/importlib.metadata.html#distribution-versions)
    - [Distribution files](https://docs.python.org/3.14/library/importlib.metadata.html#distribution-files)
    - [Distribution requirements](https://docs.python.org/3.14/library/importlib.metadata.html#distribution-requirements)
    - [Mapping import to distribution packages](https://docs.python.org/3.14/library/importlib.metadata.html#mapping-import-to-distribution-packages)

  - [Distributions](https://docs.python.org/3.14/library/importlib.metadata.html#distributions)
  - [Distribution Discovery](https://docs.python.org/3.14/library/importlib.metadata.html#distribution-discovery)
  - [Implementing Custom Providers](https://docs.python.org/3.14/library/importlib.metadata.html#implementing-custom-providers)
    - [Example](https://docs.python.org/3.14/library/importlib.metadata.html#example)

- [The initialization of the `sys.path` module search path](https://docs.python.org/3.14/library/sys_path_init.html)
  - [Virtual Environments](https://docs.python.org/3.14/library/sys_path_init.html#virtual-environments)
  - [_pth files](https://docs.python.org/3.14/library/sys_path_init.html#pth-files)
  - [Embedded Python](https://docs.python.org/3.14/library/sys_path_init.html#embedded-python)

[Subject index](INDEX.md) · [Continue](../msilib/msilib-read-and-write-microsoft-installer-files.md)
