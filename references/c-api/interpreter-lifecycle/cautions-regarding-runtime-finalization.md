# Cautions regarding runtime finalization

### Cautions regarding runtime finalization

During the final phase of [interpreter shutdown](https://docs.python.org/3.14/glossary.html#term-interpreter-shutdown), once the runtime has tried to wait on non-daemon threads to finish (which a [`KeyboardInterrupt`](https://docs.python.org/3.14/library/exceptions.html#KeyboardInterrupt) can interrupt) and has executed the [`atexit`](https://docs.python.org/3.14/library/atexit.html#module-atexit) functions, the runtime gets flagged as *finalizing*: `Py_IsFinalizing()` together with [`sys.is_finalizing()`](https://docs.python.org/3.14/library/sys.html#sys.is_finalizing) report true. From here on, the [GIL](https://docs.python.org/3.14/glossary.html#term-GIL) may be acquired by only the *finalization thread* that began finalization (usually the main thread).

Should any thread besides the finalization thread try to attach a [thread state](https://docs.python.org/3.14/glossary.html#term-thread-state) while finalization runs, whether by explicit or implicit means, that thread drops into **a permanently blocked state** and stays there until the process ends. Usually that does no damage, yet deadlock can follow if some subsequent finalization step tries to grab a lock held by the blocked thread, or otherwise waits on it.

Gross? Yes. Doing this avoids the random crashes and/or surprise skipping of C++ finalizations higher in the call stack that happened when such threads got forcibly exited here in CPython 3.13 and earlier. CPython's runtime [thread state](https://docs.python.org/3.14/glossary.html#term-thread-state) C APIs have never set up any error reporting or handling expectations at the point of thread state attachment that could have permitted a clean exit from this scenario. Altering that would demand brand-new stable C APIs plus reworking most of the C code throughout the CPython ecosystem to adopt them with error handling.

[Subject index](INDEX.md) · [Previous source contract](pyunstable-atexit.md) · [Following source contract](py-setprogramname-to-py-getpath.md)
