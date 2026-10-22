# What’s New In Python 3.5 / PEP 489: Multi-phase extension module initialization

> PEP written and implemented by Brett Cannon.

### PEP 489: Multi-phase extension module initialization

[**PEP 489**](https://peps.python.org/pep-0489/) revises how extension modules initialize so they can exploit the two-step loading machinery that [**PEP 451**](https://peps.python.org/pep-0451/) delivered back in Python 3.4.

Thanks to this revision, the import behavior of extension modules that choose the fresh mechanism lines up far more tightly with that of Python source and bytecode modules; that includes accepting any valid identifier for a module name rather than staying limited to ASCII.

See also

[**PEP 489**](https://peps.python.org/pep-0489/) ? Multi-phase extension module initialization

[Subject index](INDEX.md) · [Previous source section](pep-488-elimination-of-pyo-files.md) · [Next source section](other-language-changes.md) · [Release/subject declaration](summary-release-highlights.md)
