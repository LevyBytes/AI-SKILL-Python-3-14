# Python 3.6.0 beta 3 / core and builtins / memory and lifetimes

[bpo-28509](https://bugs.python.org/issue?@action=redirect&bpo=28509): dict.update() stops over-allocating large blocks of memory.

[bpo-23782](https://bugs.python.org/issue?@action=redirect&bpo=23782): Repaired a possible memory leak inside _PyTraceback_Add() along with exception loss inside PyTraceBack_Here().

[bpo-28471](https://bugs.python.org/issue?@action=redirect&bpo=28471): Repair the "Python memory allocator called without holding the GIL" crash occurring in socket.setblocking.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
