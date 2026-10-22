# Queues

# Asyncio Queue, Asyncio Runner

## Overview

Covers: Queues; Runners.

## Queues

### Queues

**Source code:** [Lib/asyncio/queues.py](https://github.com/python/cpython/tree/3.14/Lib/asyncio/queues.py)

---

The asyncio queues take their shape from the classes found in the [`queue`](https://docs.python.org/3.14/library/queue.html#module-queue) module. They are not thread-safe, having been built expressly for use inside async/await code.

Bear in mind that no method on an asyncio queue takes a *timeout* parameter; to give a queue operation a timeout, wrap it with the [`asyncio.wait_for()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.wait_for) function.

See also the Examples section below.

[Subject index](INDEX.md) · [Continue](asyncio-queue-class.md)
