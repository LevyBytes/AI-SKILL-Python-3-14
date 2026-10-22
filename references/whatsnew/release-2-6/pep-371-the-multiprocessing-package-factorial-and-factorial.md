# What’s New in Python 2.6 / PEP 371: The `multiprocessing` Package — multiprocessing, queue, threading

Initially the [`multiprocessing`](https://docs.python.org/3.14/library/multiprocessing.html#module-multiprocessing) module was conceived as a faithful clone of the [`threading`](https://docs.python.org/3.14/library/threading.html#module-threading) module, swapping processes in for threads. While that aim was dropped before Python 2.6 shipped, the module's overall design still resembles its predecessor. At its core sits the [`Process`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.Process) class, which receives a callable plus a tuple of arguments. Invoking the [`start()`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.Process.start) method launches that callable inside a subprocess; from there you may call [`is_alive()`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.Process.is_alive) to test whether the subprocess keeps running, and [`join()`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.Process.join) to block until that process finishes.

Below is a brief example in which the subprocess computes a factorial. The routine that performs the math is coded oddly, deliberately taking far longer whenever its input argument happens to be a multiple of 4.

```python
import time
from multiprocessing import Process, Queue

def factorial(queue, N):
    "Compute a factorial."
    # If N is a multiple of 4, this function will take much longer.
    if (N % 4) == 0:
        time.sleep(.05 * N/4)

    # Calculate the result
    fact = 1L
    for i in range(1, N+1):
        fact = fact * i

    # Put the result on the queue
    queue.put(fact)

if __name__ == '__main__':
    queue = Queue()

    N = 5

    p = Process(target=factorial, args=(queue, N))
    p.start()
    p.join()

    result = queue.get()
    print 'Factorial', N, '=', result

```

To pass the factorial result back, a [`Queue`](https://docs.python.org/3.14/library/queue.html#queue.Queue) is employed. That `Queue` object lives in a global variable. The newly spawned child sees whatever the variable held at creation time; since it is a `Queue`, both parent and child can rely on that object as a communication channel. (Were the parent to reassign the global variable afterward, the child's copy would stay the same, and the reverse holds too.)

A pair of additional classes, [`Pool`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.pool.Pool) and [`Manager`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.Manager), offer higher-level facilities. A `Pool` spins up a set number of worker processes; you then hand work to those workers either by calling [`apply()`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.pool.Pool.apply) or [`apply_async()`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.pool.Pool.apply_async) for one request at a time, or by calling [`map()`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.pool.Pool.map) or [`map_async()`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.pool.Pool.map_async) to queue many at once. In the snippet that follows, a `Pool` distributes requests over 5 worker processes and gathers back a list of results:

```python
from multiprocessing import Pool

def factorial(N, dictionary):
    "Compute a factorial."
    ...
p = Pool(5)
result = p.map(factorial, range(1, 1000, 10))
for v in result:
    print v

```

The output it generates looks like this:

```python
1
39916800
51090942171709440000
8222838654177922817725562880000000
33452526613163807108170062053440751665152000000000
...

```

The remaining high-level facility, the [`Manager`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.Manager) class, spins up a dedicated server process able to keep authoritative copies of Python data structures. Any other process may then read and alter those structures through proxy objects. In the next example a shared dictionary is built by calling the [`dict()`](https://docs.python.org/3.14/library/stdtypes.html#dict) method, after which the worker processes write entries into it. (No automatic locking happens here, which has no bearing on this particular example. The methods on a `Manager` also cover [`Lock()`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.managers.SyncManager.Lock), [`RLock()`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.managers.SyncManager.RLock), and [`Semaphore()`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.managers.SyncManager.Semaphore) for building shared locks.)

[Subject index](INDEX.md) · [Next source section](pep-371-the-multiprocessing-package-factorial.md) · [Release/subject declaration](python-3-0.md) · [Release/subject declaration](multiprocessing-package-introduction.md) · [Preceding release/subject continuation](multiprocessing-package-introduction.md)
