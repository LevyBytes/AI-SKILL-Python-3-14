# tempfile: `tempfile.TemporaryFile()`

tempfile.TemporaryFile(*mode='w+b'*, *buffering=-1*, *encoding=None*, *newline=None*, *suffix=None*, *prefix=None*, *dir=None*, ***, *errors=None*)

Hand back a [file-like object](https://docs.python.org/3.14/glossary.html#term-file-like-object) suitable as scratch storage. Creation follows the same secure rules as `mkstemp()`. The moment it closes — counting the implicit close at garbage-collection time — it is gone. On Unix the file's directory entry is either never made or is unlinked right after creation. Elsewhere that is not available, so your code must not assume one way or the other whether such a temporary file shows up by name in the file system.

You may treat the resulting object as a [context manager](https://docs.python.org/3.14/glossary.html#term-context-manager) (consult Examples). Once the context ends or the file object is destroyed, the temporary file leaves the filesystem.

By default the *mode* parameter is `'w+b'`, which lets the new file be both read and written without first closing it. Choosing binary mode keeps behavior uniform across platforms no matter what data is held. The *buffering*, *encoding*, *errors* and *newline* arguments mean the same as they do for [`open()`](https://docs.python.org/3.14/library/functions.html#open).

For the *dir*, *prefix* and *suffix* parameters, both the meaning and the defaults match those of `mkstemp()`.

On POSIX platforms what comes back is an actual file object. On the rest it is a file-like object whose `file` attribute holds the real file object underneath.

When it is present and functional, the [`os.O_TMPFILE`](https://docs.python.org/3.14/library/os.html#os.O_TMPFILE) flag is employed (a Linux-only feature needing Linux kernel 3.11 or newer).

Where a platform is neither Posix nor Cygwin, TemporaryFile simply aliases NamedTemporaryFile.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `tempfile.mkstemp` with argument `fullpath`.

Changed in version 3.5: The [`os.O_TMPFILE`](https://docs.python.org/3.14/library/os.html#os.O_TMPFILE) flag is now used when available.

Changed in version 3.8: Added *errors* parameter.

```
 tempfile.NamedTemporaryFile(*mode='w+b'*, *buffering=-1*, *encoding=None*, *newline=None*, *suffix=None*, *prefix=None*, *dir=None*, *delete=True*, ***, *errors=None*, *delete_on_close=True*)
```

This function behaves just like `TemporaryFile()`, save for these distinctions:

- The file it returns is guaranteed to carry a name that is visible in the file system.

- So the named file can be managed, it widens the `TemporaryFile()` parameter set with *delete* and *delete_on_close*, which decide whether and in what way the named file gets removed automatically.

What you receive is always a [file-like object](https://docs.python.org/3.14/glossary.html#term-file-like-object) whose `file` attribute is the real file object beneath. Such a file-like object slots into a [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement exactly as an ordinary file would. You can read the temporary file's name off the `name` attribute of the returned file-like object. On Unix — in contrast to `TemporaryFile()` — the directory entry is not unlinked right after the file is made.

When *delete* is true (its default) together with *delete_on_close* true (also default), closing the file removes it at once. When *delete* is true but *delete_on_close* is false, removal happens solely on context-manager exit, or otherwise when the [file-like object](https://docs.python.org/3.14/glossary.html#term-file-like-object) is finalized — and here removal is not always certain (see [`object.__del__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__del__)). When *delete* is false, whatever *delete_on_close* holds is disregarded.

So, if you want to reopen the temporary file by name after closing it, either keep it from being deleted at close (set *delete* false), or — should the temporary file live inside a [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement — set *delete_on_close* false. That second route is preferred, since it still helps tidy the temporary file away once the context manager exits.

Reopening the temporary file by its name while it remains open behaves as follows:

- On POSIX you can always reopen the file.

- On Windows, see to it that at least one of these holds true:

  - *delete* is false

  - a further open shares delete access (for instance by calling [`os.open()`](https://docs.python.org/3.14/library/os.html#os.open) with the flag `O_TEMPORARY`)

  - *delete* is true while *delete_on_close* is false. Mind that, in this situation, any further opens that do not share delete access (say, made through the builtin [`open()`](https://docs.python.org/3.14/library/functions.html#open)) have to be shut before leaving the context manager; otherwise the [`os.unlink()`](https://docs.python.org/3.14/library/os.html#os.unlink) at context-manager exit fails with a [`PermissionError`](https://docs.python.org/3.14/library/exceptions.html#PermissionError).

On Windows, when *delete_on_close* is false and the file lands in a directory where the user has no delete access, the [`os.unlink()`](https://docs.python.org/3.14/library/os.html#os.unlink) at the close of the context manager fails with a [`PermissionError`](https://docs.python.org/3.14/library/exceptions.html#PermissionError). With *delete_on_close* true this cannot arise, because delete access is asked for at open time, and the open fails straight away if that access is denied.

On POSIX alone, a process struck down abruptly by SIGKILL is unable to auto-delete any NamedTemporaryFiles it had created.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `tempfile.mkstemp` with argument `fullpath`.

Changed in version 3.8: Added *errors* parameter.

Changed in version 3.12: Added *delete_on_close* parameter.

[Subject index](INDEX.md) · [Previous](tempfile-generate-temporary-files-and-directories.md) · [Continue](spooled-temporary-file-rollover.md) · [Owning module, declaration or section: tempfile](tempfile-generate-temporary-files-and-directories.md)
