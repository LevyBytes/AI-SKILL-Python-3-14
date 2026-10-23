# What's New In Python 3.7 / PEP 552: Hash-based .pyc Files - compileall, py_compile

### PEP 552: Hash-based .pyc Files

Historically Python decided whether bytecode cache files (that is, `.pyc` files) were current by matching source metadata (the last-modified timestamp plus size) against the source metadata recorded in the cache file header at generation time. Effective though it is, this invalidation scheme has shortcomings. Should filesystem timestamps lack fine enough granularity, Python may overlook source changes, which confuses users. On top of that, keeping a timestamp inside the cache file works poorly for [build reproducibility](https://reproducible-builds.org/) and for content-based build systems.

[**PEP 552**](https://peps.python.org/pep-0552/) broadens the pyc format so a hash of the source file can drive invalidation rather than the source timestamp. Those `.pyc` files are termed "hash-based". Python keeps using timestamp-based invalidation by default and won't produce hash-based `.pyc` files while running. You can create hash-based `.pyc` files via [`py_compile`](https://docs.python.org/3.14/library/py_compile.html#module-py_compile) or [`compileall`](https://docs.python.org/3.14/library/compileall.html#module-compileall).

There are two flavors of hash-based `.pyc` files: checked and unchecked. At runtime Python checks checked hash-based `.pyc` files against their matching source files, yet skips that step for unchecked hash-based pycs. Unchecked hash-based `.pyc` files serve as a handy speed optimization wherever something outside Python (for instance the build system) takes charge of keeping `.pyc` files current.

For further details consult [Cached bytecode invalidation](https://docs.python.org/3.14/reference/import.html#pyc-invalidation).

See also

[**PEP 552**](https://peps.python.org/pep-0552/): Deterministic pycs

PEP written and implemented by Benjamin Peterson

[Subject index](INDEX.md) · [Previous source section](pep-560-core-support-for-typing-module-and-generic-types.md) · [Next source section](pep-545-python-documentation-translations.md) · [Release/subject declaration](summary-release-highlights.md)
