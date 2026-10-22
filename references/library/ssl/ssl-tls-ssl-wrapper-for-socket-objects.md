# ssl — `ssl` — TLS/SSL wrapper for socket objects

### `ssl` — TLS/SSL wrapper for socket objects

**Source code:** [Lib/ssl.py](https://github.com/python/cpython/tree/3.14/Lib/ssl.py)

---

For network sockets — whether you act as the client or the server — this module exposes Transport Layer Security (historically called “Secure Sockets Layer”) so you can encrypt traffic and authenticate the remote peer. The underlying engine is the OpenSSL library.

The component is an [optional module](https://docs.python.org/3.14/glossary.html#term-optional-module). Should your CPython build lack it, consult whatever documentation your distributor offers (in other words, whoever shipped Python to you). Distributors themselves should refer to [Requirements for optional modules](https://docs.python.org/3.14/using/configure.html#optional-module-requirements).

Note

Outcomes can differ across platforms, because these routines invoke the host operating system's socket APIs. Which OpenSSL build is present can shift behavior too. As one example, TLSv1.3 arrives with OpenSSL version 1.1.1.

Warning

Never reach for this module before you have gone through the Security considerations. Skipping that step can give you misplaced confidence, since the ssl module's out-of-the-box defaults won't always suit what your program actually requires.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): not WASI.

On WebAssembly this module is either nonfunctional or simply absent. Consult [WebAssembly platforms](https://docs.python.org/3.14/library/intro.html#wasm-availability) for further detail.

What follows here describes the functions and objects belonging to the `ssl` module; for broader background on certificates, SSL, and TLS, see the materials listed in the “See Also” section further down.

A class named `ssl.SSLSocket` is supplied by this module; it descends from the [`socket.socket`](https://docs.python.org/3.14/library/socket.html#socket.socket) type and acts as a socket-like wrapper that additionally handles SSL encryption and decryption of whatever traverses the socket. Extra methods are available, among them `getpeercert()`, returning the peer's certificate from the far end of the connection, `cipher()`, returning which cipher secures the current connection, and `get_verified_chain()`, `get_unverified_chain()`, which return the certificate chain.

When applications grow more elaborate, the `ssl.SSLContext` class is there to hold configuration and certificates; any SSL socket spun up via the `SSLContext.wrap_socket()` method then inherits those.

Changed in version 3.5.3: Linking against OpenSSL 1.1.0 became supported.

Changed in version 3.6: Support was dropped — and deprecation announced — for OpenSSL 0.9.8, 1.0.0 and 1.0.1. Going forward, the ssl module is to demand OpenSSL 1.0.2 or 1.1.0 as a minimum.

Changed in version 3.10: [**PEP 644**](https://peps.python.org/pep-0644/) landed. OpenSSL 1.1.1 or newer is now mandatory for the ssl module.

Deprecation warnings are emitted whenever deprecated functions or constants are used.

[Subject index](INDEX.md) · [Continue](socket-creation.md)
