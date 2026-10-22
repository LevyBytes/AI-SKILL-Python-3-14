# os: Filesystem flag updates with chflags

os.chflags(*path*, *flags*, ***, *follow_symlinks=True*)

Assign the flags of *path* to the numeric *flags*. *flags* may hold a combination (bitwise OR) of the values below (as declared in the [`stat`](https://docs.python.org/3.14/library/stat.html#module-stat) module):

- [`stat.UF_NODUMP`](https://docs.python.org/3.14/library/stat.html#stat.UF_NODUMP)

- [`stat.UF_IMMUTABLE`](https://docs.python.org/3.14/library/stat.html#stat.UF_IMMUTABLE)

- [`stat.UF_APPEND`](https://docs.python.org/3.14/library/stat.html#stat.UF_APPEND)

- [`stat.UF_OPAQUE`](https://docs.python.org/3.14/library/stat.html#stat.UF_OPAQUE)

- [`stat.UF_NOUNLINK`](https://docs.python.org/3.14/library/stat.html#stat.UF_NOUNLINK)

- [`stat.UF_COMPRESSED`](https://docs.python.org/3.14/library/stat.html#stat.UF_COMPRESSED)

- [`stat.UF_HIDDEN`](https://docs.python.org/3.14/library/stat.html#stat.UF_HIDDEN)

- [`stat.SF_ARCHIVED`](https://docs.python.org/3.14/library/stat.html#stat.SF_ARCHIVED)

- [`stat.SF_IMMUTABLE`](https://docs.python.org/3.14/library/stat.html#stat.SF_IMMUTABLE)

- [`stat.SF_APPEND`](https://docs.python.org/3.14/library/stat.html#stat.SF_APPEND)

- [`stat.SF_NOUNLINK`](https://docs.python.org/3.14/library/stat.html#stat.SF_NOUNLINK)

- [`stat.SF_SNAPSHOT`](https://docs.python.org/3.14/library/stat.html#stat.SF_SNAPSHOT)

This function can support not following symlinks.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `os.chflags` with arguments `path`, `flags`.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI.

Changed in version 3.3: Added the *follow_symlinks* parameter.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

[Subject index](INDEX.md) · [Previous](os-f-ok-to-os-chdir.md) · [Continue](os-chmod-to-stat-s-ixoth.md) · [Owning module, declaration or section: os](os-error-to-os-name.md) · [Owning module, declaration or section: Files and Directories](os-access.md)
