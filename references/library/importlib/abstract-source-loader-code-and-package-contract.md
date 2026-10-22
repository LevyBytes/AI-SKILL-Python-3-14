# importlib: `get_code()`, `exec_module()`, `load_module()`, `get_source()`, `is_package()`

An optional abstract method that persists the given bytes to a particular file path. Where intermediate directories along that path are missing, the implementation should bring them into being on its own.

Should the write fail because the destination is read-only ([`errno.EACCES`](https://docs.python.org/3.14/library/errno.html#errno.EACCES)/[`PermissionError`](https://docs.python.org/3.14/library/exceptions.html#PermissionError)), the resulting exception must be swallowed rather than re-raised.

Changed in version 3.4: No longer raises [`NotImplementedError`](https://docs.python.org/3.14/library/exceptions.html#NotImplementedError) when called.

 get_code(*fullname*)

Concrete implementation of `InspectLoader.get_code()`.

 exec_module(*module*)

Concrete implementation of `Loader.exec_module()`.

Added in version 3.4.

 load_module(*fullname*)

Concrete implementation of `Loader.load_module()`.

Deprecated since version 3.4, slated for removal in 3.15: rely on `exec_module()` going forward.

 get_source(*fullname*)

Concrete implementation of `InspectLoader.get_source()`.

 is_package(*fullname*)

Concrete implementation of `InspectLoader.is_package()`. The module counts as a package when its file path (returned by `ExecutionLoader.get_filename()`) names a file called `__init__` once the extension is dropped, **and** the module name does not itself terminate in `__init__`.

[Subject index](INDEX.md) · [Continue](../importlib-machinery/importable-file-suffixes.md) · [Owning module, declaration or section: importlib.abc.SourceLoader](abstract-source-loader-path-and-data-contract.md) · [Owning module, declaration or section: `importlib.abc` ? Abstract base classes related to import](importlib-abc-metapathfinder-class.md) · [Owning module, declaration or section: set_data](abstract-source-loader-path-and-data-contract.md) · [Preceding source contract and version conditions](abstract-source-loader-path-and-data-contract.md)
