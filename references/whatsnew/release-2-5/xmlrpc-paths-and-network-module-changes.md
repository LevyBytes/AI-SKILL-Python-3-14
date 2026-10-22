# What's New in Python 2.5 / New, Improved, and Removed Modules — re, socket, struct, sys, tarfile, threading, unicodedata, uuid, xmlrpc.server

The [`SimpleXMLRPCServer`](https://docs.python.org/3.14/library/xmlrpc.server.html#module-xmlrpc.server) and `DocXMLRPCServer` classes have gained an `rpc_paths` attribute that restricts XML-RPC requests to a small list of permitted URL paths; by default only `'/'` and `'/RPC2'` are accepted. Assigning `None` or an empty tuple to `rpc_paths` turns this path validation off.

- On Linux the [`socket`](https://docs.python.org/3.14/library/socket.html#module-socket) module can now work with `AF_NETLINK` sockets, courtesy of a patch contributed by Philippe Biondi. These Linux-only sockets exist to let a user-space process talk to kernel code; you'll find an introductory write-up about them at [https://www.linuxjournal.com/article/7356](https://www.linuxjournal.com/article/7356). Within Python, a netlink address takes the form of a tuple holding 2 integers, `(pid, group_mask)`.

Socket objects also picked up two fresh methods, `recv_into(buffer)` and `recvfrom_into(buffer)`, which place the incoming bytes into an object implementing the buffer protocol rather than handing back the data as a string. As a result you can deposit the data straight into an array or a memory-mapped file.

In addition, socket objects gained `getfamily()`, `gettype()`, and `getproto()` accessor methods that report back the socket's family, type, and protocol values.

- New module: through the `spwd` module you get functions that reach the shadow password database on platforms where shadow passwords are available.

- [`struct`](https://docs.python.org/3.14/library/struct.html#module-struct) now runs faster because it turns format strings into `Struct` objects carrying `pack()` and `unpack()` methods. The approach parallels the way the [`re`](https://docs.python.org/3.14/library/re.html#module-re) module hands you compiled regular expression objects. The module-level `pack()` and `unpack()` functions remain usable; behind the scenes they build `Struct` objects and keep them cached. Alternatively, work with `Struct` instances directly:

```python
s = struct.Struct('ih3s')

data = s.pack(1972, 187, 'abc')
year, number, name = s.unpack(data)

```

Packing and unpacking can also target buffer objects directly by way of the `pack_into(buffer, offset, v1, v2, ...)` and `unpack_from(buffer, offset)` methods. With this you can deposit data straight into an array or a memory-mapped file.

(The `Struct` objects came from Bob Ippolito during the NeedForSpeed sprint. Buffer-object support was contributed by Martin Blais, likewise at the NeedForSpeed sprint.)

- Over the course of 2.5 development, the Python team migrated away from CVS toward Subversion. Details on the precise build version surface through the `sys.subversion` variable, a 3-tuple of `(interpreter-name, branch-name, revision-range)`. As an illustration, while this was being written my own 2.5 copy was reporting `('CPython', 'trunk', '45313:45315')`.

C extensions can reach the same data through the [`Py_GetBuildInfo()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_GetBuildInfo) function, which yields a build-information string along the lines of `"trunk:45355:45356M, Apr 13 2006, 07:42:19"`. (Contributed by Barry Warsaw.)

- A further new function, [`sys._current_frames()`](https://docs.python.org/3.14/library/sys.html#sys._current_frames), hands back the current stack frames for every running thread as a dictionary that maps each thread's identifier to whichever stack frame sits at the top of that thread when the call is made. (Contributed by Tim Peters.)

- Within the [`tarfile`](https://docs.python.org/3.14/library/tarfile.html#module-tarfile) module, the `TarFile` class now offers an `extractall()` method that pulls every member out of the archive and into the current working directory. You can also point extraction at a different directory, as well as unpack just some of the archive's members.

A tarfile opened in stream mode can now have its compression detected automatically through the mode `'r|*'`. (Contributed by Lars Gustäbel.)

- The [`threading`](https://docs.python.org/3.14/library/threading.html#module-threading) module now permits configuring the stack size for newly spawned threads. Calling `stack_size([*size*])` reports the stack size in effect, and passing the optional *size* argument assigns a fresh value. Changing the stack size isn't possible on every platform, but Windows, POSIX threading, and OS/2 each support it. (Contributed by Andrew MacIntyre.)

- The [`unicodedata`](https://docs.python.org/3.14/library/unicodedata.html#module-unicodedata) module was refreshed to draw on version 4.1.0 of the Unicode character database. Because certain specifications still call for version 3.2.0, it remains reachable as [`unicodedata.ucd_3_2_0`](https://docs.python.org/3.14/library/unicodedata.html#unicodedata.ucd_3_2_0).

- New module: the [`uuid`](https://docs.python.org/3.14/library/uuid.html#module-uuid) module produces universally unique identifiers (UUIDs) following [**RFC 4122**](https://datatracker.ietf.org/doc/html/rfc4122.html). That RFC lays out several distinct UUID versions, derived from a seed string, from properties of the system, or entirely at random. The module ships a `UUID` class plus the functions `uuid1()`, `uuid3()`, `uuid4()`, and `uuid5()` for producing the various UUID versions. (Version 2 UUIDs fall outside [**RFC 4122**](https://datatracker.ietf.org/doc/html/rfc4122.html) and this module does not handle them.)

```python
>>> import uuid
>>> # make a UUID based on the host ID and current time
>>> uuid.uuid1()
UUID('a8098c1a-f86e-11da-bd1a-00112444be1e')

>>> # make a UUID using an MD5 hash of a namespace UUID and a name
>>> uuid.uuid3(uuid.NAMESPACE_DNS, 'python.org')
UUID('6fa459ea-ee8a-3ca4-894e-db77e160355e')

>>> # make a random UUID
>>> uuid.uuid4()
UUID('16fd2706-8baf-433b-82eb-8c7fada847da')

>>> # make a UUID using a SHA-1 hash of a namespace UUID and a name
>>> uuid.uuid5(uuid.NAMESPACE_DNS, 'python.org')
UUID('886313e1-3b8a-5372-9b90-0c9aee199e5d')

```

(Contributed by Ka-Ping Yee.)

[Subject index](INDEX.md) · [Next source section](weakref-and-archive-module-changes.md) · [Release/subject declaration](pep-308-conditional-expressions.md) · [Release/subject declaration](standard-library-module-changes.md) · [Preceding release/subject continuation](operator-through-completion-module-changes.md)
