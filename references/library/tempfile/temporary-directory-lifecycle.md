# tempfile / Generate temporary files and directories: `tempfile.TemporaryDirectory`, `cleanup()`

*class *tempfile.TemporaryDirectory(*suffix=None*, *prefix=None*, *dir=None*, *ignore_cleanup_errors=False*, ***, *delete=True*)

Following the same rules as `mkdtemp()`, this class builds a temporary directory securely. You may treat the resulting object as a [context manager](https://docs.python.org/3.14/glossary.html#term-context-manager) (consult Examples). When the context wraps up or the temporary-directory object is destroyed, that freshly made temporary directory and everything inside it are wiped from the filesystem.

 name

You read the directory's name from the `name` attribute of the returned object. Where that object serves as a [context manager](https://docs.python.org/3.14/glossary.html#term-context-manager), the `name` is bound to whatever the `as` clause of the [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement names, should one exist.

 cleanup()

Calling the `cleanup()` method tears the directory down on demand. With *ignore_cleanup_errors* true, any exception that goes unhandled during explicit or implicit cleanup (for example a [`PermissionError`](https://docs.python.org/3.14/library/exceptions.html#PermissionError) while removing open files on Windows) is swallowed, and whatever else can be removed is deleted on a “best-effort” basis. Otherwise such errors propagate in whichever context the cleanup runs — the `cleanup()` call, leaving the context manager, garbage collection of the object, or interpreter shutdown.

The *delete* parameter lets you switch off teardown of the directory tree at context exit. It might look odd for a context manager to suppress the very action it takes on exit, yet this comes in handy while debugging, or whenever you want the cleanup to hinge on some other condition.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `tempfile.mkdtemp` with argument `fullpath`.

Added in version 3.2.

Changed in version 3.10: Added *ignore_cleanup_errors* parameter.

Changed in version 3.12: Added the *delete* parameter.

[Subject index](INDEX.md) · [Previous](spooled-temporary-file-rollover.md) · [Continue](tempfile-mkstemp-to-tempfile-gettempdir.md) · [Owning module, declaration or section: tempfile](tempfile-generate-temporary-files-and-directories.md)
