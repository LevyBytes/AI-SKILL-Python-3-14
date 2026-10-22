# Python 3.7.0 alpha 1 / library / threads and concurrency

[bpo-31233](https://bugs.python.org/issue?@action=redirect&bpo=31233): socketserver.ThreadingMixIn now tracks a list of non-daemonic threads so that server_close() can wait for every one of those threads to finish.

[bpo-29293](https://bugs.python.org/issue?@action=redirect&bpo=29293): Supply the missing "n" parameter on multiprocessing.Condition.notify(). The docs say multiprocessing.Condition acts like threading.Condition, yet its notify() method was missing the optional "n" argument (which names how many sleepers to wake) that threading.Condition.notify() accepts.

[bpo-28387](https://bugs.python.org/issue?@action=redirect&bpo=28387): Removed a possible crash in the _io.TextIOWrapper deallocator that struck when the garbage collector ran on another thread. This rests on a patch from Sebastian Cufre.

[bpo-29376](https://bugs.python.org/issue?@action=redirect&bpo=29376): An assertion error within threading._DummyThread.is_alive() was corrected.

[bpo-28969](https://bugs.python.org/issue?@action=redirect&bpo=28969): Resolved a race condition inside the C version of functools.lru_cache. A KeyError was able to surface whenever a cached function whose cache was full got invoked at the same time from separate threads using identical uncached arguments.

[bpo-28427](https://bugs.python.org/issue?@action=redirect&bpo=28427): Stale keys should no longer wipe out fresh values from a WeakValueDictionary during collection triggered by a separate thread.

[bpo-19542](https://bugs.python.org/issue?@action=redirect&bpo=19542): Corrected defects in WeakValueDictionary.setdefault() plus WeakValueDictionary.pop() that appeared whenever a GC collection fired from a separate thread.

[bpo-30886](https://bugs.python.org/issue?@action=redirect&bpo=30886): Repair multiprocessing.Queue.join_thread(): it now waits for the thread to finish even when that thread was launched by the same process that created the queue.

[bpo-18966](https://bugs.python.org/issue?@action=redirect&bpo=18966): The non-daemonic threads that a multiprocessing.Process spawns are now joined when the child exits.

[bpo-30414](https://bugs.python.org/issue?@action=redirect&bpo=30414): The multiprocessing.Queue._feed thread running in the background will no longer leave the main loop when an exception occurs.

[bpo-29212](https://bugs.python.org/issue?@action=redirect&bpo=29212): When no thread_name_prefix is given, concurrent.futures.thread.ThreadPoolExecutor worker threads default to a name that is no longer derived from repr(). Each one now reports itself as “ThreadPoolExecutor-y_n”.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
