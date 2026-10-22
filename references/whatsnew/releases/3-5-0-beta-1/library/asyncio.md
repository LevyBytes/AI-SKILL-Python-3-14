# Python 3.5.0 beta 1 / library / asyncio

[bpo-23008](https://bugs.python.org/issue?@action=redirect&bpo=23008): Corrected the resolution of attributes whose boolean value is False inside pydoc.

- Resolve asyncio issue 235: the put on LifoQueue and PriorityQueue failed to bump unfinished tasks (the defect crept in when JoinableQueue got folded into Queue).

[bpo-23887](https://bugs.python.org/issue?@action=redirect&bpo=23887): urllib.error.HTTPError now carries a proper repr() representation. Berker Peksag supplied the patch.

- asyncio: New event loop APIs: set_task_factory() and get_task_factory().

- asyncio: async() function is deprecated in favour of ensure_future().

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
