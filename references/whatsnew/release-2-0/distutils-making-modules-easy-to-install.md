# What’s New in Python 2.0 / Distutils: Making Modules Easy to Install

### Distutils: Making Modules Easy to Install

In the days before Python 2.0, installing modules was a wearisome task – nothing told you automatically where Python sat or which compiler flags extension modules needed. Authors of software had to endure a painful routine of hand-editing Makefiles and configuration files that really only functioned on Unix, leaving Windows and MacOS out in the cold. Python users were confronted with installation instructions that differed wildly from one extension package to the next, turning the upkeep of a Python installation into a bit of a slog.

The SIG devoted to distribution utilities, led by Greg Ward, built the Distutils, a system that greatly simplifies package installation. It makes up the `distutils` package, a fresh addition to Python’s standard library. Ideally, installing a Python module from source takes the same steps each time: you just unpack the tarball or zip archive and then run “`python setup.py install`”. The platform gets detected automatically, the compiler is recognized, C extension modules get compiled, and the distribution lands in the right directory. Optional command-line arguments give you finer control over how installation proceeds, the distutils package supplies many hooks for overriding defaults – splitting the build from the install, building or installing somewhere other than the default directories, and so on.

To make use of the Distutils, you have to author a `setup.py` script. In the simplest scenario, where the software is made up of nothing but .py files, a bare-bones `setup.py` need only run a handful of lines:

```python
from distutils.core import setup
setup (name = "foo", version = "1.0",
       py_modules = ["module1", "module2"])

```

The `setup.py` file grows only slightly more involved when the software is split across a few packages:

```python
from distutils.core import setup
setup (name = "foo", version = "1.0",
       packages = ["package", "package.subpackage"])

```

The trickiest scenario is a C extension; below is an example lifted from the PyXML package:

```python
from distutils.core import setup, Extension

expat_extension = Extension('xml.parsers.pyexpat',
     define_macros = [('XML_NS', None)],
     include_dirs = [ 'extensions/expat/xmltok',
                      'extensions/expat/xmlparse' ],
     sources = [ 'extensions/pyexpat.c',
                 'extensions/expat/xmltok/xmltok.c',
                 'extensions/expat/xmltok/xmlrole.c', ]
       )
setup (name = "PyXML", version = "0.5.4",
       ext_modules =[ expat_extension ] )

```

The Distutils can likewise handle building source and binary distributions. The “sdist” command, invoked by “`python setup.py sdist`’, produces a source distribution such as `foo-1.0.tar.gz`. Tacking on new commands is easy: “bdist_rpm” and “bdist_wininst” commands have already been contributed to build an RPM distribution and a Windows installer for the software, respectively. Commands for other distribution formats such as Debian packages and Solaris `.pkg` files are at differing points of development.

The whole thing is covered in a brand-new manual, *Distributing Python Modules*, that joins the core set of Python documentation.

[Subject index](INDEX.md) · [Previous source section](extending-embedding-changes.md) · [Next source section](xml-modules.md) · [Release/subject declaration](introduction.md)
