# What’s New in Python 2.6 / New and Improved Modules - os, os.path, stat, subprocess

The `attrgetter()` function now takes dotted names and carries out the matching attribute lookups:

```python
>>> inst_name = operator.attrgetter(
...        '__class__.__name__')
>>> inst_name('')
'str'
>>> inst_name(help)
'_Helper'

```

(Contributed by Georg Brandl, after a suggestion by Barry Warsaw.)

- The [`os`](https://docs.python.org/3.14/library/os.html#module-os) module now provides wrappers for a number of new system calls. `fchmod(fd, mode)` and `fchown(fd, uid, gid)` adjust the mode and ownership of an already-open file, while `lchmod(path, mode)` adjusts the mode of a symlink. (Contributed by Georg Brandl and Christian Heimes.)

`chflags()` and `lchflags()` wrap the matching system calls (on platforms where they exist), toggling the flags set on a file. The [`stat`](https://docs.python.org/3.14/library/stat.html#module-stat) module defines constants for the flag values; among the possibilities are `UF_IMMUTABLE` to mark that a file must not be altered and `UF_APPEND` to mark that data may only be appended to the file. (Contributed by M. Levinson.)

`os.closerange(low, high)` quickly shuts every file descriptor running from *low* through *high*, swallowing any errors and leaving out *high* itself. The [`subprocess`](https://docs.python.org/3.14/library/subprocess.html#module-subprocess) module now leans on this function to launch processes more quickly. (Contributed by Georg Brandl; [bpo-1663329](https://bugs.python.org/issue?@action=redirect&bpo=1663329).)

- The `clear()` method on the `os.environ` object will now drop the environment variables by way of [`os.unsetenv()`](https://docs.python.org/3.14/library/os.html#os.unsetenv) on top of wiping the object’s keys. (Contributed by Martin Horcicka; [bpo-1181](https://bugs.python.org/issue?@action=redirect&bpo=1181).)

- The [`os.walk()`](https://docs.python.org/3.14/library/os.html#os.walk) function now takes a `followlinks` parameter. Set it to True and it will trace symlinks that point at directories and descend into those directories’ contents. To stay backward compatible, the parameter defaults to false. Be aware that the function can spiral into infinite recursion when a symlink points back at a parent directory. ([bpo-1273829](https://bugs.python.org/issue?@action=redirect&bpo=1273829))

- Within the [`os.path`](https://docs.python.org/3.14/library/os.path.html#module-os.path) module, the `splitext()` function was altered so that it no longer splits on leading period characters. The outcome is better when working over Unix’s dot-files. For instance, `os.path.splitext('.ipython')` now returns `('.ipython', '')` rather than `('', '.ipython')`. ([bpo-1115886](https://bugs.python.org/issue?@action=redirect&bpo=1115886))

There is a new function, `os.path.relpath(path, start='.')`, which yields a relative path from the `start` path when one is given, or otherwise from the current working directory, over to the target `path`. (Contributed by Richard Barran; [bpo-1339796](https://bugs.python.org/issue?@action=redirect&bpo=1339796).)

On Windows, [`os.path.expandvars()`](https://docs.python.org/3.14/library/os.path.html#os.path.expandvars) will now expand environment variables written in the form “%var%”, and “~user” will expand into that user’s home directory path. (Contributed by Josiah Carlson; [bpo-957650](https://bugs.python.org/issue?@action=redirect&bpo=957650).)

-

[Subject index](INDEX.md) · [Previous source section](itertools-through-operator-module-changes.md) · [Release/subject declaration](python-3-0.md) · [Release/subject declaration](standard-library-module-changes.md) · [Following release/subject continuation](new-and-improved-modules-baseexception.md)
