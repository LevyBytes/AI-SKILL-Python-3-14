# threading: `threading.Semaphore`

### Semaphore objects

This ranks among the oldest synchronization primitives in the history of computer science, devised by the early Dutch computer scientist Edsger W. Dijkstra (who picked the names `P()` and `V()` rather than `acquire()` and `release()`).

A semaphore keeps an internal counter that each `acquire()` call lowers and each `release()` call raises. The counter is never allowed below zero; when `acquire()` sees it at zero, it blocks and waits for some other thread to call `release()`.

Semaphores honor the context management protocol too.

 *class *threading.Semaphore(*value=1*)

This class provides semaphore objects. A semaphore keeps an atomic counter standing for the count of `release()` calls minus the count of `acquire()` calls, plus a starting value. The `acquire()` method blocks when needed until it can return without driving the counter negative. When omitted, *value* defaults to 1.

The optional argument supplies the starting *value* for the internal counter; it defaults to `1`. Should the supplied *value* fall below 0, a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised.

Changed in version 3.3: was previously a factory function, and is now a class.

[Subject index](INDEX.md) · [Previous](threading-condition-acquire-to-threading-condition-notify-all.md) · [Continue](threading-semaphore-acquire-to-threading-semaphore-release.md) · [Owning module, declaration or section: threading](threading-thread-based-parallelism.md)
