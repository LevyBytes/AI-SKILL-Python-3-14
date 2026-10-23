# What's New In Python 3.6 / PYTHONMALLOC environment variable - tracemalloc

A check now confirms the [GIL](https://docs.python.org/3.14/glossary.html#term-global-interpreter-lock) is being held whenever the allocator routines for the [`PYMEM_DOMAIN_OBJ`](https://docs.python.org/3.14/c-api/memory.html#c.PYMEM_DOMAIN_OBJ) (ex: [`PyObject_Malloc()`](https://docs.python.org/3.14/c-api/memory.html#c.PyObject_Malloc)) and [`PYMEM_DOMAIN_MEM`](https://docs.python.org/3.14/c-api/memory.html#c.PYMEM_DOMAIN_MEM) (ex: [`PyMem_Malloc()`](https://docs.python.org/3.14/c-api/memory.html#c.PyMem_Malloc)) domains run.

This verification that the GIL is being held also arrived as a fresh capability in Python 3.6.

Consult the [`PyMem_SetupDebugHooks()`](https://docs.python.org/3.14/c-api/memory.html#c.PyMem_SetupDebugHooks) routine to learn about debug hooks for Python memory allocators.

You can now also compel every Python memory allocation to route through the C library's `malloc()` allocator by setting `PYTHONMALLOC=malloc`. That proves useful when running outside memory debuggers such as Valgrind against a Python built in release mode.

When something goes wrong, the debug hooks for Python memory allocators now consult the [`tracemalloc`](https://docs.python.org/3.14/library/tracemalloc.html#module-tracemalloc) module so they can report the traceback recording where a memory block originated.

Here is a sample fatal error triggered by a buffer overflow with `python3.6 -X tracemalloc=5` (store 5 frames in traces):

```python
Debug memory block at address p=0x7fbcd41666f8: API 'o'
    4 bytes originally requested
    The 7 pad bytes at p-7 are FORBIDDENBYTE, as expected.
    The 8 pad bytes at tail=0x7fbcd41666fc are not all FORBIDDENBYTE (0xfb):
        at tail+0: 0x02 *** OUCH
        at tail+1: 0xfb
        at tail+2: 0xfb
        at tail+3: 0xfb
        at tail+4: 0xfb
        at tail+5: 0xfb
        at tail+6: 0xfb
        at tail+7: 0xfb
    The block was made by call #1233329 to debug malloc/realloc.
    Data at p: 1a 2b 30 00

Memory block allocated at (most recent call first):
  File "test/test_bytes.py", line 323
  File "unittest/case.py", line 600
  File "unittest/case.py", line 648
  File "unittest/suite.py", line 122
  File "unittest/suite.py", line 84

Fatal Python error: bad trailing pad byte

Current thread 0x00007fbcdbd32700 (most recent call first):
  File "test/test_bytes.py", line 323 in test_hex
  File "unittest/case.py", line 600 in run
  File "unittest/case.py", line 648 in __call__
  File "unittest/suite.py", line 122 in run
  File "unittest/suite.py", line 84 in __call__
  File "unittest/suite.py", line 122 in run
  File "unittest/suite.py", line 84 in __call__
  ...

```

(Contributed by Victor Stinner in [bpo-26516](https://bugs.python.org/issue?@action=redirect&bpo=26516) and [bpo-26564](https://bugs.python.org/issue?@action=redirect&bpo=26564).)

### PYTHONMALLOC environment variable

The fresh [`PYTHONMALLOC`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONMALLOC) environment variable lets you choose the Python memory allocators and switch on debug hooks.

You can now turn on debug hooks for the Python memory allocators even on a Python built in release mode by way of `PYTHONMALLOC=debug`. What the debug hooks do:

- Memory just allocated gets filled with the byte `0xCB`

- Memory just freed gets filled with the byte `0xDB`

- Catch breaches of the Python memory allocator API. As an example, [`PyObject_Free()`](https://docs.python.org/3.14/c-api/memory.html#c.PyObject_Free) invoked on a block that [`PyMem_Malloc()`](https://docs.python.org/3.14/c-api/memory.html#c.PyMem_Malloc) had allocated.

- Catch writes ahead of where a buffer begins (buffer underflows)

- Catch writes past where a buffer ends (buffer overflows)

-

[Subject index](INDEX.md) · [Next source section](dtrace-and-systemtap-probing-support.md) · [Release/subject declaration](summary-release-highlights.md) · [Previous source section](pep-523-adding-a-frame-evaluation-api-to-cpython.md)
