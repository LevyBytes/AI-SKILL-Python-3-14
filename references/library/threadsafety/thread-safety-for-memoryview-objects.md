# Thread safety for memoryview objects

### Thread safety for memoryview objects

[`memoryview`](https://docs.python.org/3.14/library/stdtypes.html#memoryview) objects expose the inner data of some underlying object without making a copy. Whether they are thread-safe rests on both the memoryview itself and the underlying buffer exporter.

The memoryview implementation tracks its own exports through atomic operations under the [free-threaded build](https://docs.python.org/3.14/glossary.html#term-free-threaded-build). Both creating and releasing a memoryview are thread-safe. Attribute access (for example [`shape`](https://docs.python.org/3.14/library/stdtypes.html#memoryview.shape), [`format`](https://docs.python.org/3.14/library/stdtypes.html#memoryview.format)) reads fields that stay immutable across the memoryview's lifetime, so simultaneous reads are fine provided the memoryview has not yet been released.

The actual data reached through the memoryview, however, belongs to the underlying object. Simultaneous access to that data is fine only where the underlying object permits it:

- With immutable objects like [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes), simultaneous reads via several memoryviews are fine.

- With mutable objects like [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray), reading and writing one memory region from several threads with no external synchronization is unsafe and can lead to data corruption. Be aware that even read-only memoryviews onto mutable objects do not guard against data races should another thread modify the underlying object.

```python
# NOT safe: concurrent writes to the same buffer
data = bytearray(1000)
view = memoryview(data)
# Thread 1: view[0:500] = b'x' * 500
# Thread 2: view[0:500] = b'y' * 500

```

```python
# Safe: use a lock for concurrent access
import threading
lock = threading.Lock()
data = bytearray(1000)
view = memoryview(data)

with lock:
    view[0:500] = b'x' * 500

```

Resizing or reallocating the underlying object (for instance by calling [`bytearray.resize()`](https://docs.python.org/3.14/library/stdtypes.html#bytearray.resize)) while a memoryview stays exported raises [`BufferError`](https://docs.python.org/3.14/library/exceptions.html#BufferError). That holds no matter what the threading looks like.

[Subject index](INDEX.md) · [Previous](thread-safety-for-bytearray-objects.md)
