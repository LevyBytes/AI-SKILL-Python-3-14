# Python 3.10.0 alpha 3 / library / asyncio

[bpo-42183](https://bugs.python.org/issue?@action=redirect&bpo=42183): Fix a stack overflow error for asyncio Task or Future repr().

That overflow happens in certain cases where a Task or Future recursively hands back itself.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
