# Python 3.9.0 alpha 1 / library / collections abc

[bpo-38008](https://bugs.python.org/issue?@action=redirect&bpo=38008): The parent class check in protocols was fixed so that the module providing a builtin protocol is correctly identified, rather than presuming each one originates from the [`collections.abc`](https://docs.python.org/3.14/library/collections.abc.html#module-collections.abc) module

[bpo-25988](https://bugs.python.org/issue?@action=redirect&bpo=25988): The abstract base classes living in [`collections.abc`](https://docs.python.org/3.14/library/collections.abc.html#module-collections.abc) are no longer surfaced through the ordinary [`collections`](https://docs.python.org/3.14/library/collections.html#module-collections) module.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
