# Python 3.7.0 alpha 4 / library / memory and lifetimes

[bpo-32422](https://bugs.python.org/issue?@action=redirect&bpo=32422): `functools.lru_cache` consumes less memory (3 words per cached key) and needs roughly a third of the time during cyclic GC.

[bpo-31993](https://bugs.python.org/issue?@action=redirect&bpo=31993): While serializing large bytes and str objects to a file, the pickler now uses less memory. Pickles built under protocol 4 will demand less memory when unpickling large bytes and str objects.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
