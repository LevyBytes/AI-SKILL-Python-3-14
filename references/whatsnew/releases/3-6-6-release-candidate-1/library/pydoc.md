# Python 3.6.6 release candidate 1 / library / pydoc

[bpo-31238](https://bugs.python.org/issue?@action=redirect&bpo=31238): pydoc: the stop() method belonging to the private ServerThread class now blocks until DocServer.serve_until_quit() returns, then deliberately nulls its docserver attribute to sever a reference cycle.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
