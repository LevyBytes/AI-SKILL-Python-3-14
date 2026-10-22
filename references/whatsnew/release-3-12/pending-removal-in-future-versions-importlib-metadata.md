# What’s New In Python 3.12 / Pending removal in future versions — importlib.metadata, logging, mailbox, os, re, shutil, ssl

- [`importlib.metadata`](https://docs.python.org/3.14/library/importlib.metadata.html#module-importlib.metadata):

  - The `EntryPoints` tuple interface.

  - Implicit `None` on return values.

- [`logging`](https://docs.python.org/3.14/library/logging.html#module-logging): the `warn()` method, deprecated all the way back in Python 3.3, should give way to [`warning()`](https://docs.python.org/3.14/library/logging.html#logging.warning).

- [`mailbox`](https://docs.python.org/3.14/library/mailbox.html#module-mailbox): relying on StringIO input together with text mode is deprecated; switch to BytesIO with binary mode.

- [`os`](https://docs.python.org/3.14/library/os.html#module-os): Invoking [`os.register_at_fork()`](https://docs.python.org/3.14/library/os.html#os.register_at_fork) within a multi-threaded process.

- `pydoc.ErrorDuringImport`: supplying a tuple for the *exc_info* parameter is deprecated; pass an exception instance.

- [`re`](https://docs.python.org/3.14/library/re.html#module-re): Tighter rules now govern numerical group references plus group names within regular expressions. As a numerical reference, only a run of ASCII digits is accepted from now on. Inside bytes patterns and replacement strings, group names are now limited to ASCII letters, digits, and underscore. (Contributed by Serhiy Storchaka in [gh-91760](https://github.com/python/cpython/issues/91760).)

- The `sre_compile`, `sre_constants` and `sre_parse` modules.

- [`shutil`](https://docs.python.org/3.14/library/shutil.html#module-shutil): the *onerror* parameter of [`rmtree()`](https://docs.python.org/3.14/library/shutil.html#shutil.rmtree) became deprecated in Python 3.12; switch to the *onexc* parameter.

- [`ssl`](https://docs.python.org/3.14/library/ssl.html#module-ssl) options and protocols:

  - [`ssl.SSLContext`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext) lacking a protocol argument is deprecated.

  - [`ssl.SSLContext`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext): the [`set_npn_protocols()`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext.set_npn_protocols) and `selected_npn_protocol()` calls are deprecated; adopt ALPN.

  - `ssl.OP_NO_SSL*` options

  - `ssl.OP_NO_TLS*` options

  - `ssl.PROTOCOL_SSLv3`

  - `ssl.PROTOCOL_TLS`

  - `ssl.PROTOCOL_TLSv1`

  - `ssl.PROTOCOL_TLSv1_1`

  - `ssl.PROTOCOL_TLSv1_2`

  - `ssl.TLSVersion.SSLv3`

[Subject index](INDEX.md) · [Previous source section](undated-api-removals.md) · [Next source section](pending-removal-in-future-versions-ssl-tlsversion-tlsv1.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](undated-api-removals.md)
