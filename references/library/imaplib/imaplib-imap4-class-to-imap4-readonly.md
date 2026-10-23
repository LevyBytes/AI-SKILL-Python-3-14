# imaplib: `imaplib.IMAP4`, `IMAP4.error`, `IMAP4.abort`, `IMAP4.readonly`

# Imaplib

### `imaplib` - IMAP4 protocol client

**Source code:** [Lib/imaplib.py](https://github.com/python/cpython/tree/3.14/Lib/imaplib.py)

---

The module supplies three classes — `IMAP4`, `IMAP4_SSL` and `IMAP4_stream` — that wrap a connection to an IMAP4 server and cover a substantial portion of the IMAP4rev1 client protocol described by [**RFC 2060**](https://datatracker.ietf.org/doc/html/rfc2060.html). Compatibility with older IMAP4 ([**RFC 1730**](https://datatracker.ietf.org/doc/html/rfc1730.html)) servers is retained, though be aware that IMAP4 lacks support for the `STATUS` command.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): not WASI.

On WebAssembly this module is either unavailable or non-functional. Consult [WebAssembly platforms](https://docs.python.org/3.14/library/intro.html#wasm-availability) for further detail.

The `imaplib` module exposes three classes, with `IMAP4` serving as the base:

 *class *imaplib.IMAP4(*host=''*, *port=IMAP4_PORT*, *timeout=None*)

This class carries out the IMAP4 protocol itself. As soon as the instance is initialized, the connection gets opened and the protocol version (IMAP4 or IMAP4rev1) is settled. When *host* is left unspecified, `''` (the local host) applies. Should *port* be omitted, the standard IMAP4 port (143) takes effect. The optional *timeout* parameter gives a timeout in seconds for the connection attempt. When timeout is absent or set to `None`, the global default socket timeout governs.

You can use the `IMAP4` class with the [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement. Used this way, the IMAP4 `LOGOUT` command fires off automatically as the `with` block ends. For instance:

```python
>>> from imaplib import IMAP4
>>> with IMAP4("domain.org") as M:
...     M.noop()
...
('OK', [b'Nothing Accomplished. d25if65hy903weo.87'])

```

Changed in version 3.5: Support for the [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement was added.

Changed in version 3.9: The optional *timeout* parameter was added.

The `IMAP4` class declares three exceptions as attributes:

 *exception *IMAP4.error

Raised whenever an error occurs. Its constructor receives, as a string, the reason behind the exception.

 *exception *IMAP4.abort

Errors from the IMAP4 server trigger this exception. It descends from `IMAP4.error`. Recovery is generally possible by discarding the instance and building a fresh one.

 *exception *IMAP4.readonly

Raised whenever the server alters the status of a mailbox that was writable. It descends from `IMAP4.error`. Write permission has now passed to some other client, so the mailbox must be re-opened to regain that permission.

A subclass for secure connections is also provided:

[Subject index](INDEX.md) · [Continue](imaplib-imap4-ssl-class.md)
