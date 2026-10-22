# socket — `socket` — Low-level networking interface

### `socket` — Low-level networking interface

**Source code:** [Lib/socket.py](https://github.com/python/cpython/tree/3.14/Lib/socket.py)

---

Through this module you reach the BSD *socket* interface. You will find it on every contemporary Unix system, on Windows, on MacOS, and most likely on yet other platforms too.

Note

Because the calls go down to the operating system socket APIs, certain behavior can vary from one platform to another.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): not WASI.

On WebAssembly this module is either nonfunctional or absent. Consult [WebAssembly platforms](https://docs.python.org/3.14/library/intro.html#wasm-availability) for further detail.

Python's interface maps the Unix system-call and library interface for sockets directly onto Python's object-oriented idiom: calling `socket()` hands back a *socket object* whose methods carry out the individual socket system calls. The parameter types sit a notch above the C interface: much as with `read()` and `write()` on Python files, the buffer for receive operations is allocated for you, and on send operations the buffer length is taken implicitly.

See also

Module [`socketserver`](https://docs.python.org/3.14/library/socketserver.html#module-socketserver)

Classes that simplify writing network servers.

Module [`ssl`](https://docs.python.org/3.14/library/ssl.html#module-ssl)

A TLS/SSL wrapper for socket objects.

[Subject index](INDEX.md) · [Continue](socket-families-section-introduction-and-initial-examples.md)
