# What's New In Python 3.3 / PEP 405: Virtual Environments — venv

### PEP 405: Virtual Environments

A virtual environment lets you build isolated Python setups that still draw on a shared system-wide base install, which keeps upkeep simple. Each virtual environment carries its own private site packages (that is, libraries installed locally), and may optionally be walled off from the system-wide site packages. The idea and the code behind them draw on the well-known `virtualenv` third-party package, yet gain from closer coupling with the interpreter core.

The PEP introduces the [`venv`](https://docs.python.org/3.14/library/venv.html#module-venv) module for programmatic use, plus the `pyvenv` script for managing and accessing them from the command line. To locate the root of a virtual environment's directory tree, the Python interpreter looks for a `pyvenv.cfg`, file whose presence marks it.

See also

[**PEP 405**](https://peps.python.org/pep-0405/) - Python Virtual Environments

PEP written by Carl Meyer; implementation by Carl Meyer and Vinay Sajip

[Subject index](INDEX.md) · [Previous source section](summary-release-highlights.md) · [Next source section](pep-420-implicit-namespace-packages.md) · [Release/subject declaration](summary-release-highlights.md)
