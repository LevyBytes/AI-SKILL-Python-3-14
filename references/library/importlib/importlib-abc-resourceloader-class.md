# importlib: `importlib.abc.ResourceLoader`

*class *importlib.abc.ResourceLoader

*Superseded by TraversableResources*

>

An abstract base class for a [loader](https://docs.python.org/3.14/glossary.html#term-loader) that provides the optional [**PEP 302**](https://peps.python.org/pep-0302/) protocol for pulling arbitrary resources out of the storage back-end.

Deprecated since version 3.7: This ABC has been deprecated, with resource loading instead routed through [`importlib.resources.abc.TraversableResources`](https://docs.python.org/3.14/library/importlib.resources.abc.html#importlib.resources.abc.TraversableResources). It remains only to stay backwards-compatible with the other ABCs in this module.

 *abstractmethod *get_data(*path*)

>

An abstract method that yields the bytes of the data sitting at *path*. A loader whose file-like storage back-end can hold arbitrary data may implement this abstract method to expose that stored data directly. When *path* cannot be located, [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) is to be raised. The expectation is that *path* was built from a module's [`__file__`](https://docs.python.org/3.14/reference/datamodel.html#module.__file__) attribute or from one of the entries in a package's [`__path__`](https://docs.python.org/3.14/reference/datamodel.html#module.__path__).

Changed in version 3.4: Raises [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) instead of [`NotImplementedError`](https://docs.python.org/3.14/library/exceptions.html#NotImplementedError).

[Subject index](INDEX.md) · [Previous](importlib-abc-loader-class-to-module-loader.md) · [Continue](abstract-inspect-loader.md) · [Owning module, declaration or section: `importlib.abc` ? Abstract base classes related to import](importlib-abc-metapathfinder-class.md)
