# pathlib: `Path.walk()`

Path.walk(*top_down=True*, *on_error=None*, *follow_symlinks=False*)

Produce the file names within a directory tree by walking that tree either top-down or bottom-up.

For every directory in the directory tree rooted at *self* (taking in *self* yet skipping '.' and '..'), the method yields a 3-tuple of `(dirpath, dirnames, filenames)`.

*dirpath* is a `Path` to the directory being walked at the moment, *dirnames* is a list of strings naming the subdirectories inside *dirpath* (skipping `'.'` and `'..'`), and *filenames* is a list of strings naming the non-directory files inside *dirpath*. To obtain a full path (one that opens with *self*) to a file or directory inside *dirpath*, write `dirpath / name`. Whether those lists come out sorted depends on the file system.

When the optional argument *top_down* is true (its default), the triple for a directory is produced ahead of the triples for any of its subdirectories (directories get walked top-down). When *top_down* is false, the triple for a directory is produced after the triples for all of its subdirectories (directories get walked bottom-up). Regardless of the *top_down* value, the list of subdirectories is fetched before the triples for the directory and its subdirectories get walked.

While *top_down* is true, the caller may alter the *dirnames* list in-place (for instance, with [`del`](https://docs.python.org/3.14/reference/simple_stmts.html#del) or slice assignment), and `Path.walk()` will descend only into those subdirectories whose names stay in *dirnames*. You can use this to prune the search, or to enforce a particular visiting order, or even to tell `Path.walk()` about directories the caller creates or renames before it picks `Path.walk()` back up. Altering *dirnames* while *top_down* is false changes nothing about how `Path.walk()` behaves, since by the time *dirnames* is yielded to the caller the directories within it have already been produced.

By default, errors coming from [`os.scandir()`](https://docs.python.org/3.14/library/os.html#os.scandir) get ignored. When the optional argument *on_error* is supplied, it should be a callable; it gets called with a single argument, an [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) instance. That callable can deal with the error so the walk goes on, or re-raise it so the walk halts. Note that the filename is reachable as the `filename` attribute of the exception object.

By default, `Path.walk()` does not chase symbolic links, and instead drops them into the *filenames* list. Set *follow_symlinks* to true so symlinks get resolved and placed into *dirnames* and *filenames* according to their targets, and so directories reached through symlinks get visited (where the platform supports it).

Note

Be aware that setting *follow_symlinks* to true may lead to endless recursion when a link points at a parent directory of itself. `Path.walk()` keeps no record of the directories it has already visited.

Note

`Path.walk()` presumes the directories it walks stay unmodified while it runs. As an example, when a directory from *dirnames* has been swapped out for a symlink and *follow_symlinks* is false, `Path.walk()` will still attempt to descend into it. To head off that behavior, drop directories from *dirnames* as appropriate.

Note

In contrast to [`os.walk()`](https://docs.python.org/3.14/library/os.html#os.walk), `Path.walk()` lists symlinks to directories within *filenames* when *follow_symlinks* is false.

The example below shows the number of bytes consumed by all files in each directory, while passing over `__pycache__` directories:

```python
from pathlib import Path
for root, dirs, files in Path("cpython/Lib/concurrent").walk(on_error=print):
  print(
      root,
      "consumes",
      sum((root / file).stat().st_size for file in files),
      "bytes in",
      len(files),
      "non-directory files"
  )
  if '__pycache__' in dirs:
        dirs.remove('__pycache__')

```

This further example is a basic implementation of [`shutil.rmtree()`](https://docs.python.org/3.14/library/shutil.html#shutil.rmtree). Walking the tree bottom-up matters here, since `rmdir()` will not let you delete a directory before it is empty:

```python
# Delete everything reachable from the directory "top".
# CAUTION:  This is dangerous! For example, if top == Path('/'),
# it could delete all of your files.
for root, dirs, files in top.walk(top_down=False):
    for name in files:
        (root / name).unlink()
    for name in dirs:
        (root / name).rmdir()

```

Added in version 3.12.

[Subject index](INDEX.md) · [Previous](path-rglob.md) · [Continue](path-touch-to-path-mkdir.md) · [Owning module, declaration or section: pathlib](pathlib-object-oriented-filesystem-paths.md) · [Owning module, declaration or section: Reading directories](path-iterdir-to-path-glob.md)
