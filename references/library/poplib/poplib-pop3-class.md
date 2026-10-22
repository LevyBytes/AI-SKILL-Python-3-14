# poplib: `poplib.POP3`

### `poplib` — POP3 protocol client

**Source code:** [Lib/poplib.py](https://github.com/python/cpython/tree/3.14/Lib/poplib.py)

---

Here a single class, `POP3`, is declared; it wraps a link to a POP3 server and carries out the protocol described by [**RFC 1939**](https://datatracker.ietf.org/doc/html/rfc1939.html). Both the required and the optional command groups of [**RFC 1939**](https://datatracker.ietf.org/doc/html/rfc1939.html) are handled by the `POP3` class. On top of that, the `POP3` class understands the `STLS` command from [**RFC 2595**](https://datatracker.ietf.org/doc/html/rfc2595.html), letting you turn on encrypted traffic over a link that is already open.

The module also ships a second class, `POP3_SSL`, meant for reaching POP3 servers that run SSL as the transport beneath them.

Keep in mind that POP3, despite its broad reach, is on its way out. Server quality differs enormously, and a fair number are downright bad. Should your mail host offer IMAP, the [`imaplib.IMAP4`](https://docs.python.org/3.14/library/imaplib.html#imaplib.IMAP4) class is the wiser choice, since IMAP servers are usually built to a higher standard.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): not WASI.

On WebAssembly this module is either non-functional or absent. Consult [WebAssembly platforms](https://docs.python.org/3.14/library/intro.html#wasm-availability) if you want the details.

Two classes are exposed by the `poplib` module:

`class poplib.POP3(*host*, *port=POP3_PORT*[, *timeout*])`

The genuine POP3 protocol lives in this class. Building the instance is what opens the link. Leave *port* off and the usual POP3 port (110) applies. The discretionary *timeout* argument gives, in seconds, how long the connection attempt may take; drop it and the process-wide default timeout governs instead.

Fires an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `poplib.connect` carrying the arguments `self`, `host`, `port`.

Each command emits an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `poplib.putline` carrying `self` and `line`, in which `line` holds the bytes that are about to travel to the remote host.

Changed in version 3.9: Passing zero for the *timeout* argument now triggers a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError), so that a non-blocking socket is never made.

[Subject index](INDEX.md) · [Previous](pop3-protocol-client.md) · [Continue](poplib-pop3-ssl-class.md)
