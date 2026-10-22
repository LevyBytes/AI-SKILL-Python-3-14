# Python 3.5.1 release candidate 1 / library / threads and concurrency

[bpo-25304](https://bugs.python.org/issue?@action=redirect&bpo=25304): Introduced asyncio.run_coroutine_threadsafe(). It allows you to hand a coroutine to a loop from a different thread, giving back a concurrent.futures.Future. Vincent Michel contributed it.

[bpo-24891](https://bugs.python.org/issue?@action=redirect&bpo=24891): Closed a startup race condition that arose when the file descriptor for stdin (0), stdout (1) or stderr (2) was shut while Python was building the sys.stdin, sys.stdout and sys.stderr objects. Should constructing one of these objects fail, the attribute is now set to None rather than an OSError being raised. Marco Paolini provided the first version of the patch.

[bpo-24992](https://bugs.python.org/issue?@action=redirect&bpo=24992): Cleared up error handling plus a garbage-collection-related race condition inside the collections.OrderedDict constructor.

[bpo-25319](https://bugs.python.org/issue?@action=redirect&bpo=25319): On reinitializing a threading.Event, the backing condition ought to rely on an ordinary lock instead of a recursive one.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
