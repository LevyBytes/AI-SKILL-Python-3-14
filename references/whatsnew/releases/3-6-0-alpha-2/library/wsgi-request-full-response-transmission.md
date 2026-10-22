# Python 3.6.0 alpha 2 / library / repaired wsgiref simple server wsgirequesthandler writes data client full

[bpo-24291](https://bugs.python.org/issue?@action=redirect&bpo=24291): Repaired wsgiref.simple_server.WSGIRequestHandler so it writes data to the client in full. Earlier it might do partial writes and truncate the data. In addition, wsgiref.handler.ServerHandler can now cope with stdout performing partial writes, though that is deprecated.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
