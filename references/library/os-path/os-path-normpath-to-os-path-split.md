# os.path: `os.path.normpath()`, `os.path.realpath()`, `os.path.ALLOW_MISSING`, `os.path.relpath()`, `os.path.samefile()`, `os.path.sameopenfile()`, `os.path.samestat()`, `os.path.split()`

os.path.normpath(*path*)

Bring a pathname into a normal form by squeezing out redundant separators and up-level references, so that `A//B`, `A/B/`, `A/./B` and `A/foo/../B` all turn into `A/B`. Where symbolic links are present, this string manipulation can alter what a path means. Under Windows, forward slashes become backward slashes. For case normalization, reach for `normcase()`.

Note

Under POSIX systems, per [IEEE Std 1003.1 2013 Edition; 4.13 Pathname Resolution](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap04.html#tag_04_13), when a pathname opens with exactly two slashes, the first component after those leading characters may be read in an implementation-defined way, though anything beyond two leading characters is to be handled as one single character.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

 os.path.realpath(*path*, */*, ***, *strict=False*)

Hand back the canonical path for the named filename, removing any symbolic links met along the path (where the operating system supports them). Under Windows, this routine additionally resolves MS-DOS (also termed 8.3) style names like `C:\\PROGRA~1` into `C:\\Program Files`.

By default, evaluation of the path proceeds up to the first component that is absent, forms a symlink loop, or whose evaluation triggers [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError). Every such component is tacked on unchanged to the portion of the path already resolved.

Among the errors handled in this fashion are "access denied", "not a directory", and "bad argument to internal function". The path that results may therefore be absent or unreachable, may yet hold links or loops, and may pass through non-directories.

Keyword arguments let you alter this behavior:

When *strict* is `True`, the very first error met while evaluating the path is re-raised. Specifically, [`FileNotFoundError`](https://docs.python.org/3.14/library/exceptions.html#FileNotFoundError) gets raised when *path* is absent, or a different [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) when it is otherwise unreachable.

When *strict* is `os.path.ALLOW_MISSING`, every error apart from [`FileNotFoundError`](https://docs.python.org/3.14/library/exceptions.html#FileNotFoundError) is re-raised (just as with `strict=True`). The path that comes back will accordingly hold no symbolic links, though the named file together with some of its parent directories may be absent.

Note

What this function does is mimic the operating system's own way of canonicalizing a path, and that way differs a little between Windows and UNIX in how links and the path components that follow them interact.

Since operating system APIs canonicalize paths whenever required, calling this function is not usually needed.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

Changed in version 3.8: Under Windows, both junctions and symbolic links now get resolved.

Changed in version 3.10: The *strict* parameter was added.

Changed in version 3.14: For the *strict* parameter, the `ALLOW_MISSING` value became available.

 os.path.ALLOW_MISSING

Special value used for the *strict* argument in `realpath()`.

Added in version 3.14.

 os.path.relpath(*path*, *start=os.curdir*)

Hand back a relative filepath leading to *path*, measured from the current directory or, when supplied, from an optional *start* directory. The work is purely a path computation: the filesystem goes untouched, so neither the existence nor the nature of *path* or *start* is checked. Under Windows, a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised whenever *path* and *start* sit on different drives.

*start* defaults to [`os.curdir`](https://docs.python.org/3.14/library/os.html#os.curdir).

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

 os.path.samefile(*path1*, *path2*, */*)

Yield `True` when both pathname arguments point at the same file or directory. This is judged by the device number together with the i-node number, and an exception is raised should an [`os.stat()`](https://docs.python.org/3.14/library/os.html#os.stat) call on either pathname fail.

Changed in version 3.2: Added Windows support.

Changed in version 3.4: the implementation Windows relies on is now identical to that of every other platform.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

 os.path.sameopenfile(*fp1*, *fp2*)

Yield `True` when the file descriptors *fp1* and *fp2* point at the same file.

Changed in version 3.2: Added Windows support.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

 os.path.samestat(*stat1*, *stat2*, */*)

Yield `True` when the stat tuples *stat1* and *stat2* point at the same file. Such structures may have come from [`os.fstat()`](https://docs.python.org/3.14/library/os.html#os.fstat), [`os.lstat()`](https://docs.python.org/3.14/library/os.html#os.lstat), or [`os.stat()`](https://docs.python.org/3.14/library/os.html#os.stat). This function provides the comparison underlying both `samefile()` and `sameopenfile()`.

Changed in version 3.4: Added Windows support.

 os.path.split(*path*, */*)

Break the pathname *path* apart into a pair, `(head, tail)`, in which *tail* is the final pathname component and *head* covers everything before it. A slash will never appear in the *tail* part; when *path* finishes with a slash, *tail* turns out empty. With no slash anywhere in *path*, *head* turns out empty. When *path* itself is empty, both *head* and *tail* are empty. Trailing slashes get trimmed off *head*, except where it is the root (nothing but one or more slashes). Across every case, `join(head, tail)` yields a path to the same place as *path* (though the two strings can differ). The functions `join()`, `dirname()` and `basename()` are also worth consulting.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

[Subject index](INDEX.md) · [Previous](os-path-isjunction-to-os-path-normcase.md) · [Continue](os-path-splitdrive-to-os-path-splitroot.md) · [Owning module, declaration or section: os.path](os-path-abspath-to-os-path-dirname.md)
