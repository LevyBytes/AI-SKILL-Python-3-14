# Python 3.10.0 beta 1 / library / threading

[bpo-43723](https://bugs.python.org/issue?@action=redirect&bpo=43723): The `threading` methods listed below are deprecated now and ought to be swapped out:

  - `currentThread` => [`threading.current_thread()`](https://docs.python.org/3.14/library/threading.html#threading.current_thread)

  - `activeCount` => [`threading.active_count()`](https://docs.python.org/3.14/library/threading.html#threading.active_count)

  - `Condition.notifyAll` => [`threading.Condition.notify_all()`](https://docs.python.org/3.14/library/threading.html#threading.Condition.notify_all)

  - `Event.isSet` => [`threading.Event.is_set()`](https://docs.python.org/3.14/library/threading.html#threading.Event.is_set)

  - `Thread.setName` => [`threading.Thread.name`](https://docs.python.org/3.14/library/threading.html#threading.Thread.name)

  - `thread.getName` => [`threading.Thread.name`](https://docs.python.org/3.14/library/threading.html#threading.Thread.name)

  - `Thread.isDaemon` => [`threading.Thread.daemon`](https://docs.python.org/3.14/library/threading.html#threading.Thread.daemon)

  - `Thread.setDaemon` => [`threading.Thread.daemon`](https://docs.python.org/3.14/library/threading.html#threading.Thread.daemon)

Jelle Zijlstra wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
