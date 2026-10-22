# importlib: Loader execution and module-attribute initialization

*class *importlib.abc.Loader

An abstract base class for a [loader](https://docs.python.org/3.14/glossary.html#term-loader). The precise definition of a loader appears in [**PEP 302**](https://peps.python.org/pep-0302/).

Any loader that wants to offer resource reading ought to provide a `get_resource_reader()` method matching the specification in [`importlib.resources.abc.ResourceReader`](https://docs.python.org/3.14/library/importlib.resources.abc.html#importlib.resources.abc.ResourceReader).

Changed in version 3.7: Introduced the optional `get_resource_reader()` method.

 create_module(*spec*)

A method that yields the module object to be used while a module is being imported. Returning `None` here signals that the default module-creation semantics should apply.

Added in version 3.4.

Changed in version 3.6: Once `exec_module()` is defined, this method ceases to be optional.

 exec_module(*module*)

An abstract method that runs the module inside its own namespace whenever a module is imported or reloaded. By the time `exec_module()` runs, the module ought already to be initialized. Wherever this method is present, `create_module()` has to be defined.

Added in version 3.4.

Changed in version 3.6: `create_module()` must also be defined.

 load_module(*fullname*)

A legacy way to load a module. When the module cannot be loaded, [`ImportError`](https://docs.python.org/3.14/library/exceptions.html#ImportError) is raised; otherwise the loaded module comes back.

When the module being requested is already present in [`sys.modules`](https://docs.python.org/3.14/library/sys.html#sys.modules), that existing module should be taken and reloaded. Failing that, the loader ought to build a new module and put it into `sys.modules` ahead of any loading, so that the import does not recurse. If the loader did add a module and the load then fails, the loader has to take that module back out of `sys.modules`; anything that was sitting in `sys.modules` before the loader started should be left untouched.

The loader ought to assign a number of attributes on the module (keep in mind that reloading a module can change some of these attributes):

- [`module.__name__`](https://docs.python.org/3.14/reference/datamodel.html#module.__name__)

- [`module.__file__`](https://docs.python.org/3.14/reference/datamodel.html#module.__file__)

- [`module.__cached__`](https://docs.python.org/3.14/reference/datamodel.html#module.__cached__) *(deprecated)*

- [`module.__path__`](https://docs.python.org/3.14/reference/datamodel.html#module.__path__)

- [`module.__package__`](https://docs.python.org/3.14/reference/datamodel.html#module.__package__) *(deprecated)*

- [`module.__loader__`](https://docs.python.org/3.14/reference/datamodel.html#module.__loader__) *(deprecated)*

Where `exec_module()` is present, backwards-compatible behavior is supplied.

Changed in version 3.4: A call now raises [`ImportError`](https://docs.python.org/3.14/library/exceptions.html#ImportError) rather than [`NotImplementedError`](https://docs.python.org/3.14/library/exceptions.html#NotImplementedError). The functionality is supplied wherever `exec_module()` exists.

Deprecated since version 3.4, will be removed in version 3.15: For loading a module, `exec_module()` (together with `create_module()`) is the API to prefer. Have loaders provide that in place of `load_module()`. Once `exec_module()` is implemented, the import machinery looks after every other duty that `load_module()` used to cover.

[Subject index](INDEX.md) · [Previous](path-entry-finder-contract.md) · [Continue](importlib-abc-resourceloader-class.md) · [Owning module, declaration or section: `importlib.abc` ? Abstract base classes related to import](importlib-abc-metapathfinder-class.md)
