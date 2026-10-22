# Python 3.5.0 alpha 2 / library / codecs

[bpo-23215](https://bugs.python.org/issue?@action=redirect&bpo=23215): When multibyte codecs ran custom error handlers that swallow errors, they burned excessive memory and threw SystemError or MemoryError. Aleksi Torhamo wrote the original patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
