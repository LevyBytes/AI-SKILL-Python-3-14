# module.__file__ / module.__cached__

module.__file__

 module.__cached__

Both `__file__` and `__cached__` are optional attributes that may or may not have a value. When present, each ought to be a [`str`](https://docs.python.org/3.14/library/stdtypes.html#str).

`__file__` records the pathname of whichever file supplied the module (when a file was the source), or, for extension modules that load on the fly out of a shared library, the pathname of that shared library file. It can be absent for some kinds of modules, like C modules statically linked into the interpreter, and the [import system](https://docs.python.org/3.14/reference/import.html#importsystem) may choose to leave it unset when it conveys no semantic meaning (say, a module loaded out of a database).

When `__file__` has a value, the `__cached__` attribute may have one too, pointing at any compiled rendition of the code (for example, a byte-compiled file). That file need not actually exist for this attribute to be set; the path can merely indicate where the compiled file *would* exist (consult [**PEP 3147**](https://peps.python.org/pep-3147/)).

Observe that `__cached__` can carry a value even when `__file__` does not. That situation, however, is rather uncommon. In the end it is the [loader](https://docs.python.org/3.14/glossary.html#term-loader) that draws on the module spec supplied by the [finder](https://docs.python.org/3.14/glossary.html#term-finder) (and `__file__` plus `__cached__` derive from that spec). Hence if a loader is able to load from a cached module yet does not otherwise load from a file, that uncommon situation can be fitting.

You are **strongly** advised to reach for [`module.__spec__.cached`](https://docs.python.org/3.14/library/importlib.html#importlib.machinery.ModuleSpec.cached) rather than `module.__cached__`.

Deprecated since version 3.13, will be removed in version 3.15: It is deprecated to set `__cached__` on a module while leaving `__spec__.cached` unset. As of Python 3.15, `__cached__` will no longer be set or consulted by the import system or standard library.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](the-standard-type-hierarchy.md) · [Owning language section](modules.md) · [Owning language section](import-related-attributes-on-module-objects.md) · [Previous source section](module-path.md) · [Following source section](other-writable-attributes-on-module-objects.md)
