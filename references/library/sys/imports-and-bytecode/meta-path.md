# sys.meta_path

sys.meta_path

A list of [meta path finder](https://docs.python.org/3.14/glossary.html#term-meta-path-finder) objects whose [`find_spec()`](https://docs.python.org/3.14/library/importlib.html#importlib.abc.MetaPathFinder.find_spec) methods are invoked to determine whether one of the objects can locate the module that is to be imported. By default it carries entries that supply Python’s standard import behavior. The `find_spec()` method receives at minimum the absolute name of the module being imported. When the module to import sits inside a package, the parent package’s [`__path__`](https://docs.python.org/3.14/reference/datamodel.html#module.__path__) attribute is supplied as a second argument. The method yields a [module spec](https://docs.python.org/3.14/glossary.html#term-module-spec), or `None` when the module cannot be located.

See also

[`importlib.abc.MetaPathFinder`](https://docs.python.org/3.14/library/importlib.html#importlib.abc.MetaPathFinder)

The abstract base class that lays out the interface of finder objects on `meta_path`.

[`importlib.machinery.ModuleSpec`](https://docs.python.org/3.14/library/importlib.html#importlib.machinery.ModuleSpec)

The concrete class whose instances [`find_spec()`](https://docs.python.org/3.14/library/importlib.html#importlib.abc.MetaPathFinder.find_spec) is expected to return.

Changed in version 3.4: [Module specs](https://docs.python.org/3.14/glossary.html#term-module-spec) arrived in Python 3.4, through [**PEP 451**](https://peps.python.org/pep-0451/).

Changed in version 3.12: Dropped the fallback that searched for a `find_module()` method whenever a `meta_path` entry lacked a [`find_spec()`](https://docs.python.org/3.14/library/importlib.html#importlib.abc.MetaPathFinder.find_spec) method.

[API family](INDEX.md) · [sys context index](../INDEX.md).
