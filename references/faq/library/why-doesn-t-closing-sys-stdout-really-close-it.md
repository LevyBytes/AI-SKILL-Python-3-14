# Why doesn't closing sys.stdout (stdin, stderr) really close it?

### Why doesn't closing sys.stdout (stdin, stderr) really close it?

In Python, [file objects](https://docs.python.org/3.14/glossary.html#term-file-object) form a high-level layer of abstraction sitting over low-level C file descriptors.

For the bulk of file objects you build in Python through the built-in [`open()`](https://docs.python.org/3.14/library/functions.html#open) function, calling `f.close()` flags the Python file object as closed from Python's standpoint and also sees to closing the underlying C file descriptor. The same thing occurs automatically inside `f`?s destructor when `f` turns into garbage.

Python, however, handles stdin, stdout and stderr in a special way, mirroring the special status C itself grants them. Calling `sys.stdout.close()` flags the Python-level file object as closed, yet does *not* close the C file descriptor tied to it.

Before you close the underlying C file descriptor for any of these three, make certain that's really your intent (for example, you might trip up extension modules attempting I/O). If so, use [`os.close()`](https://docs.python.org/3.14/library/os.html#os.close):

```python
os.close(stdin.fileno())
os.close(stdout.fileno())
os.close(stderr.fileno())

```

Alternatively, you can pass the numeric constants 0, 1 and 2, respectively.

[Subject index](INDEX.md)
