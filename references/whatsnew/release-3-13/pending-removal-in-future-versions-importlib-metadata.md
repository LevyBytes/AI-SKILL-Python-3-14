# What's New In Python 3.13 / Pending removal in future versions — importlib.metadata, logging, mailbox, os, re, shutil, ssl

- [`importlib.metadata`](https://docs.python.org/3.14/library/importlib.metadata.html#module-importlib.metadata):

  - The `EntryPoints` tuple interface.

  - Returning an implicit `None`.

- [`logging`](https://docs.python.org/3.14/library/logging.html#module-logging): the `warn()` method has carried a deprecation since Python 3.3; rely on [`warning()`](https://docs.python.org/3.14/library/logging.html#logging.warning) instead.

- [`mailbox`](https://docs.python.org/3.14/library/mailbox.html#module-mailbox): relying on StringIO input together with text mode carries a deprecation; switch to BytesIO with binary mode.

- [`os`](https://docs.python.org/3.14/library/os.html#module-os): invoking [`os.register_at_fork()`](https://docs.python.org/3.14/library/os.html#os.register_at_fork) within a multi-threaded process.

- `pydoc.ErrorDuringImport`: handing a tuple as the *exc_info* parameter carries a deprecation; pass an exception instance.

- [`re`](https://docs.python.org/3.14/library/re.html#module-re): tighter rules now govern numerical group references plus group names inside regular expressions. A numerical reference may now consist only of a sequence of ASCII digits. Within bytes patterns and replacement strings, a group name is now limited to ASCII letters, digits, and the underscore. (Contributed by Serhiy Storchaka in [gh-91760](https://github.com/python/cpython/issues/91760).)

- The `sre_compile`, `sre_constants` and `sre_parse` modules.

- [`shutil`](https://docs.python.org/3.14/library/shutil.html#module-shutil): the *onerror* parameter of [`rmtree()`](https://docs.python.org/3.14/library/shutil.html#shutil.rmtree) carries a deprecation as of Python 3.12; rely on the *onexc* parameter instead.

- [`ssl`](https://docs.python.org/3.14/library/ssl.html#module-ssl) options and protocols:

  - [`ssl.SSLContext`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext) lacking a protocol argument carries a deprecation.

  - [`ssl.SSLContext`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext): both [`set_npn_protocols()`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext.set_npn_protocols) and `selected_npn_protocol()` carry a deprecation; turn to ALPN instead.

  - `ssl.OP_NO_SSL*` options

  - `ssl.OP_NO_TLS*` options

  - `ssl.PROTOCOL_SSLv3`

  - `ssl.PROTOCOL_TLS`

  - `ssl.PROTOCOL_TLSv1`

  - `ssl.PROTOCOL_TLSv1_1`

  - `ssl.PROTOCOL_TLSv1_2`

  - `ssl.TLSVersion.SSLv3`

[Subject index](INDEX.md) · [Previous source section](undated-api-removals.md) · [Next source section](pending-removal-in-future-versions-ssl-tlsversion-tlsv1.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](undated-api-removals.md)
