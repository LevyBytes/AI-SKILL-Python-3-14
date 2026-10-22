# Using asyncio with threads

### Using asyncio with threads

Running a single event loop per thread is something asyncio permits, and it lets you tap several CPU cores under free-threaded Python. Each thread keeps its own event loop, and tasks land on those loops independently of one another.

The following snippet shows asyncio working together with threads:

```python
import asyncio
import threading

async def worker(name: str) -> None:
    print(f"Worker {name} starting")
    await asyncio.sleep(1)
    print(f"Worker {name} done")

def run_loop(name: str) -> None:
    asyncio.run(worker(name))

threads = [
    threading.Thread(target=run_loop, args=(f"T{i}",))
    for i in range(4)
]
for t in threads:
    t.start()
for t in threads:
    t.join()

```

Here every thread spins up an event loop of its own via [`asyncio.run()`](https://docs.python.org/3.14/library/asyncio-runner.html#asyncio.run) and drives a coroutine on it. The threads proceed concurrently, and on a free-threaded build they can occupy distinct CPU cores at the same time.

[Subject index](INDEX.md) · [Previous](thread-safety-considerations.md) · [Continue](producer-consumer-across-threads.md)
