# Producer/consumer across threads

### Producer/consumer across threads

Whenever an ordinary (non-asyncio) thread has to pass work over to an asyncio event loop living in some other thread, reach for a thread-safe primitive like [`queue.Queue`](https://docs.python.org/3.14/library/queue.html#queue.Queue) in place of [`asyncio.Queue`](https://docs.python.org/3.14/library/asyncio-queue.html#asyncio.Queue), the latter being safe only inside one event loop.:

```python
import asyncio
import queue
import threading

def producer(q: queue.Queue[int]) -> None:
    for i in range(5):
        print(f"Producing {i}")
        q.put(i)
    q.shutdown()

async def consumer(q: queue.Queue[int]) -> None:
    while True:
        try:
            item = q.get_nowait()
        except queue.Empty:
            await asyncio.sleep(0.1)
            continue
        except queue.ShutDown:
            break
        print(f"Consumed {item}")
        await asyncio.sleep(item)

q: queue.Queue[int] = queue.Queue()
consumer_thread = threading.Thread(
    target=lambda: asyncio.run(consumer(q))
)
consumer_thread.start()
producer(q)
consumer_thread.join()

```

While the producer sits on the main thread and the consumer lives inside an event loop on a thread of its own, the two still exchange data safely by way of `queue.Queue`. Should the queue run dry, the consumer naps for a moment and retries. Once the producer finishes it invokes [`shutdown()`](https://docs.python.org/3.14/library/queue.html#queue.Queue.shutdown), after which later [`get_nowait()`](https://docs.python.org/3.14/library/queue.html#queue.Queue.get_nowait) calls raise [`queue.ShutDown`](https://docs.python.org/3.14/library/queue.html#queue.ShutDown), giving the consumer a clean way out.

[Subject index](INDEX.md) · [Previous](using-asyncio-with-threads.md) · [Continue](../asyncio/async-io-overview.md)
