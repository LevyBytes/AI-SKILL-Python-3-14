# Python 3.8.0 alpha 2 / library / importlib

[bpo-34572](https://bugs.python.org/issue?@action=redirect&bpo=34572): Correct the C implementation of pickle.loads so it uses importlib's locking mechanisms and thus steers clear of partially loaded modules. Patch by Tim Burgess.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
