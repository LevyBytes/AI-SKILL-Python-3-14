# Python 3.13.0 alpha 5 / library / multiprocessing

[bpo-43952](https://bugs.python.org/issue?@action=redirect&bpo=43952): Make [`multiprocessing.connection.Listener.accept()`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.connection.Listener.accept) accept empty bytes for the authkey. When empty bytes are rejected as the key, the call hangs forever.

[gh-104090](https://github.com/python/cpython/issues/104090): The multiprocessing resource tracker now leaves with a non-zero status code whenever a resource leak got detected. In every other case it still leaves with status code 0.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
