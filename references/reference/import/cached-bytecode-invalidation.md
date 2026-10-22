# 5.4.6. Cached bytecode invalidation

### 5.4.6. Cached bytecode invalidation

Each time Python is about to read cached bytecode out of a `.pyc` file, it confirms the cache stays current relative to the `.py` source. The default approach records the source's size and last-modified timestamp into the cache file as it is written. Later, at import time, the import system verifies the cache file by comparing the metadata kept inside it with the source's own metadata.

Python additionally offers "hash-based" cache files, which keep a hash of the source's contents in place of its metadata. Hash-based `.pyc` files come in two flavours: checked and unchecked. With a checked hash-based `.pyc`, Python checks the cache by hashing the source and matching that hash against the one recorded in the cache file. Whenever a checked hash-based cache file turns out invalid, Python rebuilds it and writes a fresh checked hash-based cache file. For an unchecked hash-based `.pyc`, Python merely trusts that the cache is valid so long as it is present. You can override the validation behaviour of hash-based `.pyc` files using the [`--check-hash-based-pycs`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-check-hash-based-pycs) flag.

Changed in version 3.7: hash-based `.pyc` files were introduced. Up to then, the only bytecode-cache invalidation Python offered was timestamp-based.

[Subject index](INDEX.md) · [Owning language section](the-import-system.md) · [Owning language section](loading.md) · [Previous source section](module-reprs.md) · [Following source section](the-path-based-finder.md)
