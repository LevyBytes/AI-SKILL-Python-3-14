# Modules and packages

Open when checking Python definitions for modules and packages.

## module

An object acting as an organizational unit for Python code. A module carries a namespace holding arbitrary Python objects. Bringing modules into Python happens through the importing process.

See also package.

## extension module

A module authored in C or C++, employing Python's C API to communicate with the core and with user code.

## optional module

An extension module belonging to the standard library that may nonetheless be missing in some CPython builds, normally because third-party libraries are absent or because the module does not exist for a particular platform.

Consult [Requirements for optional modules](https://docs.python.org/3.14/using/configure.html#optional-module-requirements) for a listing of optional modules dependent on third-party libraries.

## standard library

The assortment of packages, modules and extension modules shipped as part of the official Python interpreter package. Precisely what belongs to the assortment can shift with the platform, the system libraries on hand, or other factors. You can find the documentation at [The Python Standard Library](https://docs.python.org/3.14/library/index.html#library-index).

Consult [`sys.stdlib_module_names`](https://docs.python.org/3.14/library/sys.html#sys.stdlib_module_names) as well for a listing of every possible standard library module name.

## stdlib

A short form of standard library.

## package

A Python module capable of holding submodules or, recursively, subpackages. In technical terms, a package is a Python module carrying a `__path__` attribute.

See also regular package and namespace package.

## regular package

A conventional package, for instance a directory holding an `__init__.py` file.

See also namespace package.

## namespace package

A package whose sole role is to hold subpackages. A namespace package can lack any physical representation, and notably differs from a regular package in having no `__init__.py` file.

By way of namespace packages, several packages installable on their own may share one parent package. Apart from that case, a regular package is the recommended choice.

For further details, see [**PEP 420**](https://peps.python.org/pep-0420/) and [Namespace packages](https://docs.python.org/3.14/reference/import.html#reference-namespace-package).

See also module.

## portion

A collection of files within one directory (potentially kept inside a zip file) that feed into a namespace package, as laid out in [**PEP 420**](https://peps.python.org/pep-0420/).

## virtual environment

A cooperatively isolated runtime environment letting Python users and applications install and upgrade Python distribution packages without disturbing how other Python applications on the same system behave.

See also [`venv`](https://docs.python.org/3.14/library/venv.html#module-venv).

[Glossary context index](INDEX.md).
