# Python 3.6.6 release candidate 1 / library / fixed defect where invoking write eof selectorsockettransport had already closed

[bpo-31647](https://bugs.python.org/issue?@action=redirect&bpo=31647): Fixed the defect where invoking write_eof() on a _SelectorSocketTransport that had already been closed throws AttributeError.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
