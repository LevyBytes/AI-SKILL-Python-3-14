# Python 3.5.2 release candidate 1 / library / exceptions and tracebacks

[bpo-26402](https://bugs.python.org/issue?@action=redirect&bpo=26402): Make the XML-RPC client retry when the server closes a persistent connection. That had been a regression connected to the new http.client.RemoteDisconnected exception introduced in 3.5.0a4.

[bpo-12923](https://bugs.python.org/issue?@action=redirect&bpo=12923): Reset the redirect counter of FancyURLopener even when an exception occurs. Brian Brazil and Daniel Rocco supplied the patches this builds on.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
