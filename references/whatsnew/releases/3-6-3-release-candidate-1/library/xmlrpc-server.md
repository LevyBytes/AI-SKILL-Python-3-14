# Python 3.6.3 release candidate 1 / library / xmlrpc server

[bpo-31247](https://bugs.python.org/issue?@action=redirect&bpo=31247): xmlrpc.server now deliberately severs reference cycles whenever it relies on sys.exc_info() in the code that handles exceptions.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
