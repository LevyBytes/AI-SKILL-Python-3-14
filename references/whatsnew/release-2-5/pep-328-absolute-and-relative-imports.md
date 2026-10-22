# What's New in Python 2.5 / PEP 328: Absolute and Relative Imports — string

### PEP 328: Absolute and Relative Imports

The easier portion of [**PEP 328**](https://peps.python.org/pep-0328/) already arrived in Python 2.4: parentheses became usable for grouping the names brought in from a module via the `from ... import ...` statement, which simplifies importing a large set of distinct names.

Python 2.5 carries the trickier portion: a module's imports can be designated as either absolute or package-relative. The intent is to gradually shift toward absolute imports becoming the default in later Python releases.

Suppose you have a package directory shaped like this:

```python
pkg/
pkg/__init__.py
pkg/main.py
pkg/string.py

```

That establishes a package called `pkg` that holds the `pkg.main` and `pkg.string` submodules.

Look at the code within the `main.py` module. Suppose it runs the statement `import string`. Under Python 2.4 and earlier, it begins by checking the package's directory to carry out a relative import, locates `pkg/string.py`, brings in the contents of that file as the `pkg.string` module, and binds that module to the name `string` inside the `pkg.main` module's namespace.

That’s fine if `pkg.string` was what you wanted. But what if Python's standard [`string`](https://docs.python.org/3.14/library/string.html#module-string) module was the one you were after? There was no tidy means of skipping `pkg.string` and reaching for the standard module; in general you had to inspect what was in `sys.modules`, which is a bit unclean. Holger Krekel’s `py.std` package offers a neater approach to pulling imports from the standard library, `import py; py.std.string.join()`, yet that package isn't present on every Python installation.

Code that leans on relative imports is also harder to read, since a reader might be unsure whether [`string`](https://docs.python.org/3.14/library/string.html#module-string) or `pkg.string` is the one meant to be used. Python users quickly figured out not to reuse the names of standard library modules as the names of their packages? submodules, but there's no guarding against your submodule's name clashing with a brand-new module added in some future Python release.

Under Python 2.5 you can flip [`import`](https://docs.python.org/3.14/reference/simple_stmts.html#import)?s behaviour over to absolute imports with a `from __future__ import absolute_import` directive. That absolute-import behaviour is slated to become the default in some upcoming version (Python 2.7, most likely). Once absolute imports are the default, `import string` will reliably reach the standard library's version. The recommendation is for users to lean on absolute imports wherever they can, so it's better to start writing `from pkg import string` in your code.

You can still do relative imports by prefixing a leading period to the module name within the `from ... import` form:

```python
# Import names from pkg.string
from .string import name1, name2
# Import pkg.string
from . import string

```

That brings in the [`string`](https://docs.python.org/3.14/library/string.html#module-string) module relative to the current package, so within `pkg.main` this imports *name1* and *name2* out of `pkg.string`. Tacking on further leading periods runs the relative import beginning from the parent of the current package. As an illustration, code inside the `A.B.C` module is allowed to do:

```python
from . import D                 # Imports A.B.D
from .. import E                # Imports A.E
from ..F import G               # Imports A.F.G

```

Those leading periods can't be combined with the `import modname` form of the import statement ? only the `from ... import` form supports them.

See also

[**PEP 328**](https://peps.python.org/pep-0328/) - Imports: Multi-Line and Absolute/Relative

PEP written by Aahz; implemented by Thomas Wouters.

[https://pylib.readthedocs.io/](https://pylib.readthedocs.io/)

The py library by Holger Krekel, which contains the `py.std` package.

[Subject index](INDEX.md) · [Previous source section](pep-314-metadata-for-python-software-packages-v1-1.md) · [Next source section](pep-338-executing-modules-as-scripts.md) · [Release/subject declaration](pep-308-conditional-expressions.md)
