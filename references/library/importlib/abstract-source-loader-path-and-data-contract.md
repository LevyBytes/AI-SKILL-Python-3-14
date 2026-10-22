# importlib: `importlib.abc.SourceLoader`, `ResourceLoader.get_data()`, `ExecutionLoader.get_filename()`, `path_stats()`, `path_mtime()`, `set_data()`

*class *importlib.abc.SourceLoader

An abstract base class for putting together loading of source files (and, when you want, bytecode files). It draws from both `ResourceLoader` and `ExecutionLoader`, and asks you to implement:

- `ResourceLoader.get_data()`

- `ExecutionLoader.get_filename()`

Only the path to the source file should come back; sourceless loading has no support here.

The abstract methods this class declares exist to layer on optional bytecode file support. Leave those optional methods unimplemented (or let them raise [`NotImplementedError`](https://docs.python.org/3.14/library/exceptions.html#NotImplementedError)) and the loader handles source code alone. Provide them and the loader can deal with source *and* bytecode files; even so, this does not enable *sourceless* loading where bytecode is all you have. Bytecode files serve as an optimization that quickens loading by dropping the parsing stage of Python's compiler, which is why no bytecode-specific API gets exposed.

 path_stats(*path*)

Optional abstract method that yields a [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict) holding metadata about the given path. The dictionary keys it supports are:

- `'mtime'` (mandatory): an integer, or a floating-point value, that conveys when the source code was last modified;

- `'size'` (optional): the size in bytes of the source code.

Every other key in the dictionary is disregarded, leaving room for later extensions. When the path cannot be handled, [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) is raised.

Added in version 3.3.

Changed in version 3.4: Raise [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) instead of [`NotImplementedError`](https://docs.python.org/3.14/library/exceptions.html#NotImplementedError).

 path_mtime(*path*)

Optional abstract method that yields the modification time of the given path.

Deprecated since version 3.3: `path_stats()` has taken over from this deprecated method. Implementing it is not required, though it stays around for compatibility's sake. Raise [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) if the path cannot be handled.

Changed in version 3.4: Raise [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) instead of [`NotImplementedError`](https://docs.python.org/3.14/library/exceptions.html#NotImplementedError).

 set_data(*path*, *data*)

[Subject index](INDEX.md) · [Previous](abstract-file-loader.md) · [Owning module, declaration or section: `importlib.abc` ? Abstract base classes related to import](importlib-abc-metapathfinder-class.md) · [Required continuation of the source contract](abstract-source-loader-code-and-package-contract.md)
