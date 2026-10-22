# select: `select.error`, `select.devpoll()`, `select.epoll()`, `select.poll()`, `select.kqueue()`, `select.kevent()`

# Select

### `select` — Waiting for I/O completion

---

Through this module you reach the `select()` and `poll()` functions present on most operating systems, plus `devpoll()` on Solaris and its derivatives, `epoll()` on Linux 2.5+, and `kqueue()` on the majority of BSD systems. Be aware that under Windows the support extends to sockets alone; elsewhere it covers additional file types too (for instance, on Unix it handles pipes). Ordinary files are not supported here for the purpose of checking whether a file has grown since the previous read.

Note

I/O multiplexing at a high level and with good efficiency is offered by the [`selectors`](https://docs.python.org/3.14/library/selectors.html#module-selectors) module, which is layered on top of the `select` module primitives. Reaching for the `selectors` module is the recommended path, unless fine-grained command over the OS-level primitives is what you are after.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): not WASI.

On WebAssembly this module is either unavailable or non-functional. Consult [WebAssembly platforms](https://docs.python.org/3.14/library/intro.html#wasm-availability) for further detail.

What the module defines is as follows:

 *exception *select.error

A deprecated alias of [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError).

Changed in version 3.3: In keeping with [**PEP 3151**](https://peps.python.org/pep-3151/), this class became an alias of [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError).

 select.devpoll()

Hands back a `/dev/poll` polling object; consult the /dev/poll polling objects section further down for the methods that devpoll objects support.

Every `devpoll()` object is tied to the file-descriptor limit in force when it was created. Should your program lower that limit, `devpoll()` will fail; should it raise the limit, `devpoll()` might hand back an incomplete set of active file descriptors.

The new file descriptor is [non-inheritable](https://docs.python.org/3.14/library/os.html#fd-inheritance).

Added in version 3.3.

Changed in version 3.4: Now the freshly created file descriptor cannot be inherited.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Solaris.

 select.epoll(*sizehint=-1*, *flags=0*)

Hands back an edge polling object, usable as an Edge or Level Triggered interface for I/O events.

*sizehint* tells epoll roughly how many events you expect to register. It has to be positive, or `-1` for the default. Its only use is on older systems lacking `epoll_create1()`; in every other case it does nothing (although the value is still validated).

*flags* is deprecated and disregarded entirely. Still, if you do pass it, the value has to be `0` or `select.EPOLL_CLOEXEC`, or else `OSError` is raised.

Look at the Edge and level trigger polling (epoll) objects section further down for the methods that epolling objects support.

The context management protocol is supported by `epoll` objects: inside a [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement, the new file descriptor closes by itself once the block finishes.

The new file descriptor is [non-inheritable](https://docs.python.org/3.14/library/os.html#fd-inheritance).

Changed in version 3.3: Added the *flags* parameter.

Changed in version 3.4: The [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement gained support here, and the freshly created file descriptor can no longer be inherited.

Deprecated since version 3.4: The *flags* parameter. These days `select.EPOLL_CLOEXEC` applies by default; call [`os.set_inheritable()`](https://docs.python.org/3.14/library/os.html#os.set_inheritable) should you need an inheritable file descriptor.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Linux >= 2.5.44.

 select.poll()

Hands back a polling object that lets you register and unregister file descriptors and afterward poll them for I/O events; consult the Polling objects section further down for the methods that polling objects support.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

 select.kqueue()

Hands back a kernel queue object; consult the Kqueue objects section further down for the methods that kqueue objects support.

The new file descriptor is [non-inheritable](https://docs.python.org/3.14/library/os.html#fd-inheritance).

Changed in version 3.4: From now on the newly produced file descriptor is not inheritable.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): BSD, macOS.

 select.kevent(*ident*, *filter=KQ_FILTER_READ*, *flags=KQ_EV_ADD*, *fflags=0*, *data=0*, *udata=0*)

Hands back a kernel event object; consult the Kevent objects section further down for the methods that kevent objects support.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): BSD, macOS.

[Subject index](INDEX.md) · [Continue](select-select-to-select-pipe-buf.md)
