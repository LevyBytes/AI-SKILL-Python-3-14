# How do I delete a file? (And other file questions?)

### Input and Output

### How do I delete a file? (And other file questions?)

Call `os.remove(filename)` or `os.unlink(filename)`; the [`os`](https://docs.python.org/3.14/library/os.html#module-os) module documents these. The pair behave identically; [`unlink()`](https://docs.python.org/3.14/library/os.html#os.unlink) merely carries the name of the Unix system call backing this function.

Delete a directory with [`os.rmdir()`](https://docs.python.org/3.14/library/os.html#os.rmdir), and create one with [`os.mkdir()`](https://docs.python.org/3.14/library/os.html#os.mkdir). Any missing intermediate directories along `path` get created by `os.makedirs(path)`. As long as they're empty, intermediate directories are removed by `os.removedirs(path)`; to wipe out a whole directory tree along with everything in it, turn to [`shutil.rmtree()`](https://docs.python.org/3.14/library/shutil.html#shutil.rmtree).

Rename a file with `os.rename(old_path, new_path)`.

To truncate a file, open it via `f = open(filename, "rb+")` and call `f.truncate(offset)`; when omitted, offset defaults to the current seek position. There is also `os.ftruncate(fd, offset)` for files opened through [`os.open()`](https://docs.python.org/3.14/library/os.html#os.open), in which *fd* is the file descriptor (a small integer).

A number of file-oriented functions also live in the [`shutil`](https://docs.python.org/3.14/library/shutil.html#module-shutil) module, among them [`copyfile()`](https://docs.python.org/3.14/library/shutil.html#shutil.copyfile), [`copytree()`](https://docs.python.org/3.14/library/shutil.html#shutil.copytree), and [`rmtree()`](https://docs.python.org/3.14/library/shutil.html#shutil.rmtree).

[Subject index](INDEX.md)
