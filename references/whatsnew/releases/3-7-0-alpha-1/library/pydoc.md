# Python 3.7.0 alpha 1 / library / pydoc

[bpo-31238](https://bugs.python.org/issue?@action=redirect&bpo=31238): pydoc: the private ServerThread class's stop() method now holds off until DocServer.serve_until_quit() has finished, after which it explicitly sets its docserver attribute to None so a reference cycle is broken.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
