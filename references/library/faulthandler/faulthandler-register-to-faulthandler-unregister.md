# faulthandler - Dumping the traceback on a user signal

### Dumping the traceback on a user signal

 faulthandler.register(*signum*, *file=sys.stderr*, *all_threads=True*, *chain=False*)

Sign up a user signal: register a handler for the *signum* signal that dumps the traceback for all threads, or for just the active thread when *all_threads* is `False`, into *file*. The earlier handler is invoked when chain is `True`.

The *file* has to remain open until `unregister()` removes the signal: see issue with file descriptors.

Not available on Windows.

Changed in version 3.5: Support for handing this function a file descriptor was added.

 faulthandler.unregister(*signum*)

Remove a user signal: take out the handler for the *signum* signal that `register()` installed. Yields `True` when the signal had been registered, and `False` if not.

Not available on Windows.

[Subject index](INDEX.md) · [Previous](delayed-traceback-dump-and-cancellation.md) · [Continue](issue-with-file-descriptors.md) · [Owning module, declaration or section: faulthandler](faulthandler-dump-the-python-traceback.md)
