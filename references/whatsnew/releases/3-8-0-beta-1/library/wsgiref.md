# Python 3.8.0 beta 1 / library / wsgiref

[bpo-29183](https://bugs.python.org/issue?@action=redirect&bpo=29183): Resolves double exceptions inside [`wsgiref.handlers.BaseHandler`](https://docs.python.org/3.14/library/wsgiref.html#wsgiref.handlers.BaseHandler) by triggering its `close()` method solely when nothing was raised.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
