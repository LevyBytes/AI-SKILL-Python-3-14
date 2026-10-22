# Python 3.14.0 alpha 7 / library / http server

[gh-85162](https://github.com/python/cpython/issues/85162): Built-in support for HTTPS servers now lives in the [`http.server`](https://docs.python.org/3.14/library/http.server.html#module-http.server) module, surfaced through [`http.server.HTTPSServer`](https://docs.python.org/3.14/library/http.server.html#http.server.HTTPSServer). The command-line interface (`python -m http.server`) exposes this capability with the `--tls-cert`, `--tls-key` and `--tls-password-file` options. Semyon Moroz wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
