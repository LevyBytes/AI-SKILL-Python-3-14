# smtplib: `smtplib.SMTP`

# Smtplib

### `smtplib` - SMTP protocol client

**Source code:** [Lib/smtplib.py](https://github.com/python/cpython/tree/3.14/Lib/smtplib.py)

---

The `smtplib` module provides an SMTP client session object suitable for delivering mail to any internet host running an SMTP or ESMTP listener daemon. To understand how SMTP and ESMTP behave, see [**RFC 821**](https://datatracker.ietf.org/doc/html/rfc821.html) (Simple Mail Transfer Protocol) along with [**RFC 1869**](https://datatracker.ietf.org/doc/html/rfc1869.html) (SMTP Service Extensions).

[Availability](https://docs.python.org/3.14/library/intro.html#availability): not WASI.

On WebAssembly this module is either unavailable or non-functional. Refer to [WebAssembly platforms](https://docs.python.org/3.14/library/intro.html#wasm-availability) for further details.

 *class *smtplib.SMTP(*host=''*, *port=0*, *local_hostname=None*, [*timeout*, ]*source_address=None*)

An `SMTP` instance wraps a single SMTP connection. Its methods cover the complete range of SMTP and ESMTP operations. When the optional *host* and *port* parameters are supplied, the SMTP `connect()` method runs with those values as part of initialization. When given, *local_hostname* serves as the FQDN of the local host in the HELO/EHLO command. If it is absent, the local hostname is determined through [`socket.getfqdn()`](https://docs.python.org/3.14/library/socket.html#socket.getfqdn). Should the `connect()` call yield anything other than a success code, an `SMTPConnectError` results. The optional *timeout* parameter sets, in seconds, how long blocking operations such as the connection attempt may take (when left unset, the global default timeout setting applies). Once the timeout elapses, [`TimeoutError`](https://docs.python.org/3.14/library/exceptions.html#TimeoutError) is raised. The optional *source_address* parameter lets you bind to a particular source address on a machine that has several network interfaces, and/or to a particular source TCP port. It accepts a 2-tuple `(host, port)` that the socket binds to as its source address before it connects. When left out (or when *host* or *port* equal `''` and/or `0` respectively) the OS default behavior takes over.

In ordinary usage you should only need the initialization/connect step, plus the `sendmail()` and `SMTP.quit()` methods. See the example provided below.

The `SMTP` class works with the [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement. Used in this fashion, the SMTP `QUIT` command runs automatically once the `with` statement closes. For example:

```python
>>> from smtplib import SMTP
>>> with SMTP("domain.org") as smtp:
...     smtp.noop()
...
(250, b'Ok')
>>>

```

Every command raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `smtplib.SMTP.send` carrying the arguments `self` and `data`, in which `data` holds the bytes that are about to go out to the remote host.

Changed in version 3.3: Support for the [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement was added.

Changed in version 3.3: *source_address* argument was added.

Added in version 3.5: The SMTPUTF8 extension ([**RFC 6531**](https://datatracker.ietf.org/doc/html/rfc6531.html)) is now supported.

Changed in version 3.9: When the *timeout* parameter is given the value zero, a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised so that a non-blocking socket cannot be created.

[Subject index](INDEX.md) · [Continue](smtplib-smtp-ssl-class.md)
