# Defining extension modules

# Extension Modules, File

## Overview

Covers: Defining extension modules; File objects.

## Defining extension modules

### Defining extension modules

In CPython, a C extension takes the form of a shared library — say, a `.so` file under Linux or a `.pyd` DLL on Windows — that the Python process is able to load (provided it was built with matching compiler options) and that publishes an initialization function.

So that the default machinery can locate it (namely [`importlib.machinery.ExtensionFileLoader`](https://docs.python.org/3.14/library/importlib.html#importlib.machinery.ExtensionFileLoader)), the shared library has to sit somewhere on [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path) and carry a filename that joins the module name to one of the suffixes enumerated by [`importlib.machinery.EXTENSION_SUFFIXES`](https://docs.python.org/3.14/library/importlib.html#importlib.machinery.EXTENSION_SUFFIXES).

Note

Compiling, packaging, and shipping extension modules falls to third-party tooling and lies beyond what this page covers. Setuptools is one such tool; you can read its documentation at [https://setuptools.pypa.io/en/latest/setuptools.html](https://setuptools.pypa.io/en/latest/setuptools.html).

In the usual case, the initialization function hands back a module definition that has been set up via `PyModuleDef_Init()`. Doing so lets the creation work be broken into a sequence of phases:

- Ahead of running any meaningful code, Python is able to learn which features the module offers, so it can tailor the environment or decline to load an extension that is incompatible.

- Out of the box, Python is the one that builds the module object — the parallel to what [`object.__new__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__new__) does for classes. Python likewise populates starting attributes such as [`__package__`](https://docs.python.org/3.14/reference/datamodel.html#module.__package__) and [`__loader__`](https://docs.python.org/3.14/reference/datamodel.html#module.__loader__).

- After that, code belonging to the extension finishes setting up the module object — the counterpart to [`__init__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__init__) on classes.

The term for this is *multi-phase initialization*, which sets it apart from the older (yet still permitted) *single-phase initialization* approach, in which the initialization function yields an already-finished module. The single-phase-initialization section further down spells out the specifics.

Changed in version 3.5: Added support for multi-phase initialization ([**PEP 489**](https://peps.python.org/pep-0489/)).

[Subject index](INDEX.md) · [Following source contract](multiple-module-instances.md)
