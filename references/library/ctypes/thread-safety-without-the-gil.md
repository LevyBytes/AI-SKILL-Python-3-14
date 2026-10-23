# ctypes - Thread safety without the GIL

### Thread safety without the GIL

Starting with Python 3.13, you can turn off the [GIL](https://docs.python.org/3.14/glossary.html#term-GIL) on the [free-threaded build](https://docs.python.org/3.14/glossary.html#term-free-threaded-build). Within ctypes, concurrent reads and writes targeting one object are safe, whereas spreading them across several objects is not:

>

```pycon
>>> number = c_int(42)
>>> pointer_a = pointer(number)
>>> pointer_b = pointer(number)

```

Here, when the GIL is off, only a single object may read and write that address at any given moment. That means you can hand `pointer_a` around and write through it from many threads, provided `pointer_b` isn’t trying to do the very same thing at the same time. Should that become a problem, reach for a [`threading.Lock`](https://docs.python.org/3.14/library/threading.html#threading.Lock) to coordinate memory access:

>

```pycon
>>> import threading
>>> lock = threading.Lock()
>>> # Thread 1
>>> with lock:
...    pointer_a.contents = 24
>>> # Thread 2
>>> with lock:
...    pointer_b.contents = 42

```

[Subject index](INDEX.md) · [Previous](pointers-code-example-null-ptr-pointer-c-int.md) · [Continue](type-conversions.md) · [Owning module, declaration or section: ctypes](ctypes-a-foreign-function-library-for-python.md)
