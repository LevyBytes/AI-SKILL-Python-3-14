# Python 3.7.0 alpha 1 / library / socketserver forkingmixin server close holds off until every child process finished preventing

[bpo-31151](https://bugs.python.org/issue?@action=redirect&bpo=31151): socketserver.ForkingMixIn.server_close() now holds off until every child process has finished, preventing zombie processes from leaking.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
