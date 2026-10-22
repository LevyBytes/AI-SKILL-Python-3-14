# dictionaries C API: `PyDict_Update()`, `PyDict_MergeFromSeq2()`, `PyDict_AddWatcher()`, `PyDict_ClearWatcher()`, `PyDict_Watch()`, `PyDict_Unwatch()`

int PyDict_Update([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *a, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *b)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).** Thread safety: [Safe for concurrent use on the same object](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-shared).*

In C this matches `PyDict_Merge(a, b, 1)`, and it parallels `a.update(b)` from Python, save that `PyDict_Update()` will not resort to walking a sequence of key value pairs when the second argument lacks a “keys” attribute. Yield `0` when it succeeds, or `-1` should an exception arise.

Note

Within the [free-threaded build](https://docs.python.org/3.14/glossary.html#term-free-threaded-build), if *b* happens to be a [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict) driven by the standard iterator, the operation holds locks on both *a* and *b* until it finishes. But when *b* is a non-dict mapping, only *a* gets locked, leaving *b* open to concurrent modification by some other thread.

 int PyDict_MergeFromSeq2([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *a, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *seq2, int override)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).** Thread safety: [Safe for concurrent use on the same object](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-shared).*

Bring the key-value pairs from *seq2* into dictionary *a*, updating or merging as needed. The argument *seq2* has to be an iterable whose items are themselves length-2 iterables, each read as a key-value pair. Where keys repeat, the last takes precedence when *override* is true, and otherwise the first does. Yield `0` when it succeeds, or `-1` should an exception arise. The Python equivalent (apart from the return value):

```c
def PyDict_MergeFromSeq2(a, seq2, override):
    for key, value in seq2:
        if override or key not in a:
            a[key] = value

```

Note

For the [free-threaded](https://docs.python.org/3.14/glossary.html#term-free-threading) build, the lock applies to *a* only. Walking *seq2* carries no synchronization, so another thread is free to modify *seq2* in parallel.

 int PyDict_AddWatcher(PyDict_WatchCallback callback)

* Thread safety: [Safe to call from multiple threads with external synchronization only](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-compatible).*

Enroll *callback* to act as a dictionary watcher. The call gives back a non-negative integer id, which you then supply to later `PyDict_Watch()` calls. On error (say there are no watcher IDs left), it returns `-1` and sets an exception.

Note

No internal synchronization guards this function. On the [free-threaded](https://docs.python.org/3.14/glossary.html#term-free-threading) build, it falls to the caller to see that no `PyDict_AddWatcher()` or `PyDict_ClearWatcher()` calls run concurrently.

Added in version 3.12.

 int PyDict_ClearWatcher(int watcher_id)

* Thread safety: [Safe to call from multiple threads with external synchronization only](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-compatible).*

Remove the watcher whose *watcher_id* an earlier `PyDict_AddWatcher()` returned. The call gives back `0` on success and `-1` on error (for instance, when the supplied *watcher_id* was never registered.)

Note

This function provides no synchronization of its own. Under the [free-threaded](https://docs.python.org/3.14/glossary.html#term-free-threading) build, the caller must make certain that neither `PyDict_AddWatcher()` nor `PyDict_ClearWatcher()` is being called concurrently.

Added in version 3.12.

 int PyDict_Watch(int watcher_id, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *dict)

* Thread safety: [Safe to call without external synchronization on distinct objects](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-distinct).*

Flag the dictionary *dict* as being watched. Whenever *dict* is modified or deallocated, the callback that `PyDict_AddWatcher()` assigned *watcher_id* gets invoked. The call yields `0` on success or `-1` on error.

Added in version 3.12.

 int PyDict_Unwatch(int watcher_id, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *dict)

* Thread safety: [Safe to call without external synchronization on distinct objects](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-distinct).*

Flag the dictionary *dict* as watched no longer. From then on, the callback that `PyDict_AddWatcher()` assigned *watcher_id* stops firing when *dict* is modified or deallocated. This watcher must already have been watching the dict. The call yields `0` on success or `-1` on error.

Added in version 3.12.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pydictobject-to-pydict-copy.md) · [Previous source contract](pydict-merge.md) · [Following source contract](pydict-watchevent.md)
