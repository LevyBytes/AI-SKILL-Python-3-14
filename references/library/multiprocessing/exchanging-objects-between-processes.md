# multiprocessing — Exchanging objects between processes

### Exchanging objects between processes

`multiprocessing` provides two kinds of communication channel between processes:

**Queues**

>

The `Queue` class is a near clone of [`queue.Queue`](https://docs.python.org/3.14/library/queue.html#queue.Queue). For example:

```python
from multiprocessing import Process, Queue

def f(q):
    q.put([42, None, 'hello'])

if __name__ == '__main__':
    q = Queue()
    p = Process(target=f, args=(q,))
    p.start()
    print(q.get())    # prints "[42, None, 'hello']"
    p.join()

```

Queues are thread and process safe. Whatever object you place into a `multiprocessing` queue gets serialized.

**Pipes**

>

The `Pipe()` function hands back a pair of connection objects joined by a pipe, which defaults to being duplex (two-way). For example:

```python
from multiprocessing import Process, Pipe

def f(conn):
    conn.send([42, None, 'hello'])
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    p.start()
    print(parent_conn.recv())   # prints "[42, None, 'hello']"
    p.join()

```

The pair of connection objects handed back by `Pipe()` stand for the two ends of the pipe. Every connection object carries `send()` and `recv()` methods (along with others). Keep in mind that pipe data can be corrupted if two processes (or threads) attempt to read from or write to the *same* end of the pipe simultaneously. Naturally, there is no corruption danger when processes use distinct ends of the pipe at once.

The `send()` method serializes the object and `recv()` re-creates the object.

[Subject index](INDEX.md) · [Previous](contexts-and-start-methods.md) · [Continue](synchronization-between-processes.md) · [Owning module, declaration or section: multiprocessing](multiprocessing-process-based-parallelism.md)
