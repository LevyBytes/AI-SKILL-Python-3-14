# Python 3.10.0 alpha 3 / core and builtins / faster comparison between bytes objects non bytes objects whenever option

[bpo-42435](https://bugs.python.org/issue?@action=redirect&bpo=42435): Faster comparison between bytes objects and non-bytes objects whenever the option [`-b`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-b) is given. Also accelerates comparing bytarray objects against a non-buffer object.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
