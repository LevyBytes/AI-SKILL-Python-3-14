# What’s New in Python 2.4 / New, Improved, and Deprecated Modules — atexit, signal, socket, tarfile, threading, timeit, weakref, xmlrpc.client

The [`signal`](https://docs.python.org/3.14/library/signal.html#module-signal) module now scrutinizes the arguments handed to [`signal.signal()`](https://docs.python.org/3.14/library/signal.html#signal.signal) more strictly. Installing a handler on the `SIGKILL` signal, for one, is off-limits; where older Python builds let this slide in silence, 2.4 throws a [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError) exception.

- The [`socket`](https://docs.python.org/3.14/library/socket.html#module-socket) module took on a pair of new functions. `socketpair()` yields two sockets already connected to each other, while `getservbyport(port)` resolves the service name tied to a particular port number. (Contributed by Dave Cole and Barry Warsaw.)

- Deprecation has come to the `sys.exitfunc()` function. The right tool now is the long-standing [`atexit`](https://docs.python.org/3.14/library/atexit.html#module-atexit) module, which properly manages invoking several exit functions. In time `sys.exitfunc()` is set to become a strictly internal interface that only `atexit` reaches.

- By default the [`tarfile`](https://docs.python.org/3.14/library/tarfile.html#module-tarfile) module now turns out tar archives in the GNU format. (Contributed by Lars Gustäbel.)

- The [`threading`](https://docs.python.org/3.14/library/threading.html#module-threading) module now offers a neat, straightforward route to thread-local data. Inside it sits a `local` class, and each thread sees its own private set of attribute values on instances of that class.

```python
import threading

data = threading.local()
data.number = 42
data.url = ('www.python.org', 80)

```

Each separate thread is free to set and read its own copies of the `number` and `url` attributes. Subclassing `local` lets you seed attributes up front or bolt on methods. (Contributed by Jim Fulton.)

- During its timing loop the [`timeit`](https://docs.python.org/3.14/library/timeit.html#module-timeit) module now switches off periodic garbage collection on its own. The upshot is that back-to-back timings line up more comparably. (Contributed by Raymond Hettinger.)

- A broader range of objects is now accepted by the [`weakref`](https://docs.python.org/3.14/library/weakref.html#module-weakref) module — covering Python functions and class instances, sets together with frozensets, deques, arrays, files plus sockets, and pattern objects from regular expressions. (Contributed by Raymond Hettinger.)

- The [`xmlrpclib`](https://docs.python.org/3.14/library/xmlrpc.client.html#module-xmlrpc.client) module now backs a multi-call extension, letting several XML-RPC calls ride within one HTTP operation. (Contributed by Brian Quinlan.)

- Gone now are the `mpz`, `rotor`, and `xreadlines` modules.

[Subject index](INDEX.md) · [Previous source section](logging-through-regex-module-changes.md) · [Next source section](cookielib.md) · [Release/subject declaration](pep-218-built-in-set-objects.md) · [Release/subject declaration](new-improved-and-deprecated-modules.md) · [Preceding release/subject continuation](logging-basicconfig-keywords.md)
