# Python 3.5.2 release candidate 1 / library / repair wsgiref simple server wsgirequesthandler all data reaches client full

[bpo-24291](https://bugs.python.org/issue?@action=redirect&bpo=24291): Repair wsgiref.simple_server.WSGIRequestHandler so that all data reaches the client in full. It had been capable of partial writes that truncated data. Moreover, wsgiref.handler.ServerHandler can now cope with stdout performing partial writes, though that behavior is deprecated.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
