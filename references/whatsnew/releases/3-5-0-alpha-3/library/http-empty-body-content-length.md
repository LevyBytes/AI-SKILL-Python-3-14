# Python 3.5.0 alpha 3 / library / body none http client httpconnection request puts content length put post patch headers

[bpo-23539](https://bugs.python.org/issue?@action=redirect&bpo=23539): When body is None, http.client.HTTPConnection.request now puts Content-Length at 0 for PUT, POST, and PATCH headers, dodging the 411 errors that some web servers return.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
