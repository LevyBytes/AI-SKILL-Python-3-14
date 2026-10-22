# What's New in Python 2.5 / PEP 338: Executing Modules as Scripts — runpy, zipimport

### PEP 338: Executing Modules as Scripts

The [`-m`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-m) switch, brought in with Python 2.4 for running a module as a script, gained a few extra capabilities. Rather than living as C code within the Python interpreter, the switch is now driven by an implementation housed in a new module, [`runpy`](https://docs.python.org/3.14/library/runpy.html#module-runpy).

The [`runpy`](https://docs.python.org/3.14/library/runpy.html#module-runpy) module provides a more refined import mechanism, so it's now feasible to run modules sitting inside a package such as `pychecker.checker`. The module additionally supports alternative import mechanisms like the [`zipimport`](https://docs.python.org/3.14/library/zipimport.html#module-zipimport) module. That lets you append the path of a .zip archive to `sys.path` and afterward use the [`-m`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-m) switch to run code straight out of the archive.

See also

[**PEP 338**](https://peps.python.org/pep-0338/) - Executing modules as scripts

PEP written and implemented by Nick Coghlan.

[Subject index](INDEX.md) · [Previous source section](pep-328-absolute-and-relative-imports.md) · [Next source section](pep-341-unified-try-except-finally.md) · [Release/subject declaration](pep-308-conditional-expressions.md)
