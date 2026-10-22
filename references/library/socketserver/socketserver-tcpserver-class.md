# socketserver: `socketserver.TCPServer`

# Socketserver

### `socketserver` — A framework for network servers

**Source code:** [Lib/socketserver.py](https://github.com/python/cpython/tree/3.14/Lib/socketserver.py)

---

Writing network servers becomes much easier with the `socketserver` module.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): not WASI.

On WebAssembly this module is either absent or non-functional. Consult [WebAssembly platforms](https://docs.python.org/3.14/library/intro.html#wasm-availability) for further details.

The package ships four fundamental concrete server classes:

 *class *socketserver.TCPServer(*server_address*, *RequestHandlerClass*, *bind_and_activate=True*)

Built on the internet TCP protocol, this delivers uninterrupted streams of data flowing between client and server. When *bind_and_activate* is true, the constructor will on its own try to call `server_bind()` and `server_activate()`. Remaining arguments get forwarded to the `BaseServer` base class.

[Subject index](INDEX.md) · [Continue](socketserver-udpserver-class.md)
