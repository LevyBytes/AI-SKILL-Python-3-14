# What's New In Python 3.6 / Deprecated Python modules, functions and methods / importlib — importlib, sys

#### importlib

The [`importlib.machinery.SourceFileLoader.load_module()`](https://docs.python.org/3.14/library/importlib.html#importlib.machinery.SourceFileLoader.load_module) and [`importlib.machinery.SourcelessFileLoader.load_module()`](https://docs.python.org/3.14/library/importlib.html#importlib.machinery.SourcelessFileLoader.load_module) methods are now deprecated. They stood as the last surviving implementations of [`importlib.abc.Loader.load_module()`](https://docs.python.org/3.14/library/importlib.html#importlib.abc.Loader.load_module) inside [`importlib`](https://docs.python.org/3.14/library/importlib.html#module-importlib) that earlier Python versions had not already deprecated in favour of [`importlib.abc.Loader.exec_module()`](https://docs.python.org/3.14/library/importlib.html#importlib.abc.Loader.exec_module).

The [`importlib.machinery.WindowsRegistryFinder`](https://docs.python.org/3.14/library/importlib.html#importlib.machinery.WindowsRegistryFinder) class is now deprecated. From 3.6.0 onward it continues to be placed onto [`sys.meta_path`](https://docs.python.org/3.14/library/sys.html#sys.meta_path) by default (on Windows), though that could shift in later releases.

[Subject index](INDEX.md) · [Previous source section](deprecated-python-modules-functions-and-methods-grp.md) · [Next source section](deprecated-python-modules-functions-and-methods-os.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](deprecated-python-modules-functions-and-methods-asynchat.md)
