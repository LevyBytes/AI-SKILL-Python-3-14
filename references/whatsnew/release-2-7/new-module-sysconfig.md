# What’s New in Python 2.7 / New module: sysconfig — sysconfig

### New module: sysconfig

The [`sysconfig`](https://docs.python.org/3.14/library/sysconfig.html#module-sysconfig) module was lifted out of the Distutils package to stand on its own as a fresh top-level module. The functions in `sysconfig` report details such as the compiler switches, the installation paths, the platform name, plus whether the interpreter is executing out of its source tree, all part of how Python is built.

A few of the module's functions are:

- [`get_config_var()`](https://docs.python.org/3.14/library/sysconfig.html#sysconfig.get_config_var) hands back variables taken from Python's Makefile and the `pyconfig.h` file.

- [`get_config_vars()`](https://docs.python.org/3.14/library/sysconfig.html#sysconfig.get_config_vars) hands back a dictionary holding every one of the configuration variables.

-

[`get_path()`](https://docs.python.org/3.14/library/sysconfig.html#sysconfig.get_path) yields the path that has been configured for some category of module: the standard library, site-specific modules, platform-specific modules, and so on.

- [`is_python_build()`](https://docs.python.org/3.14/library/sysconfig.html#sysconfig.is_python_build) gives back true when the binary you launched comes from a Python source tree, and otherwise gives back false.

Refer to the [`sysconfig`](https://docs.python.org/3.14/library/sysconfig.html#module-sysconfig) documentation if you want further detail along with the full roster of functions.

Both the Distutils package and [`sysconfig`](https://docs.python.org/3.14/library/sysconfig.html#module-sysconfig) now fall under the maintenance of Tarek Ziadé, who additionally launched a Distutils2 package (its source repository lives at [https://hg.python.org/distutils2/](https://hg.python.org/distutils2/)) aimed at building the successor generation of Distutils.

[Subject index](INDEX.md) · [Previous source section](new-module-importlib.md) · [Release/subject declaration](the-future-for-python-2-x.md) · [Next source section](ttk-themed-widgets-for-tk.md)
