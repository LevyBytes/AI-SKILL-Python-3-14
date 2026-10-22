# Python 3.11.0 alpha 1 / library / memory and lifetimes

[bpo-44608](https://bugs.python.org/issue?@action=redirect&bpo=44608): A memory leak in `_tkinter._flatten()` was fixed for the case where a sequence or set is passed rather than a list or tuple.

[bpo-38840](https://bugs.python.org/issue?@action=redirect&bpo=38840): Repaired `test___all__` on platforms that lack a shared memory implementation.

[bpo-41486](https://bugs.python.org/issue?@action=redirect&bpo=41486): Corrected a memory-use and copying performance regression present in the earlier 3.10 beta releases whenever an output buffer above 4GiB was used with zlib.decompress on input data that expands to that size.

[bpo-37788](https://bugs.python.org/issue?@action=redirect&bpo=37788): Fix a reference leak when a Thread object is never joined.

[bpo-45183](https://bugs.python.org/issue?@action=redirect&bpo=45183): zipimport.zipimporter.find_spec() no longer throws when its backing zip archive has vanished and the in-memory cache was cleared through invalidate_cache().

[bpo-45228](https://bugs.python.org/issue?@action=redirect&bpo=45228): Patched a stack buffer overflow occurring while a J1939 network address is parsed.

[bpo-45329](https://bugs.python.org/issue?@action=redirect&bpo=45329): Corrected freed-memory access in `pyexpat.xmlparser` when it is built against an installed expat library <= 2.2.0.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
