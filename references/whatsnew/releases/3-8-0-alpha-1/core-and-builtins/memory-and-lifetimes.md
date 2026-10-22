# Python 3.8.0 alpha 1 / core and builtins / memory and lifetimes

[bpo-34170](https://bugs.python.org/issue?@action=redirect&bpo=34170): -X dev: overriding the memory allocator through PYTHONMALLOC is now feasible even while developer mode is on.

[bpo-24618](https://bugs.python.org/issue?@action=redirect&bpo=24618): Resolved invalid memory reads that occurred when building a code object with a varnames tuple that was too small or with argument counts that were too large.

[bpo-34080](https://bugs.python.org/issue?@action=redirect&bpo=34080): Resolved a memory leak in the compiler that arose when it reported some uncommon errors while tokenizing.

[bpo-34042](https://bugs.python.org/issue?@action=redirect&bpo=34042): Correct dict.copy() so it keeps the total refcount accurate (as reported through sys.gettotalrefcount()).

[bpo-33418](https://bugs.python.org/issue?@action=redirect&bpo=33418): Resolve a possible memory leak in a function object whenever it forms a reference cycle.

[bpo-34735](https://bugs.python.org/issue?@action=redirect&bpo=34735): Resolve a memory leak inside Modules/timemodule.c. Patch by Zackery Spytz.

[bpo-33005](https://bugs.python.org/issue?@action=redirect&bpo=33005): Resolve a crash on fork while a custom memory allocator is in use (for example via the PYTHONMALLOC env var). _PyGILState_Reinit() and _PyInterpreterState_Enable() now rely on the default RAW memory allocator to allocate a fresh interpreters mutex on fork.

[bpo-33231](https://bugs.python.org/issue?@action=redirect&bpo=33231): Resolve a possible memory leak within `normalizestring()`.

[bpo-33391](https://bugs.python.org/issue?@action=redirect&bpo=33391): Resolve a leak within set_symmetric_difference().

[bpo-35214](https://bugs.python.org/issue?@action=redirect&bpo=35214): Repaired an out of bounds memory access while parsing a truncated unicode escape sequence at the tail of a string like `'\N'`. It would read a single byte past the end of the memory allocation.

[bpo-35720](https://bugs.python.org/issue?@action=redirect&bpo=35720): Repaired a small memory leak within the pymain_parse_cmdline_impl function in Modules/main.c

[bpo-35436](https://bugs.python.org/issue?@action=redirect&bpo=35436): Repair assorted problems with memory allocation error handling. Patch by Zackery Spytz.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
