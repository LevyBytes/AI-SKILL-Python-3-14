# Python 3.7.0 alpha 1 / library / collections and iteration

[bpo-28430](https://bugs.python.org/issue?@action=redirect&bpo=28430): Repaired the iterator belonging to the C-implemented asyncio.Future, which would not accept a non-None value handed to it via it.send(val).

[bpo-28963](https://bugs.python.org/issue?@action=redirect&bpo=28963): Out-of-bound iteration in the C implementation of asyncio.Future.remove_done_callback was corrected.

[bpo-30441](https://bugs.python.org/issue?@action=redirect&bpo=30441): Repair a defect that struck when os.environ was modified during iteration over it

[bpo-29532](https://bugs.python.org/issue?@action=redirect&bpo=29532): Modifying a kwarg dictionary handed to functools.partial() no longer changes a partial object once it has been built.

[bpo-29368](https://bugs.python.org/issue?@action=redirect&bpo=29368): While unpickling collections.deque and similar list-like objects, the extend() method is now invoked in place of append(). This can make unpickling up to twice as fast.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
