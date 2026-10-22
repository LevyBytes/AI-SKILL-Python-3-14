# Python 3.14.1 final / library / threading

[gh-137017](https://github.com/python/cpython/issues/137017): Adjust [`threading.Thread.is_alive`](https://docs.python.org/3.14/library/threading.html#threading.Thread.is_alive) so it keeps reporting `True` right up until the backing OS thread has finished its teardown. The change removes spurious false negatives in corner cases tied to thread monitoring, or to `threading.Thread.is_alive` being queried too early.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
