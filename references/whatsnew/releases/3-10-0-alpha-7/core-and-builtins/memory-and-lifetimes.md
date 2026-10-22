# Python 3.10.0 alpha 7 / core and builtins / memory and lifetimes

[bpo-37448](https://bugs.python.org/issue?@action=redirect&bpo=37448): Introduce a radix-tree-based memory map for tracking which obmalloc arenas are in use, replacing the former address_in_range() implementation. With the radix tree, growing pool sizes past the OS page size becomes straightforward. Larger pools and arenas let obmalloc satisfy a much greater share of requests via its ultra-fast code paths.

A further benefit is that it removes the memory-unsanitary behavior of the old address_in_range(). That earlier address_in_range() carried the _Py_NO_SANITIZE_ADDRESS, _Py_NO_SANITIZE_THREAD, and _Py_NO_SANITIZE_MEMORY annotations, none of which are required any longer.

You can turn the radix tree map off by defining this preprocessor flag: `-DWITH_PYMALLOC_RADIX_TREE=0`.

Co-authored-by: Tim Peters <[tim.peters@gmail.com](mailto:tim.peters%40gmail.com)>

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
