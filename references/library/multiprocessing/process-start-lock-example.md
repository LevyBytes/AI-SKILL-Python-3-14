# multiprocessing - All start methods - Code example: from multiprocessing import Process, Lock

```python
from multiprocessing import Process, Lock

def f():
    ... do something using "lock" ...

if __name__ == '__main__':
    lock = Lock()
    for i in range(10):
        Process(target=f).start()

```

should be rewritten as

```python
from multiprocessing import Process, Lock

def f(l):
    ... do something using "l" ...

if __name__ == '__main__':
    lock = Lock()
    for i in range(10):
        Process(target=f, args=(lock,)).start()

```

Beware of replacing [`sys.stdin`](https://docs.python.org/3.14/library/sys.html#sys.stdin) with a “file like object”

>

`multiprocessing` once unconditionally called:

```python
os.close(sys.stdin.fileno())

```

within the `multiprocessing.Process._bootstrap()` method — which led to trouble with processes-in-processes. That has been switched to:

```python
sys.stdin.close()
sys.stdin = open(os.open(os.devnull, os.O_RDONLY), closefd=False)

```

This fixes the core problem of processes colliding with each other and producing a bad file descriptor error, yet it brings a potential hazard for applications that swap [`sys.stdin()`](https://docs.python.org/3.14/library/sys.html#sys.stdin) for a “file-like object” with output buffering. The hazard is that, should several processes call [`close()`](https://docs.python.org/3.14/library/io.html#io.IOBase.close) on this file-like object, the same data could end up flushed to the object more than once, producing corruption.

When you write a file-like object and roll your own caching, you can make it fork-safe by recording the pid each time you append to the cache, and dropping the cache once the pid changes. To illustrate:

```python
@property
def cache(self):
    pid = os.getpid()
    if pid != self._pid:
        self._pid = pid
        self._cache = []
    return self._cache

```

For more information, see [bpo-5155](https://bugs.python.org/issue?@action=redirect&bpo=5155), [bpo-5313](https://bugs.python.org/issue?@action=redirect&bpo=5313) and [bpo-5331](https://bugs.python.org/issue?@action=redirect&bpo=5331)

[Subject index](INDEX.md) · [Previous](all-start-methods-section-introduction-and-initial-examples.md) · [Continue](the-spawn-and-forkserver-start-methods.md) · [Owning module, declaration or section: multiprocessing](multiprocessing-process-based-parallelism.md) · [Owning module, declaration or section: All start methods](all-start-methods-section-introduction-and-initial-examples.md)
