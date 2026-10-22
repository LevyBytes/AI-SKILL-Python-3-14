# Language and standard library pending removal in future versions: ssl options and protocols; threading methods

- [`ssl`](https://docs.python.org/3.14/library/ssl.html#module-ssl) options and protocols:

  - [`ssl.SSLContext`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext) lacking a protocol argument is deprecated.

  - [`ssl.SSLContext`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext): the [`set_npn_protocols()`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext.set_npn_protocols) and `selected_npn_protocol()` methods are deprecated; use ALPN in their place.

  - `ssl.OP_NO_SSL*` options

  - `ssl.OP_NO_TLS*` options

  - `ssl.PROTOCOL_SSLv3`

  - `ssl.PROTOCOL_TLS`

  - `ssl.PROTOCOL_TLSv1`

  - `ssl.PROTOCOL_TLSv1_1`

  - `ssl.PROTOCOL_TLSv1_2`

  - `ssl.TLSVersion.SSLv3`

  - `ssl.TLSVersion.TLSv1`

  - `ssl.TLSVersion.TLSv1_1`

- [`threading`](https://docs.python.org/3.14/library/threading.html#module-threading) methods:

  - `threading.Condition.notifyAll()`: use [`notify_all()`](https://docs.python.org/3.14/library/threading.html#threading.Condition.notify_all).

  - `threading.Event.isSet()`: use [`is_set()`](https://docs.python.org/3.14/library/threading.html#threading.Event.is_set).

  - `threading.Thread.isDaemon()`, [`threading.Thread.setDaemon()`](https://docs.python.org/3.14/library/threading.html#threading.Thread.setDaemon): use the [`threading.Thread.daemon`](https://docs.python.org/3.14/library/threading.html#threading.Thread.daemon) attribute.

  - `threading.Thread.getName()`, [`threading.Thread.setName()`](https://docs.python.org/3.14/library/threading.html#threading.Thread.setName): use the [`threading.Thread.name`](https://docs.python.org/3.14/library/threading.html#threading.Thread.name) attribute.

  - `threading.currentThread()`: use [`threading.current_thread()`](https://docs.python.org/3.14/library/threading.html#threading.current_thread).

  - `threading.activeCount()`: use [`threading.active_count()`](https://docs.python.org/3.14/library/threading.html#threading.active_count).

[Subject index](INDEX.md) · [Previous source section](importlib-metadata-through-shutil.md) · [Next source section](typing-text.md)
