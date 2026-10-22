# Python 3.8.0 alpha 1 / library / socketserver

[bpo-33540](https://bugs.python.org/issue?@action=redirect&bpo=33540): A fresh `block_on_close` class attribute is added to the `ForkingMixIn` and `ThreadingMixIn` classes within [`socketserver`](https://docs.python.org/3.14/library/socketserver.html#module-socketserver).

[bpo-35017](https://bugs.python.org/issue?@action=redirect&bpo=35017): [`socketserver.BaseServer.serve_forever()`](https://docs.python.org/3.14/library/socketserver.html#socketserver.BaseServer.serve_forever) now returns right away when its [`shutdown()`](https://docs.python.org/3.14/library/socketserver.html#socketserver.BaseServer.shutdown) method gets called during the time it is polling for new events.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
