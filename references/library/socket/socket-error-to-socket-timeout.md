# socket — Exceptions

### Exceptions

 *exception *socket.error

A deprecated alias of [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError).

Changed in version 3.3: In line with [**PEP 3151**](https://peps.python.org/pep-3151/), this class became an alias of [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError).

 *exception *socket.herror

A subclass of [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError), this exception gets raised for address-related errors, that is, for functions relying on *h_errno* in the POSIX C API, such as `gethostbyname_ex()` and `gethostbyaddr()`. Its accompanying value is a pair `(h_errno, string)` standing for an error a library call returned. *h_errno* is a numeric value, whereas *string* gives the description of *h_errno* that the `hstrerror()` C function returns.

Changed in version 3.3: This class was made a subclass of [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError).

 *exception *socket.gaierror

A subclass of [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError), this exception gets raised for address-related errors coming from `getaddrinfo()` and `getnameinfo()`. Its accompanying value is a pair `(error, string)` standing for an error a library call returned. *string* gives the description of *error* that the `gai_strerror()` C function returns. The numeric *error* value will line up with one of the `EAI_*` constants this module defines.

Changed in version 3.3: This class was made a subclass of [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError).

 *exception *socket.timeout

A deprecated alias of [`TimeoutError`](https://docs.python.org/3.14/library/exceptions.html#TimeoutError).

A subclass of [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError), this exception gets raised when a timeout fires on a socket that had timeouts switched on by an earlier `settimeout()` call (or implicitly via `setdefaulttimeout()`). The value that comes with it is a string, and at present that string is always "timed out".

Changed in version 3.3: This class was made a subclass of [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError).

Changed in version 3.10: This class was made an alias of [`TimeoutError`](https://docs.python.org/3.14/library/exceptions.html#TimeoutError).

[Subject index](INDEX.md) · [Previous](module-contents.md) · [Continue](socket-af-unix-to-socket-sock-nonblock.md) · [Owning module, declaration or section: socket](socket-low-level-networking-interface.md)
