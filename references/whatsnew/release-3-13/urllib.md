# What's New In Python 3.13 / urllib - ssl, urllib.request

### urllib

- Drop the *cafile*, *capath*, and *cadefault* parameters from the [`urllib.request.urlopen()`](https://docs.python.org/3.14/library/urllib.request.html#urllib.request.urlopen) function, which carried a Python 3.6 deprecation. Pass the *context* parameter instead, handing it an [`SSLContext`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext) instance. You can load particular certificates with the [`ssl.SSLContext.load_cert_chain()`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext.load_cert_chain) function, or let [`ssl.create_default_context()`](https://docs.python.org/3.14/library/ssl.html#ssl.create_default_context) choose, from the operating system, its trusted certificate authority (CA) certificates. This change was contributed by Victor Stinner in [gh-105382](https://github.com/python/cpython/issues/105382).

[Subject index](INDEX.md) · [Previous source section](unittest.md) · [Next source section](webbrowser.md) · [Release/subject declaration](summary-release-highlights.md)
