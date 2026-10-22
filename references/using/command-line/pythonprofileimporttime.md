# PYTHONPROFILEIMPORTTIME

PYTHONPROFILEIMPORTTIME

When this environment variable is set to `1`, Python reports how long each import takes. When set to `2`, Python also includes output for imported modules that were already loaded. This amounts to setting the `-X` `importtime` option.

Added in version 3.7.

Changed in version 3.14: Introduced `PYTHONPROFILEIMPORTTIME=2`, which additionally traces imports for modules already loaded.

[Subject index](INDEX.md) · [Previous source section](pythontracemalloc.md) · [Following source section](pythonasynciodebug.md)
