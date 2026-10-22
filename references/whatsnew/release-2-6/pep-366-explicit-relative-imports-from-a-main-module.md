# What’s New in Python 2.6 / PEP 366: Explicit Relative Imports From a Main Module — runpy

### PEP 366: Explicit Relative Imports From a Main Module

Python’s [`-m`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-m) switch lets you execute a module as though it were a script. Previously, running a module that lived inside a package broke relative imports.

To address this, Python 2.6 introduces a [`module.__package__`](https://docs.python.org/3.14/reference/datamodel.html#module.__package__) attribute. Whenever that attribute exists, relative imports are resolved against its value in place of the [`__name__`](https://docs.python.org/3.14/reference/datamodel.html#module.__name__) attribute.

Importers built in the PEP 302 style can then assign [`__package__`](https://docs.python.org/3.14/reference/datamodel.html#module.__package__) when needed. Because the [`runpy`](https://docs.python.org/3.14/library/runpy.html#module-runpy) module behind the [`-m`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-m) switch now does exactly that, relative imports finally behave correctly in scripts launched from within a package.

[Subject index](INDEX.md) · [Previous source section](the-contextlib-module.md) · [Next source section](pep-370-per-user-site-packages-directory.md) · [Release/subject declaration](python-3-0.md)
