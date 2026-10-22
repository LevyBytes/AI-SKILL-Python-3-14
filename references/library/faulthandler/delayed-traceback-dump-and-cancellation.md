# faulthandler — Dumping the tracebacks after a timeout

### Dumping the tracebacks after a timeout

 faulthandler.dump_traceback_later(*timeout*, *repeat=False*, *file=sys.stderr*, *exit=False*)

Emit the tracebacks for every thread once *timeout* seconds have elapsed, or recurring every *timeout* seconds when *repeat* is `True`. When *exit* is `True`, `_exit()` is invoked with status=1 after the tracebacks are emitted. (Be aware that `_exit()` terminates the process at once, so it skips cleanup such as flushing file buffers.) Calling the function a second time supersedes the earlier parameters and restarts the timeout. Timer resolution is finer than one second.

The *file* has to remain open until either the traceback gets dumped or `cancel_dump_traceback_later()` is invoked: see issue with file descriptors.

A watchdog thread backs this function's implementation.

Changed in version 3.5: Passing a file descriptor here became supported.

Changed in version 3.7: From now on this function is available unconditionally.

 faulthandler.cancel_dump_traceback_later()

Cancel the last call to `dump_traceback_later()`.

[Subject index](INDEX.md) · [Previous](faulthandler-enable-to-faulthandler-is-enabled.md) · [Continue](faulthandler-register-to-faulthandler-unregister.md) · [Owning module, declaration or section: faulthandler](faulthandler-dump-the-python-traceback.md)
