# shutil`shutil` - High-level file operations

### `shutil` - High-level file operations

**Source code:** [Lib/shutil.py](https://github.com/python/cpython/tree/3.14/Lib/shutil.py)

---

A range of high-level routines for working with files and groups of files is provided by the `shutil` module. Notably, it includes functions that handle copying and deleting files. To act on single files, consult the [`os`](https://docs.python.org/3.14/library/os.html#module-os) module as well.

Warning

Not even the more capable copying functions (`shutil.copy()`, `shutil.copy2()`) are able to reproduce every piece of file metadata.

On POSIX systems, this results in the file's owner and group being dropped, along with its ACLs. Under Mac OS, neither the resource fork nor other metadata are carried over — so those resources vanish, and the file's type and creator codes end up wrong. Under Windows, the file's owners, ACLs, and alternate data streams go uncopied.

[Subject index](INDEX.md) · [Continue](shutil-copyfileobj-to-shutil-copystat.md)
