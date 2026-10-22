# os.path / Common pathname manipulations: Path existence, expansion, timestamps and file-type queries

os.path.exists(*path*)

Yield `True` when *path* names an existing path or an open file descriptor. Broken symbolic links yield `False`. On certain platforms, this routine can yield `False` when permission to run [`os.stat()`](https://docs.python.org/3.14/library/os.html#os.stat) on the requested file is denied, even though the *path* really is there.

Changed in version 3.3: an integer is now allowed for *path*: an open file descriptor yields `True`, and anything else yields `False`.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

 os.path.lexists(*path*)

Yield `True` when *path* names an existing path, broken symbolic links included. On platforms without [`os.lstat()`](https://docs.python.org/3.14/library/os.html#os.lstat), this behaves the same as `exists()`.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

 os.path.expanduser(*path*)

Across Unix and Windows, hand back the argument after swapping any leading `~` or `~user` component for that *user*'s home directory.

Under Unix, a leading `~` becomes the value of the environment variable `HOME` when that is set; failing that, the home directory of the current user is resolved from the password directory by way of the built-in module [`pwd`](https://docs.python.org/3.14/library/pwd.html#module-pwd). A leading `~user` is resolved straight from the password directory.

Under Windows, `USERPROFILE` is consulted when set; otherwise `HOMEPATH` and `HOMEDRIVE` are combined. To deal with a leading `~user`, the final directory component of the current user's home directory is checked against `USERNAME`, and substituted when it matches.

Should the expansion not succeed, or should the path not start with a tilde, the path comes back as it was.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

Changed in version 3.8: No longer uses `HOME` on Windows.

 os.path.expandvars(*path*)

Hand back the argument with its environment variables expanded. Pieces shaped like `$name` or `${name}` get swapped for the value of environment variable *name*. References to variables that do not exist, along with malformed variable names, stay as they are.

Under Windows, `%name%` expansions work too, on top of `$name` and `${name}`.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

 os.path.getatime(*path*, */*)

Hand back the time *path* was last accessed. What comes back is a floating-point number counting the seconds elapsed since the epoch (consult the [`time`](https://docs.python.org/3.14/library/time.html#module-time) module). An [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) is raised when the file is missing or cannot be reached.

 os.path.getmtime(*path*, */*)

Hand back the time *path* was last modified. What comes back is a floating-point number counting the seconds elapsed since the epoch (consult the [`time`](https://docs.python.org/3.14/library/time.html#module-time) module). An [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) is raised when the file is missing or cannot be reached.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

 os.path.getctime(*path*, */*)

Hand back the system's ctime, which on some systems (Unix among them) is the time the metadata last changed, while on others (Windows among them) it is the creation time for *path*. What comes back is a number counting the seconds elapsed since the epoch (consult the [`time`](https://docs.python.org/3.14/library/time.html#module-time) module). An [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) is raised when the file is missing or cannot be reached.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

 os.path.getsize(*path*, */*)

Hand back how large *path* is, measured in bytes. An [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) is raised when the file is missing or cannot be reached.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

 os.path.isabs(*path*, */*)

Yield `True` when *path* is an absolute pathname. Under Unix, that requires it to start with a slash; under Windows, that it start with two (back)slashes, or with a drive letter, a colon, and a (back)slash combined.

See also

`abspath()`

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

Changed in version 3.13: under Windows, a path beginning with precisely one (back)slash now yields `False`.

 os.path.isfile(*path*)

Yield `True` when *path* is an `existing` regular file. Symbolic links are followed, which is why both `islink()` and `isfile()` may hold for one and the same path.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

 os.path.isdir(*path*, */*)

Yield `True` when *path* is an `existing` directory. Symbolic links are followed, which is why both `islink()` and `isdir()` may hold for one and the same path.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

[Subject index](INDEX.md) · [Previous](os-path-abspath-to-os-path-dirname.md) · [Continue](os-path-isjunction-to-os-path-normcase.md) · [Owning module, declaration or section: os.path](os-path-abspath-to-os-path-dirname.md)
