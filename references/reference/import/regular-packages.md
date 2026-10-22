# 5.2.1. Regular packages

### 5.2.1. Regular packages

Two flavors of package exist in Python: [regular packages](https://docs.python.org/3.14/glossary.html#term-regular-package) and [namespace packages](https://docs.python.org/3.14/glossary.html#term-namespace-package). The regular kind matches the conventional packages from Python 3.2 and before. You generally build a regular package as a directory holding an `__init__.py` file. Importing such a package causes that `__init__.py` file to run implicitly, and whatever it defines becomes bound to names inside the package’s namespace. That `__init__.py` file may hold any Python code that a normal module could hold, and Python tacks on a handful of extra attributes to the module at import time.

To illustrate, the file system arrangement below sets up a top level `parent` package containing three subpackages:

```python
parent/
    __init__.py
    one/
        __init__.py
    two/
        __init__.py
    three/
        __init__.py

```

When you import `parent.one`, both `parent/__init__.py` and `parent/one/__init__.py` run implicitly. Later imports of `parent.two` or `parent.three` will run `parent/two/__init__.py` and `parent/three/__init__.py` accordingly.

Whenever a subdirectory sitting within a regular package lacks an `__init__.py` file, it is handled as an implicit namespace package (a “namespace subpackage”) anchored to that parent. The governing specification is laid out in [**PEP 420**](https://peps.python.org/pep-0420/).

[Subject index](INDEX.md) · [Owning language section](the-import-system.md) · [Owning language section](packages.md) · [Previous source section](packages.md) · [Following source section](namespace-packages.md)
