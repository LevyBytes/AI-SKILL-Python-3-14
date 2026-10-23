# What's new in Python 3.14 / Pending removal in future versions - importlib.metadata, logging, mailbox, os, re, shutil, ssl

- [`importlib.metadata`](https://docs.python.org/3.14/library/importlib.metadata.html#module-importlib.metadata):

  - `EntryPoints` tuple interface.

  - Implicit `None` on return values.

- [`logging`](https://docs.python.org/3.14/library/logging.html#module-logging): carrying a deprecation since Python 3.3, the `warn()` method should give way to [`warning()`](https://docs.python.org/3.14/library/logging.html#logging.warning).

- [`mailbox`](https://docs.python.org/3.14/library/mailbox.html#module-mailbox): feeding StringIO input and relying on text mode carries a deprecation; switch to BytesIO together with binary mode.

- [`os`](https://docs.python.org/3.14/library/os.html#module-os): Invoking [`os.register_at_fork()`](https://docs.python.org/3.14/library/os.html#os.register_at_fork) within a multi-threaded process.

- `pydoc.ErrorDuringImport`: supplying a tuple for the *exc_info* parameter carries a deprecation; hand it an exception instance.

- [`re`](https://docs.python.org/3.14/library/re.html#module-re): Tighter rules now govern numerical group references along with group names inside regular expressions. A numerical reference will now only accept a run of ASCII digits. Within bytes patterns and replacement strings, a group name is now confined to ASCII letters, digits, and underscore. (Contributed by Serhiy Storchaka in [gh-91760](https://github.com/python/cpython/issues/91760).)

- `sre_compile`, `sre_constants` and `sre_parse` modules.

- [`shutil`](https://docs.python.org/3.14/library/shutil.html#module-shutil): the *onerror* parameter of [`rmtree()`](https://docs.python.org/3.14/library/shutil.html#shutil.rmtree) carries a deprecation as of Python 3.12; lean on the *onexc* parameter instead.

- [`ssl`](https://docs.python.org/3.14/library/ssl.html#module-ssl) options and protocols:

  - Building an [`ssl.SSLContext`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext) with no protocol argument carries a deprecation.

  - [`ssl.SSLContext`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext): the [`set_npn_protocols()`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext.set_npn_protocols) and `selected_npn_protocol()` members carry a deprecation; switch to ALPN.

  - `ssl.OP_NO_SSL*` options

  - `ssl.OP_NO_TLS*` options

  - `ssl.PROTOCOL_SSLv3`

  - `ssl.PROTOCOL_TLS`

  - `ssl.PROTOCOL_TLSv1`

  - `ssl.PROTOCOL_TLSv1_1`

  - `ssl.PROTOCOL_TLSv1_2`

  - `ssl.TLSVersion.SSLv3`

[Subject index](INDEX.md) · [Previous source section](undated-api-removals.md) · [Next source section](pending-removal-in-future-versions-ssl-tlsversion-tlsv1.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](undated-api-removals.md)
