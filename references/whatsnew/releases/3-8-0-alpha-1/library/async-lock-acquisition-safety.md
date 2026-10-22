# Python 3.8.0 alpha 1 / library / resolved asyncio lock correctness flaw permitted very same lock taken

[bpo-32734](https://bugs.python.org/issue?@action=redirect&bpo=32734): Resolved an `asyncio.Lock()` correctness flaw that permitted the very same lock to be taken and held repeatedly before it had been released. Patch by Bar Harel.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
