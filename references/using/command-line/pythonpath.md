# PYTHONPATH

PYTHONPATH

Extend the default lookup path for module files. Its format matches the shell's `PATH`: one or more directory pathnames split by [`os.pathsep`](https://docs.python.org/3.14/library/os.html#os.pathsep) (for instance colons on Unix or semicolons on Windows). Directories that don't exist are quietly skipped.

Beyond ordinary directories, individual `PYTHONPATH` entries can point to zipfiles holding pure Python modules (whether source or compiled). Extension modules can't be loaded out of zipfiles.

The default lookup path varies by installation, though it usually starts with `*prefix*/lib/python*version*` (refer to `PYTHONHOME` above). It is *always* tacked onto `PYTHONPATH`.

A further directory gets placed into the lookup path ahead of `PYTHONPATH` as outlined above under Interface options. A Python program can adjust the lookup path through the variable [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path).

[Subject index](INDEX.md) · [Previous source section](pythonhome.md) · [Following source section](pythonsafepath.md)
