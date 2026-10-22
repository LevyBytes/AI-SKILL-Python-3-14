# Python 3.10.0 alpha 3 / core and builtins / debug

[bpo-42576](https://bugs.python.org/issue?@action=redirect&bpo=42576): `types.GenericAlias` now throws a `TypeError` if you try to initialize it with a keyword argument. Earlier this would crash the interpreter whenever it had been compiled with debug symbols; release builds were unaffected. Ken Jin wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
