# Watching file descriptors

### Watching file descriptors

 loop.add_reader(*fd*, *callback*, **args*)

Begin watching the *fd* file descriptor for read readiness and call *callback* with the given arguments as soon as *fd* becomes readable.

Whatever callback was already registered for *fd* gets cancelled and *callback* takes its place.

 loop.remove_reader(*fd*)

Cease watching the *fd* file descriptor for read readiness. Returns `True` when *fd* had been under monitoring for reads.

 loop.add_writer(*fd*, *callback*, **args*)

Begin watching the *fd* file descriptor for write readiness and call *callback* with the given arguments *args* as soon as *fd* becomes writable.

Whatever callback was already registered for *fd* gets cancelled and *callback* takes its place.

Use [`functools.partial()`](https://docs.python.org/3.14/library/functools.html#functools.partial) to pass keyword arguments to *callback*.

 loop.remove_writer(*fd*)

Cease watching the *fd* file descriptor for write readiness. Returns `True` when *fd* had been under monitoring for writes.

Consult as well the [Platform Support](https://docs.python.org/3.14/library/asyncio-platforms.html#asyncio-platform-support) section regarding certain limitations of these methods.

[Subject index](INDEX.md) · [Previous](loop-start-tls.md) · [Continue](loop-sock-recv-to-loop-sock-connect.md)
