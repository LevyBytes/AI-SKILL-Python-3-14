# What’s New In Python 3.5 / PEP 486: Make the Python Launcher aware of virtual environments

> PEP written by Christopher Barker; implemented by Chris Barker and Tal Einat.

### PEP 486: Make the Python Launcher aware of virtual environments

[**PEP 486**](https://peps.python.org/pep-0486/) teaches the Windows launcher (consult [**PEP 397**](https://peps.python.org/pep-0397/)) to recognize a currently active virtual environment. Whenever the default interpreter would otherwise run while the `VIRTUAL_ENV` environment variable carries a value, the launcher instead selects the interpreter located inside that virtual environment.

See also

[**PEP 486**](https://peps.python.org/pep-0486/) ? Make the Python Launcher aware of virtual environments

[Subject index](INDEX.md) · [Previous source section](pep-485-a-function-for-testing-approximate-equality.md) · [Next source section](pep-488-elimination-of-pyo-files.md) · [Release/subject declaration](summary-release-highlights.md)
