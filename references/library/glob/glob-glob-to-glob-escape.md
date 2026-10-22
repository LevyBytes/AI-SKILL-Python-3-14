# glob: `glob.glob()`, `glob.iglob()`, `glob.escape()`

### `glob` — Unix style pathname pattern expansion

**Source code:** [Lib/glob.py](https://github.com/python/cpython/tree/3.14/Lib/glob.py)

---

The `glob` module locates pathnames through pattern matching rules resembling those of the Unix shell. Tilde expansion does not happen, yet `*`, `?`, and character ranges written with `[]` are matched correctly. It accomplishes this by combining the [`os.scandir()`](https://docs.python.org/3.14/library/os.html#os.scandir) and [`fnmatch.fnmatch()`](https://docs.python.org/3.14/library/fnmatch.html#fnmatch.fnmatch) functions, rather than by spawning a subshell.

Note

The order in which pathnames come back is unspecified. When a particular order matters to you, sort the results yourself.

Files whose names open with a dot (`.`) are matched solely by patterns that themselves open with a dot, which differs from [`fnmatch.fnmatch()`](https://docs.python.org/3.14/library/fnmatch.html#fnmatch.fnmatch) or [`pathlib.Path.glob()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.glob). To get tilde and shell variable expansion, turn to [`os.path.expanduser()`](https://docs.python.org/3.14/library/os.path.html#os.path.expanduser) and [`os.path.expandvars()`](https://docs.python.org/3.14/library/os.path.html#os.path.expandvars).

To match literally, enclose the meta-characters in brackets. As an example, `'[?]'` matches the character `'?'`.

The functions defined by the `glob` module are:

 glob.glob(*pathname*, ***, *root_dir=None*, *dir_fd=None*, *recursive=False*, *include_hidden=False*)

Hand back a possibly empty list of path names matching *pathname*, which has to be a string holding a path specification. *pathname* may be absolute (such as `/usr/src/Python-1.5/Makefile`) or relative (such as `../../Tools/*/*.gif`), and it may carry shell-style wildcards. As in the shell, broken symlinks appear among the results. Whether the results come back sorted hinges on the file system. Should a file meeting the conditions be deleted or created while this function runs, it is unspecified whether a path name for it ends up in the output.

When *root_dir* is not `None`, it ought to be a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object) naming the root directory to search from. Its effect on `glob()` mirrors switching the current directory ahead of the call. When *pathname* is relative, the result holds paths taken relative to *root_dir*.

By way of the *dir_fd* parameter, this function can handle [paths relative to directory descriptors](https://docs.python.org/3.14/library/os.html#dir-fd).

When *recursive* is true, the “`**`” pattern matches any files plus zero or more directories, subdirectories, and symbolic links pointing at directories. Where the pattern has an [`os.sep`](https://docs.python.org/3.14/library/os.html#os.sep) or [`os.altsep`](https://docs.python.org/3.14/library/os.html#os.altsep) right after it, files will not match.

When *include_hidden* is true, the “`**`” pattern matches hidden directories.

Emits an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `glob.glob` carrying the arguments `pathname`, `recursive`.

Emits an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `glob.glob/2` carrying the arguments `pathname`, `recursive`, `root_dir`, `dir_fd`.

Note

Applying the “`**`” pattern across large directory trees can eat up an excessive amount of time.

Note

This function can hand back duplicate path names whenever *pathname* holds several “`**`” patterns while *recursive* is true.

Note

Every [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) exception thrown while scanning the filesystem is swallowed. That covers [`PermissionError`](https://docs.python.org/3.14/library/exceptions.html#PermissionError) raised on reaching directories you lack read permission for.

Changed in version 3.5: Support for recursive globs using “`**`”.

Changed in version 3.10: Added the *root_dir* and *dir_fd* parameters.

Changed in version 3.11: Added the *include_hidden* parameter.

 glob.iglob(*pathname*, ***, *root_dir=None*, *dir_fd=None*, *recursive=False*, *include_hidden=False*)

Hand back an [iterator](https://docs.python.org/3.14/glossary.html#term-iterator) that produces the same values as `glob()` yet never keeps them all in memory at once.

Emits an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `glob.glob` carrying the arguments `pathname`, `recursive`.

Emits an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `glob.glob/2` carrying the arguments `pathname`, `recursive`, `root_dir`, `dir_fd`.

Note

Duplicate path names may be produced by this function when *pathname* carries more than one “`**`” pattern and *recursive* is true.

Note

Filesystem-scanning [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) exceptions are all suppressed. That includes a [`PermissionError`](https://docs.python.org/3.14/library/exceptions.html#PermissionError) encountered while opening directories without read permission.

Changed in version 3.5: Support for recursive globs using “`**`”.

Changed in version 3.10: Added the *root_dir* and *dir_fd* parameters.

Changed in version 3.11: Added the *include_hidden* parameter.

 glob.escape(*pathname*)

Escape every special character (`'?'`, `'*'` and `'['`). This comes in handy when you wish to match an arbitrary literal string that might contain special characters. Special characters within drive/UNC sharepoints stay unescaped; for instance, on Windows `escape('//?/c:/Quo vadis?.txt')` returns `'//?/c:/Quo vadis[?].txt'`.

Added in version 3.4.

[Subject index](INDEX.md) · [Previous](unix-style-pathname-pattern-expansion.md) · [Continue](glob-translate.md)
