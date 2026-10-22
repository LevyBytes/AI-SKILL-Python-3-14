# stat: `stat.S_IFMT()`, `stat.filemode()`, `stat.ST_MODE`, `stat.ST_INO`, `stat.ST_DEV`, `stat.ST_NLINK`, `stat.ST_UID`, `stat.ST_GID`, `stat.ST_SIZE`, `stat.ST_ATIME`

stat.S_IFMT(*mode*)

Hands back the slice of a file's mode that encodes its type — the same slice the `S_IS*()` helpers above rely on.

In ordinary use the `os.path.is*()` helpers are what you reach for when checking a file's type; the routines here earn their keep when you run several checks against one file and want to skip the cost of a fresh `stat()` system call on every check. They also help when you need details that [`os.path`](https://docs.python.org/3.14/library/os.path.html#module-os.path) does not cover, such as detecting block and character devices.

Example:

```python
import os, sys
from stat import *

def walktree(top, callback):
    '''recursively descend the directory tree rooted at top,
       calling the callback function for each regular file'''

    for f in os.listdir(top):
        pathname = os.path.join(top, f)
        mode = os.lstat(pathname).st_mode
        if S_ISDIR(mode):
            # It's a directory, recurse into it
            walktree(pathname, callback)
        elif S_ISREG(mode):
            # It's a file, call the callback function
            callback(pathname)
        else:
            # Unknown file type, print a message
            print('Skipping %s' % pathname)

def visitfile(file):
    print('visiting', file)

if __name__ == '__main__':
    walktree(sys.argv[1], visitfile)

```

One more helper exists that turns a file's mode into text a person can read:

 stat.filemode(*mode*)

Convert a file’s mode to a string of the form ‘-rwxrwxrwx’.

Added in version 3.3.

Changed in version 3.4: The function supports `S_IFDOOR`, `S_IFPORT` and `S_IFWHT`.

Each variable that follows is merely a named position within the 10-tuple handed back by [`os.stat()`](https://docs.python.org/3.14/library/os.html#os.stat), [`os.fstat()`](https://docs.python.org/3.14/library/os.html#os.fstat) or [`os.lstat()`](https://docs.python.org/3.14/library/os.html#os.lstat).

 stat.ST_MODE

Inode protection mode.

 stat.ST_INO

Inode number.

 stat.ST_DEV

Device inode resides on.

 stat.ST_NLINK

Number of links to the inode.

 stat.ST_UID

User id of the owner.

 stat.ST_GID

Group id of the owner.

 stat.ST_SIZE

For an ordinary file, its byte count; for certain special files, how much data is queued.

 stat.ST_ATIME

Time of last access.

[Subject index](INDEX.md) · [Previous](stat-s-isdir-to-stat-s-imode.md) · [Continue](stat-st-mtime-to-stat-s-irwxu.md) · [Owning module, declaration or section: stat](stat-s-isdir-to-stat-s-imode.md)
