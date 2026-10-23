# What's new in Python 3.14 / http - http.server

### http

- Directory listings together with error pages that the [`http.server`](https://docs.python.org/3.14/library/http.server.html#module-http.server) module emits now let the browser fall back to its own dark mode. (Contributed by Yorik Hansen in [gh-123430](https://github.com/python/cpython/issues/123430).)

- Serving over HTTPS by means of the [`http.server.HTTPSServer`](https://docs.python.org/3.14/library/http.server.html#http.server.HTTPSServer) class is now supported by the [`http.server`](https://docs.python.org/3.14/library/http.server.html#module-http.server) module. The command-line interface (`python -m http.server`) makes this reachable with these options:

  - [`--tls-cert <path>`](https://docs.python.org/3.14/library/http.server.html#cmdoption-http.server-tls-cert): Path to the TLS certificate file.

  - [`--tls-key <path>`](https://docs.python.org/3.14/library/http.server.html#cmdoption-http.server-tls-key): Optional path to the private key file.

  - [`--tls-password-file <path>`](https://docs.python.org/3.14/library/http.server.html#cmdoption-http.server-tls-password-file): Optional path to the password file for the private key.

(Contributed by Semyon Moroz in [gh-85162](https://github.com/python/cpython/issues/85162).)

[Subject index](INDEX.md) · [Previous source section](hmac.md) · [Next source section](imaplib.md) · [Release/subject declaration](summary-release-highlights.md)
