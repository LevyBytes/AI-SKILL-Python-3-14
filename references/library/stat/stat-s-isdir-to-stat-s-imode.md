# stat: `stat.S_ISDIR()`, `stat.S_ISCHR()`, `stat.S_ISBLK()`, `stat.S_ISREG()`, `stat.S_ISFIFO()`, `stat.S_ISLNK()`, `stat.S_ISSOCK()`, `stat.S_ISDOOR()`, `stat.S_ISPORT()`, `stat.S_ISWHT()`, `stat.S_IMODE()`

# Stat

### `stat` — Interpreting [`stat()`](https://docs.python.org/3.14/library/os.html#os.stat) results

**Source code:** [Lib/stat.py](https://github.com/python/cpython/tree/3.14/Lib/stat.py)

---

Inside `stat` you will find constants plus helpers that let you decode whatever comes back from [`os.stat()`](https://docs.python.org/3.14/library/os.html#os.stat), [`os.fstat()`](https://docs.python.org/3.14/library/os.html#os.fstat) and [`os.lstat()`](https://docs.python.org/3.14/library/os.html#os.lstat), where those are provided. Should you need the full specifics of the `stat()`, `fstat()` and `lstat()` calls, look them up in your platform's own manual.

Changed in version 3.4: A C implementation now backs the stat module.

To probe for a given file type, `stat` offers the routines listed next:

 stat.S_ISDIR(*mode*)

Gives a non-zero result when the mode denotes a directory.

 stat.S_ISCHR(*mode*)

Yields a non-zero result when the mode belongs to a character special device file.

 stat.S_ISBLK(*mode*)

Yields a non-zero result when the mode belongs to a block special device file.

 stat.S_ISREG(*mode*)

Gives a non-zero result when the mode denotes a regular file.

 stat.S_ISFIFO(*mode*)

Gives a non-zero result when the mode denotes a FIFO (named pipe).

 stat.S_ISLNK(*mode*)

Gives a non-zero result when the mode denotes a symbolic link.

 stat.S_ISSOCK(*mode*)

Gives a non-zero result when the mode denotes a socket.

 stat.S_ISDOOR(*mode*)

Gives a non-zero result when the mode denotes a door.

Added in version 3.4.

 stat.S_ISPORT(*mode*)

Gives a non-zero result when the mode denotes an event port.

Added in version 3.4.

 stat.S_ISWHT(*mode*)

Gives a non-zero result when the mode denotes a whiteout.

Added in version 3.4.

A further pair of helpers exists for broader work on a file's mode:

 stat.S_IMODE(*mode*)

Hands back the slice of a file's mode that [`os.chmod()`](https://docs.python.org/3.14/library/os.html#os.chmod) is allowed to change—namely the permission bits together with the sticky bit, set-group-id, and set-user-id bits, wherever a platform offers them.

[Subject index](INDEX.md) · [Continue](stat-s-ifmt-to-stat-st-atime.md)
