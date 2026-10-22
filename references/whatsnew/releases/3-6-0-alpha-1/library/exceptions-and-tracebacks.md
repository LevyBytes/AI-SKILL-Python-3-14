# Python 3.6.0 alpha 1 / library / exceptions and tracebacks

[bpo-26402](https://bugs.python.org/issue?@action=redirect&bpo=26402): Corrected the XML-RPC client so it retries after the server tears down a persistent connection. This regression traced back to the new http.client.RemoteDisconnected exception introduced in 3.5.0a4.

[bpo-12923](https://bugs.python.org/issue?@action=redirect&bpo=12923): FancyURLopener's redirect counter is now reset even when an exception occurs. This draws on patches from Brian Brazil and Daniel Rocco.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
