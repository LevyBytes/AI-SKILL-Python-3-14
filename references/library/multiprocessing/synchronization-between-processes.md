# multiprocessing - Synchronization between processes

### Synchronization between processes

`multiprocessing` contains equivalents of all the synchronization primitives from [`threading`](https://docs.python.org/3.14/library/threading.html#module-threading). As one example, a lock can guarantee that only a single process writes to standard output at any given moment:

```python
from multiprocessing import Process, Lock

def f(l, i):
    l.acquire()
    try:
        print('hello world', i)
    finally:
        l.release()

if __name__ == '__main__':
    lock = Lock()

    for num in range(10):
        Process(target=f, args=(lock, num)).start()

```

Skip the lock and the output streaming from the separate processes is apt to become jumbled together.

[Subject index](INDEX.md) · [Previous](exchanging-objects-between-processes.md) · [Continue](sharing-state-between-processes.md) · [Owning module, declaration or section: multiprocessing](multiprocessing-process-based-parallelism.md)
