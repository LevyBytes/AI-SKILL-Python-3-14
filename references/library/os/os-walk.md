# os: `os.walk()`

os.walk(*top*, *topdown=True*, *onerror=None*, *followlinks=False*)

Generate, by traversing a directory tree top-down or bottom-up, the file names within it. At each directory in the tree whose root is directory *top* (counting *top* itself), it yields a 3-tuple `(dirpath, dirnames, filenames)`.

*dirpath* is a string holding the path to the directory. *dirnames* lists the names of the subdirectories sitting in *dirpath* (symlinks to directories included, `'.'` and `'..'` excluded). *filenames* lists the names of the non-directory files sitting in *dirpath*. Note that the names in the lists carry no path components. To build a full path (which begins with *top*) to a file or directory within *dirpath*, do `os.path.join(dirpath, name)`. Whether the lists come out sorted hinges on the file system. Should a file get removed from or added to the *dirpath* directory while the lists are generated, whether a name for that file appears is unspecified.

When the optional argument *topdown* is `True` or left unspecified, the triple for a directory is produced ahead of the triples for any of its subdirectories (directories are produced top-down). When *topdown* is `False`, the triple for a directory is produced after the triples for all of its subdirectories (directories are produced bottom-up). Regardless of the value of *topdown*, the list of subdirectories is fetched before the tuples for the directory and its subdirectories are produced.

While *topdown* is `True`, the caller can edit the *dirnames* list in-place (perhaps via [`del`](https://docs.python.org/3.14/reference/simple_stmts.html#del) or slice assignment), and `walk()` will only recurse into the subdirectories whose names stay in *dirnames*; this can serve to prune the search, set a particular visiting order, or even tell `walk()` about directories the caller creates or renames before it resumes `walk()` again. Editing *dirnames* while *topdown* is `False` changes nothing about how the walk behaves, since under bottom-up mode the directories listed in *dirnames* get produced ahead of *dirpath* itself.

By default, errors from the `scandir()` call are ignored. When the optional argument *onerror* is given, it should be a function; it gets called with one argument, an [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) instance. It can report the error so the walk keeps going, or raise the exception so the walk stops. Note that the `filename` attribute of the exception object holds the filename.

By default, symbolic links that resolve to directories are not descended into by `walk()`. To visit directories that symlinks point at, on systems where they are supported, set *followlinks* to `True`.

Note

Be aware that setting *followlinks* to `True` can lead to infinite recursion when a link points to a parent directory of itself. `walk()` keeps no record of the directories it has already visited.

Note

When you hand it a relative pathname, leave the current working directory alone across the resumptions of `walk()`. The current directory is never altered by `walk()`, and it assumes its caller leaves it alone too.

For every directory beneath the starting directory, this example reports how many bytes the non-directory files take up, while steering clear of any `__pycache__` subdirectory:

```python
import os
from os.path import join, getsize
for root, dirs, files in os.walk('python/Lib/xml'):
    print(root, "consumes", end=" ")
    print(sum(getsize(join(root, name)) for name in files), end=" ")
    print("bytes in", len(files), "non-directory files")
    if '__pycache__' in dirs:
        dirs.remove('__pycache__')  # don't visit __pycache__ directories

```

In the next example (a bare-bones implementation of [`shutil.rmtree()`](https://docs.python.org/3.14/library/shutil.html#shutil.rmtree)), a bottom-up traversal of the tree is crucial, since `rmdir()` refuses to delete a directory until that directory has been emptied:

```python
# Delete everything reachable from the directory named in "top",
# assuming there are no symbolic links.
# CAUTION:  This is dangerous!  For example, if top == '/', it
# could delete all your disk files.
import os
for root, dirs, files in os.walk(top, topdown=False):
    for name in files:
        os.remove(os.path.join(root, name))
    for name in dirs:
        os.rmdir(os.path.join(root, name))
os.rmdir(top)

```

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `os.walk` with arguments `top`, `topdown`, `onerror`, `followlinks`.

Changed in version 3.5: This function now calls `os.scandir()` rather than `os.listdir()`, making it faster by cutting the number of calls to `os.stat()`.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

[Subject index](INDEX.md) · [Previous](os-utime.md) · [Continue](os-fwalk-to-os-memfd-create.md) · [Owning module, declaration or section: os](os-error-to-os-name.md) · [Owning module, declaration or section: Files and Directories](os-access.md)
