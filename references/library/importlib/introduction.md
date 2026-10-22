# Introduction

### Introduction

There are three distinct goals served by the `importlib` package.

The first is to supply, written in Python source, the machinery behind the [`import`](https://docs.python.org/3.14/reference/simple_stmts.html#import) statement ? and, as a consequence, behind the [`__import__()`](https://docs.python.org/3.14/library/functions.html#import__) function as well. Because it is Python code, this `import` machinery carries over to any Python interpreter. It is likewise far more approachable to read than an equivalent written in some language that is not Python.

The second is that the building blocks needed to realize [`import`](https://docs.python.org/3.14/reference/simple_stmts.html#import) are made public here, which lets developers more readily build their own custom objects ? referred to in general as an [importer](https://docs.python.org/3.14/glossary.html#term-importer) ? that take part in importing.

The third is that the package bundles modules that surface extra capabilities for handling various facets of Python packages:

- [`importlib.metadata`](https://docs.python.org/3.14/library/importlib.metadata.html#module-importlib.metadata) presents access to metadata from third-party distributions.

- [`importlib.resources`](https://docs.python.org/3.14/library/importlib.resources.html#module-importlib.resources) provides routines for accessing non-code ?resources? from Python packages.

See also

[The import statement](https://docs.python.org/3.14/reference/simple_stmts.html#import)

The language reference for the [`import`](https://docs.python.org/3.14/reference/simple_stmts.html#import) statement.

[Packages specification](https://www.python.org/doc/essays/packages/)

The packages mechanism as it was first specified. A handful of the semantics differ today versus when this text was authored (for instance, the use of `None` in [`sys.modules`](https://docs.python.org/3.14/library/sys.html#sys.modules) to redirect).

The `__import__()` function

This function is what the [`import`](https://docs.python.org/3.14/reference/simple_stmts.html#import) statement boils down to underneath.

[The initialization of the sys.path module search path](https://docs.python.org/3.14/library/sys_path_init.html#sys-path-init)

The initialization of [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path).

[**PEP 235**](https://peps.python.org/pep-0235/)

Import on Case-Insensitive Platforms

[**PEP 263**](https://peps.python.org/pep-0263/)

Defining Python Source Code Encodings

[**PEP 302**](https://peps.python.org/pep-0302/)

New Import Hooks

[**PEP 328**](https://peps.python.org/pep-0328/)

Imports: Multi-Line and Absolute/Relative

[**PEP 366**](https://peps.python.org/pep-0366/)

Main module explicit relative imports

[**PEP 420**](https://peps.python.org/pep-0420/)

Implicit namespace packages

[**PEP 451**](https://peps.python.org/pep-0451/)

A ModuleSpec Type for the Import System

[**PEP 488**](https://peps.python.org/pep-0488/)

Elimination of PYO files

[**PEP 489**](https://peps.python.org/pep-0489/)

Multi-phase extension module initialization

[**PEP 552**](https://peps.python.org/pep-0552/)

Deterministic pycs

[**PEP 3120**](https://peps.python.org/pep-3120/)

Using UTF-8 as the Default Source Encoding

[**PEP 3147**](https://peps.python.org/pep-3147/)

PYC Repository Directories

[Subject index](INDEX.md) · [Previous](importlib-the-implementation-of-import.md) · [Continue](importlib-import-to-importlib-reload.md)
