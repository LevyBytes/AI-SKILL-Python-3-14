# Python 3.7.0 alpha 2 / core and builtins / fresh api gc freeze lets you shift every object garbage

[bpo-31558](https://bugs.python.org/issue?@action=redirect&bpo=31558): A fresh API, `gc.freeze()`, lets you shift every object the garbage collector currently tracks into a permanent generation, which effectively drops them out of later collection events. You can use this to keep such objects from having their PyGC_Head mutated. The upshot is excellent copy-on-write stability across fork().

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
