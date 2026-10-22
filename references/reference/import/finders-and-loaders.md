# 5.3.2. Finders and loaders

### 5.3.2. Finders and loaders

When the requested module is absent from [`sys.modules`](https://docs.python.org/3.14/library/sys.html#sys.modules), Python’s import protocol takes over to locate and load it. That protocol is built around two conceptual objects: [finders](https://docs.python.org/3.14/glossary.html#term-finder) and [loaders](https://docs.python.org/3.14/glossary.html#term-loader). A finder is tasked with deciding whether the named module is something it can locate by whatever method it understands. When an object satisfies both interfaces, it is called an [importer](https://docs.python.org/3.14/glossary.html#term-importer) — such objects hand back themselves once they recognize that they are able to load the requested module.

Several default finders and importers ship with Python. The first of them understands how to find built-in modules, while the second understands how to find frozen modules. Yet another default finder scans an [import path](https://docs.python.org/3.14/glossary.html#term-import-path) for modules. That import path is a roster of locations, which may identify file system paths or zip files. It is also open to extension so it can search for any resource that can be located, including those addressed by URLs.

Because the import machinery is extensible, fresh finders can be plugged in to widen the reach and breadth of module searching.

Loading modules is not actually the finders’ job. Once they locate the named module, they hand back a *module spec*, which packages up the module’s import-related details that the import machinery later draws on while loading the module.

In the sections that follow, the finder-and-loader protocol is covered in greater depth, including how you might build and register new ones to broaden the import machinery.

Changed in version 3.4: With earlier Python releases, finders gave back [loaders](https://docs.python.org/3.14/glossary.html#term-loader) directly, while these days they return module specs that *contain* loaders. Loaders remain part of import but shoulder fewer responsibilities now.

[Subject index](INDEX.md) · [Owning language section](the-import-system.md) · [Owning language section](searching.md) · [Previous source section](the-module-cache.md) · [Following source section](import-hooks.md)
