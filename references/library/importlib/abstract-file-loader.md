# importlib: `importlib.abc.FileLoader`, `load_module()`

*class *importlib.abc.FileLoader(*fullname*, *path*)

An abstract base class deriving from `ResourceLoader` and `ExecutionLoader` that furnishes concrete implementations of `ResourceLoader.get_data()` and `ExecutionLoader.get_filename()`.

The *fullname* argument is the fully resolved name of the module that the loader is meant to handle. The *path* argument gives the path to that module's file.

Added in version 3.3.

 name

The name of the module the loader can handle.

 path

Path to the file of the module.

 load_module(*fullname*)

Calls super's `load_module()`.

Deprecated since version 3.4, will be removed in version 3.15: turn to `Loader.exec_module()` rather than this.

 *abstractmethod *get_filename(*fullname*)

Returns `path`.

 *abstractmethod *get_data(*path*)

Reads *path* as a binary file and returns the bytes from it.

[Subject index](INDEX.md) · [Previous](importlib-abc-executionloader-class.md) · [Continue](abstract-source-loader-path-and-data-contract.md) · [Owning module, declaration or section: `importlib.abc` ? Abstract base classes related to import](importlib-abc-metapathfinder-class.md)
