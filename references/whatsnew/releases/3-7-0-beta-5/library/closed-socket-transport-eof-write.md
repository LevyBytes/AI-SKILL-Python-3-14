# Python 3.7.0 beta 5 / library / repaired bug where invoking write eof selectorsockettransport s already closed

[bpo-31647](https://bugs.python.org/issue?@action=redirect&bpo=31647): Repaired a bug where invoking write_eof() on a _SelectorSocketTransport that's already closed raises AttributeError.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
