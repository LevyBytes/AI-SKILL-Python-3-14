# threading — Introduction

### Introduction

With the `threading` module you can run several [threads](https://en.wikipedia.org/wiki/Thread_(computing)) (the smaller subdivisions of a process) at the same time inside one process. It supports creating threads and overseeing them, so that work proceeds in parallel while sharing the same memory. Threads shine when the work is I/O bound — think reading or writing files, or issuing network calls — because so much of that time is simply spent idle, awaiting external resources.

One common scenario for `threading` is maintaining a group of worker threads that handle several jobs at the same time. Below is a simple illustration of how `Thread` is used to build and launch threads:

```python
import threading
import time

def crawl(link, delay=3):
    print(f"crawl started for {link}")
    time.sleep(delay)  # Blocking I/O (simulating a network request)
    print(f"crawl ended for {link}")

links = [
    "https://python.org",
    "https://docs.python.org",
    "https://peps.python.org",
]

# Start threads for each link
threads = []
for link in links:
    # Using `args` to pass positional arguments and `kwargs` for keyword arguments
    t = threading.Thread(target=crawl, args=(link,), kwargs={"delay": 2})
    threads.append(t)

# Start each thread
for t in threads:
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()

```

Changed in version 3.7: Previously optional, this module can now always be imported.

See also

[`concurrent.futures.ThreadPoolExecutor`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor) gives you a higher-level way to hand jobs off to a background thread without stalling the caller, and you can still collect their outcomes whenever you need them.

[`queue`](https://docs.python.org/3.14/library/queue.html#module-queue) supplies a thread-safe way for active threads to pass data back and forth.

[`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio) presents a different route to task-level concurrency that does not depend on spinning up several operating-system threads.

Note

Within the Python 2.x line, this module included `camelCase` spellings for certain functions and methods. Although deprecated since Python 3.10, they continue to be available for backward compatibility with Python 2.5 and earlier.

**CPython implementation detail:** Within CPython, the [Global Interpreter Lock](https://docs.python.org/3.14/glossary.html#term-global-interpreter-lock) means that just one thread runs Python code at any given moment (although some libraries built for speed may work around this restriction). To take fuller advantage of the processing power on multi-core hardware, consider reaching for [`multiprocessing`](https://docs.python.org/3.14/library/multiprocessing.html#module-multiprocessing) or [`concurrent.futures.ProcessPoolExecutor`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor) instead. That said, threading remains a fitting choice when you need several I/O-bound tasks running concurrently.

[Subject index](INDEX.md) · [Previous](threading-thread-based-parallelism.md) · [Continue](gil-and-performance-considerations.md) · [Owning module, declaration or section: threading](threading-thread-based-parallelism.md)
