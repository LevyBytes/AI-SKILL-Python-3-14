# 5.4.4. __path__ attributes on modules

### 5.4.4. __path__ attributes on modules

A module's [`__path__`](https://docs.python.org/3.14/reference/datamodel.html#module.__path__) attribute ought to be a [sequence](https://docs.python.org/3.14/glossary.html#term-sequence) of strings (which may be empty) that lists every place the package's submodules can be located. By definition, any module carrying a `__path__` attribute counts as a [package](https://docs.python.org/3.14/glossary.html#term-package).

When subpackages of a package are imported, that package's [`__path__`](https://docs.python.org/3.14/reference/datamodel.html#module.__path__) attribute comes into play. Inside the import machinery it behaves quite like [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path), supplying a roster of places to look for modules while importing. That said, `__path__` is normally far narrower in scope than `sys.path`.

A package's `__path__` follows the very same rules that govern [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path). The [`sys.path_hooks`](https://docs.python.org/3.14/library/sys.html#sys.path_hooks) (covered below) are likewise consulted while walking a package's `__path__`.

The `__init__.py` file belonging to a package can assign or modify that package's [`__path__`](https://docs.python.org/3.14/reference/datamodel.html#module.__path__) attribute, and before [**PEP 420**](https://peps.python.org/pep-0420/) this was usually how namespace packages got built. Now that [**PEP 420**](https://peps.python.org/pep-0420/) has been adopted, namespace packages no longer have to ship `__init__.py` files whose only job is `__path__` manipulation; the import machinery sets `__path__` correctly for the namespace package on its own.

[Subject index](INDEX.md) · [Owning language section](the-import-system.md) · [Owning language section](loading.md) · [Previous source section](module-specs.md) · [Following source section](module-reprs.md)
