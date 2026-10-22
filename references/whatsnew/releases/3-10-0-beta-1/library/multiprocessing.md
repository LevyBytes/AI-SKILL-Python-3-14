# Python 3.10.0 beta 1 / library / multiprocessing

[bpo-43867](https://bugs.python.org/issue?@action=redirect&bpo=43867): The [`multiprocessing`](https://docs.python.org/3.14/library/multiprocessing.html#module-multiprocessing) `Server` class now deliberately traps [`SystemExit`](https://docs.python.org/3.14/library/exceptions.html#SystemExit) and shuts the client connection in that situation. This arises when the `Server.serve_client()` method hits the end of file (EOF).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
