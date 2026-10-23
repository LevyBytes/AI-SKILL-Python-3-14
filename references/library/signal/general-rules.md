# signal - General rules

### General rules

With `signal.signal()` you can register your own handlers that run whenever a given signal arrives. By default, a handful of handlers come pre-installed: `SIGPIPE` is silently dropped (which lets failed writes to pipes and sockets surface as normal Python exceptions), and `SIGINT` becomes a [`KeyboardInterrupt`](https://docs.python.org/3.14/library/exceptions.html#KeyboardInterrupt) exception, provided the parent process left it untouched.

Once you assign a handler to some signal, that handler stays in effect until you deliberately clear it (Python mimics the BSD-style interface no matter what the platform actually does underneath); the lone exception is the `SIGCHLD` handler, which defers to the platform's own behavior.

Because signals are emulated on WebAssembly platforms, their behavior diverges there. A number of functions and signals simply aren't offered on those platforms.

[Subject index](INDEX.md) · [Previous](signal-set-handlers-for-asynchronous-events.md) · [Continue](execution-of-python-signal-handlers.md) · [Owning module, declaration or section: signal](signal-set-handlers-for-asynchronous-events.md)
