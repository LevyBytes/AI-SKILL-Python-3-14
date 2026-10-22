# Python 3.8.0 alpha 1 / library / corrected bug where invoking write eof selectorsockettransport already closed raises

[bpo-31647](https://bugs.python.org/issue?@action=redirect&bpo=31647): Corrected a bug where invoking write_eof() on a _SelectorSocketTransport that has already closed raises AttributeError.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
