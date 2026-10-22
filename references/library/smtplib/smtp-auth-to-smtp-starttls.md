# smtplib: `SMTP.auth()`, `SMTP.starttls()`

SMTP.auth(*mechanism*, *authobject*, ***, *initial_response_ok=True*)

Issue an `SMTP` `AUTH` command for the named authentication *mechanism*, and process the challenge response through *authobject*.

*mechanism* names the authentication mechanism to be applied as argument to the `AUTH` command; the valid values are those that appear in the `auth` element of `esmtp_features`.

*authobject* has to be a callable object that accepts one optional argument:

```python
data = authobject(challenge=None)

```

When the optional keyword argument *initial_response_ok* is true, `authobject()` is first called with no argument. It can hand back the [**RFC 4954**](https://datatracker.ietf.org/doc/html/rfc4954.html) “initial response” ASCII `str`, which gets encoded and sent with the `AUTH` command as shown below. When `authobject()` cannot supply an initial response (for instance because a challenge is required), it should hand back `None` when called with `challenge=None`. When *initial_response_ok* is false, `authobject()` is not called first with `None`.

When the initial response check yields `None`, or when *initial_response_ok* is false, `authobject()` is called to handle the server’s challenge response; the *challenge* argument it receives will be a `bytes`. It should hand back ASCII `str` *data* that gets base64 encoded and sent to the server.

The `SMTP` class supplies `authobjects` for the `CRAM-MD5`, `PLAIN`, and `LOGIN` mechanisms; their names are `SMTP.auth_cram_md5`, `SMTP.auth_plain`, and `SMTP.auth_login` respectively. Each one requires that the `user` and `password` properties of the `SMTP` instance hold suitable values.

User code does not usually need to call `auth` on its own, and can instead call the `login()` method, which attempts each of the mechanisms above one after another, in the order shown. `auth` is made available to help implement authentication methods that `smtplib` does not (or does not yet) support directly.

Added in version 3.5.

 SMTP.starttls(***, *context=None*)

Switch the SMTP connection into TLS (Transport Layer Security) mode. Every SMTP command after that point will be encrypted. You should then invoke `ehlo()` once more.

When *keyfile* and *certfile* are supplied, they serve to build an [`ssl.SSLContext`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext).

The optional *context* parameter is an [`ssl.SSLContext`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext) object; this offers an alternative to supplying a keyfile and a certfile, and when it is named both *keyfile* and *certfile* should be `None`.

When no `EHLO` or `HELO` command has yet been sent during this session, the method attempts ESMTP `EHLO` first.

Changed in version 3.12: The *keyfile* and *certfile* parameters, long deprecated, are now gone.

`SMTPHeloError`

The server failed to respond correctly to the `HELO` greeting.

`SMTPNotSupportedError`

The server does not support the STARTTLS extension.

[`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError)

SSL/TLS support is unavailable in your Python interpreter.

Changed in version 3.3: *context* was added.

Changed in version 3.4: Hostname checking via [`ssl.SSLContext.check_hostname`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext.check_hostname) together with *Server Name Indicator* (see [`HAS_SNI`](https://docs.python.org/3.14/library/ssl.html#ssl.HAS_SNI)) is now handled by the method.

Changed in version 3.5: The error raised when STARTTLS is unsupported is now the `SMTPNotSupportedError` subclass rather than the base `SMTPException`.

[Subject index](INDEX.md) · [Previous](smtp-set-debuglevel-to-smtp-login.md) · [Continue](smtp-sendmail-to-smtp-esmtp-features.md) · [Owning module, declaration or section: smtplib](smtplib-smtp-class.md) · [Owning module, declaration or section: SMTP Objects](smtp-set-debuglevel-to-smtp-login.md)
