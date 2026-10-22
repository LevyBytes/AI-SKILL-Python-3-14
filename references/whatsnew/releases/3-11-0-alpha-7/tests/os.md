# Python 3.11.0 alpha 7 / tests / os

[bpo-47205](https://bugs.python.org/issue?@action=redirect&bpo=47205): On FreeBSD, the error-case test for [`sched_getaffinity()`](https://docs.python.org/3.14/library/os.html#os.sched_getaffinity) and [`sched_setaffinity()`](https://docs.python.org/3.14/library/os.html#os.sched_setaffinity) is now skipped.

[bpo-47015](https://bugs.python.org/issue?@action=redirect&bpo=47015): One test case covering [`os.sendfile()`](https://docs.python.org/3.14/library/os.html#os.sendfile) is migrated off the deprecated `asyncore` (refer to [**PEP 594**](https://peps.python.org/pep-0594/)) onto [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio). Oleg Iarygin provided the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
