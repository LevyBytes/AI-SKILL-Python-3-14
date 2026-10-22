# Python 3.13.0 alpha 3 / library / functions and types

[bpo-19821](https://bugs.python.org/issue?@action=redirect&bpo=19821): Deprecation now applies to the `pydoc.ispackage()` function.

[bpo-40262](https://bugs.python.org/issue?@action=redirect&bpo=40262): The *buffer* argument of the `ssl.SSLSocket.recv_into()` method no longer needs to implement `__len__`, and buffers whose item size is arbitrary are now supported.

[gh-101336](https://github.com/python/cpython/issues/101336): A `keep_alive` keyword parameter was added for `AbstractEventLoop.create_server()` and `BaseEventLoop.create_server()`.

[bpo-18060](https://bugs.python.org/issue?@action=redirect&bpo=18060): Repaired an inheritance defect capable of triggering segfaults whenever two or more subclass levels descend from a Structure or Union base class.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
