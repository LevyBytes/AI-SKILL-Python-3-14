# 5.5. The Path Based Finder

### 5.5. The Path Based Finder

As already noted, a handful of default meta path finders come bundled with Python. One among them, known as the [path based finder](https://docs.python.org/3.14/glossary.html#term-path-based-finder) ([`PathFinder`](https://docs.python.org/3.14/library/importlib.html#importlib.machinery.PathFinder)), scans an [import path](https://docs.python.org/3.14/glossary.html#term-import-path) made up of a list of [path entries](https://docs.python.org/3.14/glossary.html#term-path-entry). Every path entry designates a place to hunt for modules.

On its own the path based finder has no idea how to import anything. Rather, it walks each individual path entry, pairing every one with a path entry finder that does know how to deal with that specific flavour of path.

The standard collection of path entry finders covers all the logic for locating modules on the file system, dealing with particular file kinds like Python source code (`.py` files), Python byte code (`.pyc` files) and shared libraries (for example `.so` files). Where the standard library's [`zipimport`](https://docs.python.org/3.14/library/zipimport.html#module-zipimport) module provides support, the default path entry finders can additionally load every one of these file types (apart from shared libraries) out of zipfiles.

Path entries are not required to be confined to file system locations. They might point at URLs, database queries, or anything else expressible as a string.

The path based finder offers extra hooks and protocols so you are able to broaden and tailor which kinds of searchable path entries are supported. As an example, were you to want path entries given as network URLs, you could author a hook implementing HTTP semantics to track down modules on the web. That hook (a callable) would hand back a [path entry finder](https://docs.python.org/3.14/glossary.html#term-path-entry-finder) honouring the protocol laid out below, which was then employed to obtain a loader for the module off the web.

A caution: both this section and the one before it lean on the word *finder*, telling the two apart via the labels [meta path finder](https://docs.python.org/3.14/glossary.html#term-meta-path-finder) and [path entry finder](https://docs.python.org/3.14/glossary.html#term-path-entry-finder). The pair of finder types resemble each other closely, back similar protocols, and operate in comparable fashion across the import process, yet you must remember they differ in subtle ways. Specifically, meta path finders kick in right at the start of the import process, triggered off the [`sys.meta_path`](https://docs.python.org/3.14/library/sys.html#sys.meta_path) traversal.

Path entry finders, on the other hand, amount to an implementation detail belonging to the path based finder; indeed, were the path based finder pulled out of [`sys.meta_path`](https://docs.python.org/3.14/library/sys.html#sys.meta_path), not one of the path entry finder semantics would ever fire.

[Subject index](INDEX.md) · [Owning language section](the-import-system.md) · [Previous source section](cached-bytecode-invalidation.md) · [Following source section](path-entry-finders.md)
