# Python 3.9.0 alpha 1 / core and builtins / codecs

[bpo-37751](https://bugs.python.org/issue?@action=redirect&bpo=37751): Adjusted [`codecs.lookup()`](https://docs.python.org/3.14/library/codecs.html#codecs.lookup) so it normalizes an encoding name identically to [`encodings.normalize_encoding()`](https://docs.python.org/3.14/library/codecs.html#encodings.normalize_encoding), with the difference that [`codecs.lookup()`](https://docs.python.org/3.14/library/codecs.html#codecs.lookup) additionally lowercases the name.

[bpo-38236](https://bugs.python.org/issue?@action=redirect&bpo=38236): When Python cannot import the Python codecs for the filesystem and stdio encodings, it now dumps the path configuration.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
