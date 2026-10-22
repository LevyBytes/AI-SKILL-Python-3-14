# multiprocessing: `multiprocessing.sharedctypes.synchronized()`

multiprocessing.sharedctypes.synchronized(*obj*, *lock=None*, *ctx=None*)

Give back a process-safe wrapper object around a ctypes object, using *lock* to coordinate access. When *lock* is `None` (the default), a `multiprocessing.RLock` object gets made automatically.

*ctx* is either a context object or `None` (which uses the current context). With `None`, this call can fix the global start method. See Global start method for more details.

Beyond the methods of the object it wraps, a synchronized wrapper carries two more: `get_obj()` gives back the wrapped object and `get_lock()` gives back the lock object used for coordination.

Note that reaching the ctypes object through the wrapper can run far slower than reaching the raw ctypes object directly.

Changed in version 3.5: Synchronized objects support the [context manager](https://docs.python.org/3.14/glossary.html#term-context-manager) protocol.

The table below sets the syntax for making shared ctypes objects out of shared memory next to the ordinary ctypes syntax. (Within the table, `MyStruct` is some subclass of [`ctypes.Structure`](https://docs.python.org/3.14/library/ctypes.html#ctypes.Structure).)

| ctypes | sharedctypes using type | sharedctypes using typecode |
| --- | --- | --- |
| c_double(2.4) | RawValue(c_double, 2.4) | RawValue(‘d’, 2.4) |
| MyStruct(4, 6) | RawValue(MyStruct, 4, 6) |  |
| (c_short * 7)() | RawArray(c_short, 7) | RawArray(‘h’, 7) |
| (c_int * 3)(9, 2, 8) | RawArray(c_int, (9, 2, 8)) | RawArray(‘i’, (9, 2, 8)) |

Here is an example in which a child process alters a number of ctypes objects:

```python
from multiprocessing import Process, Lock
from multiprocessing.sharedctypes import Value, Array
from ctypes import Structure, c_double

class Point(Structure):
    _fields_ = [('x', c_double), ('y', c_double)]

def modify(n, x, s, A):
    n.value **= 2
    x.value **= 2
    s.value = s.value.upper()
    for a in A:
        a.x **= 2
        a.y **= 2

if __name__ == '__main__':
    lock = Lock()

    n = Value('i', 7)
    x = Value(c_double, 1.0/3.0, lock=False)
    s = Array('c', b'hello world', lock=lock)
    A = Array(Point, [(1.875,-6.25), (-5.75,2.0), (2.375,9.5)], lock=lock)

    p = Process(target=modify, args=(n, x, s, A))
    p.start()
    p.join()

    print(n.value)
    print(x.value)
    print(s.value)
    print([(a.x, a.y) for a in A])

```

The results printed are

```none
49
0.1111111111111111
HELLO WORLD
[(3.515625, 39.0625), (33.0625, 4.0), (5.640625, 90.25)]

```

[Subject index](INDEX.md) · [Previous](shared-ctypes-arrays-values-and-copying.md) · [Continue](multiprocessing-manager.md) · [Owning module, declaration or section: multiprocessing](multiprocessing-process-based-parallelism.md) · [Owning module, declaration or section: The `multiprocessing.sharedctypes` module](shared-ctypes-arrays-values-and-copying.md)
