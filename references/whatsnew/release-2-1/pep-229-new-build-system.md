# What’s New in Python 2.1 / PEP 229: New Build System

### PEP 229: New Build System

In order to switch on assorted extra modules when compiling Python, the user previously had to dive in and edit the `Modules/Setup` file; the default selection is fairly small, confined to modules that build on the majority of Unix platforms. The upshot is that on Unix platforms boasting many more capabilities — Linux above all — Python installations frequently lack all the handy modules they might otherwise include.

Python 2.0 brought the Distutils, a collection of modules for packaging and installing extensions. With Python 2.1, the Distutils handle compiling a large portion of the standard library’s extension modules, automatically detecting which ones the current machine supports. The hope is that this renders Python installations both simpler and richer in features.

Rather than editing the `Modules/Setup` file to switch modules on, a `setup.py` script located in the top directory of the Python source distribution runs at build time and tries to determine which modules it can enable by inspecting the machine’s modules and header files. When a module is already configured in `Modules/Setup`, the `setup.py` script leaves it alone and defers to whatever the `Modules/Setup` file specifies. That gives you a means to declare any unusual command-line flags or libraries a particular platform demands.

In a further sweeping change to the build machinery, Neil Schemenauer reorganized matters so that Python now relies on a single non-recursive makefile rather than makefiles in the top directory plus one in each of the `Python/`, `Parser/`, `Objects/`, and `Modules/` subdirectories. This speeds up building Python and also leaves the Makefiles cleaner and easier to tinker with.

See also

[**PEP 229**](https://peps.python.org/pep-0229/) - Using Distutils to Build Python

Written and implemented by A.M. Kuchling.

[Subject index](INDEX.md) · [Previous source section](pep-230-warning-framework.md) · [Next source section](pep-205-weak-references.md) · [Release/subject declaration](introduction.md)
