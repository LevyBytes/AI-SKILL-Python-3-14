# multiprocessing — Shared `ctypes` Objects

### Shared [`ctypes`](https://docs.python.org/3.14/library/ctypes.html#module-ctypes) Objects

Shared objects can be made out of shared memory and inherited by child processes.

 multiprocessing.Value(*typecode_or_type*, **args*, *lock=True*)

Give back a [`ctypes`](https://docs.python.org/3.14/library/ctypes.html#module-ctypes) object carved out of shared memory. By default what comes back is in fact a synchronized wrapper around the object. The object itself is reachable through the *value* attribute of a `Value`.

*typecode_or_type* fixes the type of the object returned: it is either a ctypes type or a single-character typecode of the sort the [`array`](https://docs.python.org/3.14/library/array.html#module-array) module uses. **args* gets forwarded to the type's constructor.

When *lock* is `True` (the default), a fresh recursive lock object is made to coordinate access to the value. When *lock* is a `Lock` or `RLock` object, that one is used to coordinate access to the value. When *lock* is `False`, access to the object returned will not be guarded by a lock automatically, so it will not necessarily be “process-safe”.

Operations such as `+=`, which read and write, are not atomic. So if, say, you want to atomically increment a shared value, just doing the following falls short

```python
counter.value += 1

```

As long as the lock tied to it is recursive (the default), the following works instead

```python
with counter.get_lock():
    counter.value += 1

```

Note that *lock* is a keyword-only argument.

 multiprocessing.Array(*typecode_or_type*, *size_or_initializer*, ***, *lock=True*)

Give back a ctypes array carved out of shared memory. By default what comes back is in fact a synchronized wrapper around the array.

*typecode_or_type* fixes the element type of the array returned: it is either a [ctypes type](https://docs.python.org/3.14/library/ctypes.html#ctypes-fundamental-data-types) or a single-character typecode of the sort the [`array`](https://docs.python.org/3.14/library/array.html#module-array) module uses, with `'w'` being the exception that is unsupported. On top of that, the `'c'` typecode is an alias for [`ctypes.c_char`](https://docs.python.org/3.14/library/ctypes.html#ctypes.c_char). When *size_or_initializer* is an integer, it fixes the array's length, and the array starts out zeroed. Otherwise, *size_or_initializer* is a sequence that seeds the array and whose length fixes the array's length.

When *lock* is `True` (the default), a fresh lock object is made to coordinate access to the value. When *lock* is a `Lock` or `RLock` object, that one is used to coordinate access to the value. When *lock* is `False`, access to the object returned will not be guarded by a lock automatically, so it will not necessarily be “process-safe”.

Note that *lock* is a keyword only argument.

Note that an array of [`ctypes.c_char`](https://docs.python.org/3.14/library/ctypes.html#ctypes.c_char) carries *value* and *raw* attributes, both usable to store and retrieve byte strings. While *raw* lets you work with a [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) object spanning the array's full size, reading *value* stops at a null byte, the way most programming languages treat strings.

[Subject index](INDEX.md) · [Previous](process-semaphore-contract.md) · [Continue](shared-ctypes-arrays-values-and-copying.md) · [Owning module, declaration or section: multiprocessing](multiprocessing-process-based-parallelism.md)
