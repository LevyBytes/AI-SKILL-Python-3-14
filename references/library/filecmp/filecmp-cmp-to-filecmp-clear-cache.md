# filecmp`filecmp` - File and Directory Comparisons

### `filecmp` - File and Directory Comparisons

**Source code:** [Lib/filecmp.py](https://github.com/python/cpython/tree/3.14/Lib/filecmp.py)

---

Functions for putting files and directories side by side — each offering its own optional balance between speed and accuracy — live in the `filecmp` module. When it is files you want to compare, the [`difflib`](https://docs.python.org/3.14/library/difflib.html#module-difflib) module is also worth a look.

These are the functions exposed by the `filecmp` module:

 filecmp.cmp(*f1*, *f2*, *shallow=True*)

Pit the two files `f1` and `f2` against each other, yielding `True` when they look the same and `False` if not.

Should `shallow` be true and the [`os.stat()`](https://docs.python.org/3.14/library/os.html#os.stat) signatures — that is, file type, size, and modification time — line up for both files, the pair is judged equal.

Failing that, a mismatch in either size or content marks the files as unequal.

Keep in mind that this function invokes no outside programs, which is what makes it both portable and quick.

Earlier comparisons and their outcomes are kept in a cache by this function, and any given entry is thrown out whenever the file's [`os.stat()`](https://docs.python.org/3.14/library/os.html#os.stat) data shifts. To wipe the cache in full, call `clear_cache()`.

 filecmp.cmpfiles(*dir1*, *dir2*, *common*, *shallow=True*)

Across the pair of directories `dir1` and `dir2`, compare the files whose names appear in `common`.

Three filename lists come back: `match`, `mismatch`, and `errors`. The first, `match`, holds the files that agree; `mismatch` records those that disagree; and `errors` names the files that defied comparison altogether. A file lands in `errors` when it is absent from one directory, when the user has no read permission for it, or when the comparison failed for some other reason.

Here the `shallow` parameter carries the identical sense and default it had in `filecmp.cmp()`.

To illustrate, `cmpfiles('a', 'b', ['c', 'd/e'])` pairs `a/c` against `b/c` along with `a/d/e` against `b/d/e`. Each of `'c'` and `'d/e'` then turns up in exactly one of the three lists handed back.

 filecmp.clear_cache()

Empty out the filecmp cache. That can come in handy when a file gets compared so soon after being changed that the gap falls inside the mtime granularity of the filesystem beneath it.

Added in version 3.4.

[Subject index](INDEX.md) · [Previous](file-and-directory-comparisons.md) · [Continue](filecmp-dircmp-class.md)
