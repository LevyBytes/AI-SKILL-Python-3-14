# ThreadPoolExecutor

### ThreadPoolExecutor

A subclass of `Executor`, `ThreadPoolExecutor` draws on a thread pool to run calls asynchronously.

A deadlock is possible whenever the callable tied to one `Future` blocks awaiting the outcome of a different `Future`. Consider:

```python
import time
def wait_on_b():
    time.sleep(5)
    print(b.result())  # b will never complete because it is waiting on a.
    return 5

def wait_on_a():
    time.sleep(5)
    print(a.result())  # a will never complete because it is waiting on b.
    return 6

executor = ThreadPoolExecutor(max_workers=2)
a = executor.submit(wait_on_b)
b = executor.submit(wait_on_a)

```

And:

```python
def wait_on_future():
    f = executor.submit(pow, 5, 2)
    # This will never complete because there is only one worker thread and
    # it is executing this function.
    print(f.result())

executor = ThreadPoolExecutor(max_workers=1)
future = executor.submit(wait_on_future)
# Note: calling future.result() would also cause a deadlock because
# the single worker thread is already waiting for wait_on_future().

```

 *class *concurrent.futures.ThreadPoolExecutor(*max_workers=None*, *thread_name_prefix=''*, *initializer=None*, *initargs=()*)

A subclass of `Executor` that draws on a pool holding no more than *max_workers* threads to run calls asynchronously.

Before the interpreter is allowed to exit, every thread queued on `ThreadPoolExecutor` gets joined. Be aware that the exit handler responsible for this runs *before* any exit handlers registered through `atexit`. Consequently, to let threads wind down cleanly you must catch and handle exceptions in the main thread so you can signal them. That is why steering long-running tasks toward `ThreadPoolExecutor` is discouraged.

The *initializer* parameter is an optional callable invoked as each worker thread begins; *initargs* is a tuple of arguments handed to that initializer. If *initializer* throws, every job still pending raises a `BrokenThreadPool`, and so does any further attempt to hand work to the pool.

Changed in version 3.5: When *max_workers* is `None` or omitted, the fallback is the count of processors on the machine, scaled by `5` ? the reasoning being that `ThreadPoolExecutor` typically overlaps I/O rather than CPU work, so its worker count ought to exceed that of `ProcessPoolExecutor`.

Changed in version 3.6: Introduced the *thread_name_prefix* parameter, letting users set the [`threading.Thread`](https://docs.python.org/3.14/library/threading.html#threading.Thread) names assigned to the pool's worker threads, which eases debugging.

Changed in version 3.7: Added the *initializer* and *initargs* arguments.

Changed in version 3.8: The default for *max_workers* became `min(32, os.cpu_count() + 4)`. That default keeps no fewer than 5 workers around for I/O bound tasks, caps usage at 32 CPU cores for GIL-releasing CPU bound tasks, and steers clear of quietly consuming very large resources on machines with many cores.

ThreadPoolExecutor now reuses idle worker threads before starting *max_workers* worker threads too.

Changed in version 3.13: Default value of *max_workers* is changed to `min(32, (os.process_cpu_count() or 1) + 4)`.

[Subject index](INDEX.md) · [Previous](executor-submit-map-and-shutdown.md) · [Continue](threadpoolexecutor-example.md)
