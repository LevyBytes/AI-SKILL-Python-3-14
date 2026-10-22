# multiprocessing: `multiprocessing.sharedctypes.RawArray()`, `multiprocessing.sharedctypes.RawValue()`, `multiprocessing.sharedctypes.Array()`, `multiprocessing.sharedctypes.Value()`, `multiprocessing.sharedctypes.copy()`

#### The `multiprocessing.sharedctypes` module

The `multiprocessing.sharedctypes` module supplies functions for carving [`ctypes`](https://docs.python.org/3.14/library/ctypes.html#module-ctypes) objects out of shared memory that child processes can inherit.

Note

Even though you can stash a pointer in shared memory, bear in mind that it points at a spot inside one particular process's address space. The pointer, however, is quite likely meaningless within a second process, and trying to dereference it from that second process may bring on a crash.

 multiprocessing.sharedctypes.RawArray(*typecode_or_type*, *size_or_initializer*)

Give back a ctypes array carved out of shared memory.

*typecode_or_type* fixes the element type of the array returned: it is either a ctypes type or a single-character typecode of the sort the [`array`](https://docs.python.org/3.14/library/array.html#module-array) module uses. When *size_or_initializer* is an integer, it fixes the array's length, and the array starts out zeroed. Otherwise *size_or_initializer* is a sequence that seeds the array and whose length fixes the array's length.

Be aware that reading or writing an element might not be atomic – reach for `Array()` instead so that a lock automatically synchronizes access.

 multiprocessing.sharedctypes.RawValue(*typecode_or_type*, **args*)

Give back a ctypes object carved out of shared memory.

*typecode_or_type* fixes the type of the object returned: it is either a ctypes type or a single-character typecode of the sort the [`array`](https://docs.python.org/3.14/library/array.html#module-array) module uses. **args* gets forwarded to the type's constructor.

Be aware that reading or writing the value might not be atomic – reach for `Value()` instead so that a lock automatically synchronizes access.

Note that an array of [`ctypes.c_char`](https://docs.python.org/3.14/library/ctypes.html#ctypes.c_char) has `value` and `raw` attributes that let you put it to use storing and fetching strings – see documentation for [`ctypes`](https://docs.python.org/3.14/library/ctypes.html#module-ctypes).

 multiprocessing.sharedctypes.Array(*typecode_or_type*, *size_or_initializer*, ***, *lock=True*, *ctx=None*)

The same as `RawArray()`, except that, hinging on the value of *lock*, a process-safe synchronization wrapper may come back rather than a raw ctypes array.

When *lock* is `True` (the default), a fresh lock object is made to coordinate access to the value. When *lock* is a `Lock` or `RLock` object, that one is used to coordinate access to the value. When *lock* is `False`, access to the object returned will not be guarded by a lock automatically, so it will not necessarily be “process-safe”.

*ctx* is either a context object or `None` (which uses the current context). With `None`, this call can fix the global start method. See Global start method for more details.

Note that *lock* and *ctx* are keyword-only parameters.

 multiprocessing.sharedctypes.Value(*typecode_or_type*, **args*, *lock=True*, *ctx=None*)

The same as `RawValue()`, except that, hinging on the value of *lock*, a process-safe synchronization wrapper may come back rather than a raw ctypes object.

When *lock* is `True` (the default), a fresh lock object is made to coordinate access to the value. When *lock* is a `Lock` or `RLock` object, that one is used to coordinate access to the value. When *lock* is `False`, access to the object returned will not be guarded by a lock automatically, so it will not necessarily be “process-safe”.

*ctx* is either a context object or `None` (which uses the current context). With `None`, this call can fix the global start method. See Global start method for more details.

Note that *lock* and *ctx* are keyword-only parameters.

 multiprocessing.sharedctypes.copy(*obj*)

Give back a ctypes object carved out of shared memory that copies the ctypes object *obj*.

[Subject index](INDEX.md) · [Previous](multiprocessing-value-to-multiprocessing-array.md) · [Continue](multiprocessing-sharedctypes-synchronized.md) · [Owning module, declaration or section: multiprocessing](multiprocessing-process-based-parallelism.md)
