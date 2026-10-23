# What’s New In Python 3.5 / PEP 471 - os.scandir() function – a better and faster directory iterator - os

### PEP 471 - os.scandir() function – a better and faster directory iterator

[**PEP 471**](https://peps.python.org/pep-0471/) contributes a fresh directory iteration function, [`os.scandir()`](https://docs.python.org/3.14/library/os.html#os.scandir), into the standard library. On top of that, [`os.walk()`](https://docs.python.org/3.14/library/os.html#os.walk) is now built atop `scandir`, which yields a 3 to 5 times speedup on POSIX systems and a 7 to 20 times speedup on Windows systems. The bulk of that gain comes from sharply cutting the count of [`os.stat()`](https://docs.python.org/3.14/library/os.html#os.stat) calls needed while walking a directory tree.

On top of that, `scandir` hands back an iterator rather than producing a list of file names, which makes memory use better when looping over extremely large directories.

The example below demonstrates a basic application of [`os.scandir()`](https://docs.python.org/3.14/library/os.html#os.scandir) to list every file (directories excluded) inside the supplied *path* that does not begin with `'.'`. The [`entry.is_file()`](https://docs.python.org/3.14/library/os.html#os.DirEntry.is_file) call will generally not make an additional system call:

```python
for entry in os.scandir(path):
    if not entry.name.startswith('.') and entry.is_file():
        print(entry.name)

```

See also

[**PEP 471**](https://peps.python.org/pep-0471/) – os.scandir() function – a better and faster directory iterator

PEP authored and built by Ben Hoyt, assisted by Victor Stinner.

[Subject index](INDEX.md) · [Previous source section](pep-484-type-hints.md) · [Next source section](pep-475-retry-system-calls-failing-with-eintr.md) · [Release/subject declaration](summary-release-highlights.md)
