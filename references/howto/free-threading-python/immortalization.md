# Immortalization

### Immortalization

Within the free-threaded build, certain objects are treated as [immortal](https://docs.python.org/3.14/glossary.html#term-immortal). Such objects never get deallocated and their reference counts stay fixed. The reason is to sidestep contention over reference counts, which would otherwise hinder scaling well across many threads.

For the 3.14 release, the set of immortalized objects covers only:

- Constants in code: numeric literals, string literals, and tuple literals built up from other constants.

- Strings that have been interned via [`sys.intern()`](https://docs.python.org/3.14/library/sys.html#sys.intern).

[Subject index](INDEX.md) · [Previous source context](known-limitations.md) · [Following source context](frame-objects.md)
