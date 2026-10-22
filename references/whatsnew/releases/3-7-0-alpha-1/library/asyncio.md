# Python 3.7.0 alpha 1 / library / asyncio

[bpo-29703](https://bugs.python.org/issue?@action=redirect&bpo=29703): asyncio was corrected so that new event loops can be created inside child processes.

[bpo-28372](https://bugs.python.org/issue?@action=redirect&bpo=28372): Enabled asyncio to handle the formatting of non-python coroutines.

[bpo-31061](https://bugs.python.org/issue?@action=redirect&bpo=31061): Repaired a crash that occurred while using asyncio together with threads.

[bpo-31185](https://bugs.python.org/issue?@action=redirect&bpo=31185): Repaired assorted errors inside the asyncio speedup module.

[bpo-29870](https://bugs.python.org/issue?@action=redirect&bpo=29870): The asyncio/ssl implementation no longer leaks ssl sockets when a connection is aborted. Michaël Sghaïer contributed the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
