# multiprocessing — Sharing state between processes

### Sharing state between processes

As the earlier discussion mentioned, in concurrent programming it is generally wisest to steer clear of shared state as much as you can. That advice holds especially when several processes are involved.

That said, if you genuinely must share some data, `multiprocessing` gives you a couple of options for doing it.

**Shared memory**

>

You can keep data in a shared memory map by using `Value` or `Array`. For instance, the code below

```python
from multiprocessing import Process, Value, Array

def f(n, a):
    n.value = 3.1415927
    for i in range(len(a)):
        a[i] = -a[i]

if __name__ == '__main__':
    num = Value('d', 0.0)
    arr = Array('i', range(10))

    p = Process(target=f, args=(num, arr))
    p.start()
    p.join()

    print(num.value)
    print(arr[:])

```

will print

```python
3.1415927
[0, -1, -2, -3, -4, -5, -6, -7, -8, -9]

```

The `'d'` and `'i'` arguments supplied while constructing `num` and `arr` are typecodes of the sort the [`array`](https://docs.python.org/3.14/library/array.html#module-array) module uses: `'d'` stands for a double precision float, whereas `'i'` stands for a signed integer. Both shared objects are safe across processes and threads.

If you want more flexibility with shared memory, the `multiprocessing.sharedctypes` module supports building arbitrary ctypes objects out of shared memory.

**Server process**

>

A manager object handed back by `Manager()` governs a server process that holds Python objects and lets other processes operate on them through proxies.

A manager handed back by `Manager()` will support types [`list`](https://docs.python.org/3.14/library/stdtypes.html#list), [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict), [`set`](https://docs.python.org/3.14/library/stdtypes.html#set), `Namespace`, `Lock`, `RLock`, `Semaphore`, `BoundedSemaphore`, `Condition`, `Event`, `Barrier`, `Queue`, `Value` and `Array`. For example,

```python
from multiprocessing import Process, Manager

def f(d, l, s):
    d[1] = '1'
    d['2'] = 2
    d[0.25] = None
    l.reverse()
    s.add('a')
    s.add('b')

if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict()
        l = manager.list(range(10))
        s = manager.set()

        p = Process(target=f, args=(d, l, s))
        p.start()
        p.join()

        print(d)
        print(l)
        print(s)

```

will print

```python
{0.25: None, 1: '1', '2': 2}
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
{'a', 'b'}

```

Managers running server processes are more flexible than shared memory objects, because you can make them support arbitrary object types. On top of that, one manager can be shared across processes on separate computers over a network. They are, however, slower than using shared memory.

[Subject index](INDEX.md) · [Previous](synchronization-between-processes.md) · [Continue](using-a-pool-of-workers.md) · [Owning module, declaration or section: multiprocessing](multiprocessing-process-based-parallelism.md)
