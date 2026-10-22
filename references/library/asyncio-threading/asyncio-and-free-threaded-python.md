# asyncio and free-threaded Python

# Asyncio Threading, Asyncio, Asyncore, Atexit ...

## Overview

Several reference areas appear here. First comes the topic asyncio and free-threaded Python. Then there is asyncio — Asynchronous I/O, followed by asyncore — Asynchronous socket handler. After that, the page turns to atexit — Exit handlers, and finally audioop — Manipulate raw audio data.

## asyncio and free-threaded Python

### asyncio and free-threaded Python

By driving an event loop that acts as a scheduler, asyncio reaches very efficient concurrency: it hops between tasks so that non-blocking I/O operations can proceed. The payoff shows up as stronger performance on I/O-bound workloads. You can additionally push CPU-bound work onto a thread or process pool, though that path stays constrained by CPython's [global interpreter lock](https://docs.python.org/3.14/glossary.html#term-global-interpreter-lock).

In [free-threaded Python](https://docs.python.org/3.14/howto/free-threading-python.html#freethreading-python-howto), by contrast, the GIL is switched off and Python becomes capable of genuine multi-threaded execution. The upshot is that asyncio can finally exploit several CPU cores free of the constraints the GIL once imposed.

From Python 3.14 onward, asyncio treats free-threaded Python as a first-class target, and its implementation is safe to run within a multi-threaded setting.

One event loop pinned to a single core can juggle many connections at the same time, yet the Python that handles each connection still runs one step after another. As soon as each request carries a meaningful chunk of computation, that handling turns into the bottleneck and one core can't keep pace. This is exactly where pairing asyncio with threads pays off: give each thread its own event loop, and the work for separate requests proceeds in parallel over multiple CPU cores. The same pairing helps whenever you must run blocking or CPU-bound code out of an asyncio application.

See also

[Scaling asyncio on Free-Threaded Python](https://labs.quansight.org/blog/scaling-asyncio-on-free-threaded-python) is a blog post from Kumar Aditya walking through the internal modifications that render asyncio both safe and efficient on free-threaded Python, accompanied by benchmarks of the gains they deliver.

[Subject index](INDEX.md) · [Continue](thread-safety-considerations.md)
