# What's New In Python 3.2 / sysconfig — sysconfig

### sysconfig

With the brand-new [`sysconfig`](https://docs.python.org/3.14/library/sysconfig.html#module-sysconfig) module it becomes easy to find install paths plus configuration values that differ between platforms and between individual installations.

This module hands you simple lookup functions covering both platform and version data:

- [`get_platform()`](https://docs.python.org/3.14/library/sysconfig.html#sysconfig.get_platform) yields strings of the form *linux-i586* or *macosx-10.6-ppc*.

- [`get_python_version()`](https://docs.python.org/3.14/library/sysconfig.html#sysconfig.get_python_version) hands back a Python version string like “3.2”.

You also get the paths and variables tied to any of seven named schemes that `distutils` relies on. The set comprises *posix_prefix*, *posix_home*, *posix_user*, *nt*, *nt_user*, *os2*, *os2_home*:

- [`get_paths()`](https://docs.python.org/3.14/library/sysconfig.html#sysconfig.get_paths) builds a dictionary holding the install paths tied to the active installation scheme.

- [`get_config_vars()`](https://docs.python.org/3.14/library/sysconfig.html#sysconfig.get_config_vars) gives back a dictionary of variables that are platform specific.

A handy command-line entry point is offered as well:

```doscon
C:\Python32>python -m sysconfig
Platform: "win32"
Python version: "3.2"
Current installation scheme: "nt"

Paths:
        data = "C:\Python32"
        include = "C:\Python32\Include"
        platinclude = "C:\Python32\Include"
        platlib = "C:\Python32\Lib\site-packages"
        platstdlib = "C:\Python32\Lib"
        purelib = "C:\Python32\Lib\site-packages"
        scripts = "C:\Python32\Scripts"
        stdlib = "C:\Python32\Lib"

Variables:
        BINDIR = "C:\Python32"
        BINLIBDEST = "C:\Python32\Lib"
        EXE = ".exe"
        INCLUDEPY = "C:\Python32\Include"
        LIBDEST = "C:\Python32\Lib"
        SO = ".pyd"
        VERSION = "32"
        abiflags = ""
        base = "C:\Python32"
        exec_prefix = "C:\Python32"
        platbase = "C:\Python32"
        prefix = "C:\Python32"
        projectbase = "C:\Python32"
        py_version = "3.2"
        py_version_nodot = "32"
        py_version_short = "3.2"
        srcdir = "C:\Python32"
        userbase = "C:\Documents and Settings\Raymond\Application Data\Python"

```

(Moved out of Distutils by Tarek Ziadé.)

[Subject index](INDEX.md) · [Previous source section](site.md) · [Next source section](pdb.md) · [Release/subject declaration](pep-384-defining-a-stable-abi.md)
