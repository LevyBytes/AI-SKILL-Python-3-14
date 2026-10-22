# Python 3.10.0 alpha 1 / library / functions and types

[bpo-41900](https://bugs.python.org/issue?@action=redirect&bpo=41900): Within xml.etree.ElementTree, C14N 2.0 serialisation broke on unprefixed attributes whenever a default namespace had been declared.

[bpo-39587](https://bugs.python.org/issue?@action=redirect&bpo=39587): apply the right mix-in data type while building Enums

[bpo-41789](https://bugs.python.org/issue?@action=redirect&bpo=41789): Respect `object` overrides during `Enum` class creation (namely `__str__`, `__repr__`, `__format__`, and `__reduce_ex__`).

[bpo-40782](https://bugs.python.org/issue?@action=redirect&bpo=40782): Adjust the asyncio.AbstractEventLoop.run_in_executor method so that it is not a coroutine.

[bpo-40791](https://bugs.python.org/issue?@action=redirect&bpo=40791): Whenever OpenSSL is present, `hashlib.compare_digest()` makes use of OpenSSL’s `CRYPTO_memcmp()` function.

[bpo-40756](https://bugs.python.org/issue?@action=redirect&bpo=40756): For `LoggerAdapter.__init__`, the second argument (extra) now defaults to None.

[bpo-39791](https://bugs.python.org/issue?@action=redirect&bpo=39791): The built-in loaders (SourceFileLoader and ZipImporter) now ship `TraversableResources` implementations for `ResourceReader`, and the previous fallback function is gone.

[bpo-40084](https://bugs.python.org/issue?@action=redirect&bpo=40084): Repair `Enum.__dir__`: dir(Enum.member) now lists attributes in addition to methods.

[bpo-41317](https://bugs.python.org/issue?@action=redirect&bpo=41317): Within asyncio.loop.sock_accept(), call add_done_callback() so the reader is unsubscribed promptly on cancellation.

[bpo-41273](https://bugs.python.org/issue?@action=redirect&bpo=41273): Make any transport built on `_ProactorReadPipeTransport` faster by invoking `recv_into` in place of `recv`, which avoids allocating a fresh buffer on each `recv` call inside the transport's read loop.

[bpo-41195](https://bugs.python.org/issue?@action=redirect&bpo=41195): Provide a read-only ssl.SSLContext.security_level attribute for reading the context's security level.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
