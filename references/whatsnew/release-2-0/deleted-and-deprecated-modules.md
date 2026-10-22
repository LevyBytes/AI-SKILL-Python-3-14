# What’s New in Python 2.0 / Deleted and Deprecated Modules

### Deleted and Deprecated Modules

Several modules were removed, either as outdated or because superior approaches to the same job now exist. Among the departures is the `stdwin` module, which served a platform-independent windowing toolkit that is no longer being worked on.

Several modules were relocated into the `lib-old` subdirectory: `cmp`, `cmpcache`, `dircmp`, `dump`, `find`, `grep`, `packmail`, `poly`, `util`, `whatsound`, `zmod`. Should your code depend on one of the modules now sitting in `lib-old`, appending that directory to `sys.path` will restore access, though revising any code that leans on these modules is the recommended path.

[Subject index](INDEX.md) · [Previous source section](idle-improvements.md) · [Next source section](acknowledgements.md) · [Release/subject declaration](introduction.md)
