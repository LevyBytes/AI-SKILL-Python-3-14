# Python 3.8.0 alpha 1 / library / numeric behavior

[bpo-35780](https://bugs.python.org/issue?@action=redirect&bpo=35780): Corrected lru_cache() faults that show up in recursive, reentrant, or multi-threaded code. Such faults could leave orphan links behind and could trap the cache in a state holding fewer than the configured maximum number of links. Corrected handling of a negative maxsize, which ought to behave like zero. Corrected errors when toggling the "full" status flag. Corrected the misordering of links whenever errors arise. Brought the C code and the pure Python code into agreement for the space-saving path used by functions taking a single positional argument. Within that frequent case, the storage overhead of a single lru cache entry shrinks by nearly half. Corrected the tally of cache misses. Under error conditions the miss count had drifted away from how many times the wrapped user function actually ran.

[bpo-32968](https://bugs.python.org/issue?@action=redirect&bpo=32968): Modulo plus floor division mixing Fraction and float ought to yield float.

[bpo-35664](https://bugs.python.org/issue?@action=redirect&bpo=35664): Boosted operator.itemgetter() throughput by 33% via streamlined argument handling together with a fast path for the frequent scenario of one non-negative integer index into a tuple (the usual pattern across the standard library).

[bpo-32713](https://bugs.python.org/issue?@action=redirect&bpo=32713): Repaired tarfile.itn handling of float values that fall out of bounds. Patch by Joffrey Fuhrer.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
