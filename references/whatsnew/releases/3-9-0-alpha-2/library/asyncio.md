# Python 3.9.0 alpha 2 / library / asyncio

[bpo-39006](https://bugs.python.org/issue?@action=redirect&bpo=39006): Repair asyncio for the case where the ssl module is absent: an ssl.SSLSocket instance check happens only when the ssl module can be loaded.

[bpo-38978](https://bugs.python.org/issue?@action=redirect&bpo=38978): Provide `__class_getitem__` across the asyncio objects (Future, Task, Queue). The patch came from Batuhan Taskaya.

[bpo-38529](https://bugs.python.org/issue?@action=redirect&bpo=38529): Discard the overly chatty asyncio warning fired when a stream is deleted without an explicit `.close()` call.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
