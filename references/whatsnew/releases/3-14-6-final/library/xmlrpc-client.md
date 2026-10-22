# Python 3.14.6 final / library / xmlrpc client

[gh-148954](https://github.com/python/cpython/issues/148954): Repair an XML injection weakness within [`xmlrpc.client.dumps()`](https://docs.python.org/3.14/library/xmlrpc.client.html#xmlrpc.client.dumps) where the `methodname` went unescaped ahead of being interpolated into the XML body.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
