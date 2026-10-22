# multiprocessing.shared_memory / Shared memory for direct access across processes: `multiprocessing.shared_memory.ShareableList`, `int()`, `str()`, `bytes()`, `count()`, `index()`

*class *multiprocessing.shared_memory.ShareableList(*sequence=None*, ***, *name=None*)

Supply a mutable list-like object in which every value held inside lives in a shared memory block. This restricts the values that can be stored to these built-in data types:

- [`int`](https://docs.python.org/3.14/library/functions.html#int) (signed 64-bit)

- [`float`](https://docs.python.org/3.14/library/functions.html#float)

- [`bool`](https://docs.python.org/3.14/library/functions.html#bool)

- [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) (less than 10M bytes each when encoded as UTF-8)

- [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) (less than 10M bytes each)

- `None`

A further noteworthy contrast with the built-in [`list`](https://docs.python.org/3.14/library/stdtypes.html#list) type is that these lists are unable to alter their total length (that is, there is no `append()`, `insert()`, etc.) and they offer no dynamic creation of new `ShareableList` instances through slicing.

*sequence* serves to fill a new `ShareableList` with values. Set it to `None` so as to instead attach to a `ShareableList` that already exists by way of its unique shared memory name.

*name* gives the requested shared memory its unique name, just as laid out in the `SharedMemory` definition. As you attach to a `ShareableList` that already exists, hand over the unique name of its shared memory block and keep *sequence* at `None`.

Note

There is a known issue affecting [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) and [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) values. Should they finish with `\x00` nul bytes or characters, those can be *silently stripped* as you retrieve them by index out of the `ShareableList`. That `.rstrip(b'\x00')` behavior counts as a bug and might disappear later on. See [gh-106939](https://github.com/python/cpython/issues/106939).

In applications where stripping the trailing nulls causes trouble, get around it by always, without exception, tacking an extra non-0 byte onto the end of such values as you store them and unconditionally taking it back off as you retrieve them:

```pycon
>>> from multiprocessing import shared_memory
>>> nul_bug_demo = shared_memory.ShareableList(['?\x00', b'\x03\x02\x01\x00\x00\x00'])
>>> nul_bug_demo[0]
'?'
>>> nul_bug_demo[1]
b'\x03\x02\x01'
>>> nul_bug_demo.shm.unlink()
>>> padded = shared_memory.ShareableList(['?\x00\x07', b'\x03\x02\x01\x00\x00\x00\x07'])
>>> padded[0][:-1]
'?\x00'
>>> padded[1][:-1]
b'\x03\x02\x01\x00\x00\x00'
>>> padded.shm.unlink()

```

 count(*value*)

Return the number of occurrences of *value*.

 index(*value*)

Return first index position of *value*. Raise [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) if *value* is not present.

 format

A read-only attribute that holds the [`struct`](https://docs.python.org/3.14/library/struct.html#module-struct) packing format applied across every value presently held.

[Subject index](INDEX.md) · [Previous](cross-process-shared-memory-overview.md) · [Continue](shareablelist-storage-contract.md) · [Owning module, declaration or section: multiprocessing.shared_memory](multiprocessing-shared-memory-sharedmemory-class.md)
