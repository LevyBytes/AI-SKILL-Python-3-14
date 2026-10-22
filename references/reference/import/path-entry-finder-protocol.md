# 5.5.2. Path entry finder protocol

### 5.5.2. Path entry finder protocol

So as to back imports of modules and initialized packages and likewise to contribute portions toward namespace packages, path entry finders are obliged to provide the [`find_spec()`](https://docs.python.org/3.14/library/importlib.html#importlib.abc.PathEntryFinder.find_spec) method.

[`find_spec()`](https://docs.python.org/3.14/library/importlib.html#importlib.abc.PathEntryFinder.find_spec) accepts two arguments: the fully qualified name of the module under import, plus the (optional) target module. `find_spec()` hands back a fully populated spec for that module. Such a spec will invariably carry "loader" set (save for one exception).

So as to tell the import machinery that the spec stands for a namespace [portion](https://docs.python.org/3.14/glossary.html#term-portion), the path entry finder assigns `submodule_search_locations` a list holding the portion.

Changed in version 3.4: stepping in for `find_loader()` and `find_module()` came [`find_spec()`](https://docs.python.org/3.14/library/importlib.html#importlib.abc.PathEntryFinder.find_spec); those two are deprecated now, though they still serve when no `find_spec()` is defined.

Path entry finders of older vintage might supply one of those two deprecated methods rather than `find_spec()`. Such methods stay honoured for the sake of backward compatibility. Even so, when `find_spec()` is present on the path entry finder, the legacy methods are passed over.

`find_loader()` accepts a single argument, the fully qualified name of the module under import. `find_loader()` yields a 2-tuple in which the first element is the loader and the second element is a namespace [portion](https://docs.python.org/3.14/glossary.html#term-portion).

To stay compatible with other realizations of the import protocol, plenty of path entry finders likewise back the same long-standing `find_module()` method that meta path finders back. That said, the `find_module()` methods of path entry finders are never invoked with a `path` argument (they are presumed to have noted the relevant path information back when the path hook was first called).

A path entry finder's `find_module()` method is deprecated, since it leaves the path entry finder no way to contribute portions toward namespace packages. When both `find_loader()` and `find_module()` are present on a path entry finder, the import system will invariably call `find_loader()` ahead of `find_module()`.

Changed in version 3.10: whenever the import system invokes `find_module()` or `find_loader()`, an [`ImportWarning`](https://docs.python.org/3.14/library/exceptions.html#ImportWarning) is now triggered.

Changed in version 3.12: both `find_module()` and `find_loader()` are gone.

[Subject index](INDEX.md) · [Owning language section](the-import-system.md) · [Owning language section](the-path-based-finder.md) · [Previous source section](path-entry-finders.md) · [Following source section](replacing-the-standard-import-system.md)
