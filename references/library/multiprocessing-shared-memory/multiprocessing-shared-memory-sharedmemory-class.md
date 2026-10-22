# multiprocessing.shared_memory: `multiprocessing.shared_memory.SharedMemory`

# Multiprocessing.Shared Memory, Netdata

## Overview

Covers: multiprocessing.shared_memory — Shared memory for direct access across processes; Internet Data Handling.

## multiprocessing.shared_memory — Shared memory for direct access across processes

### `multiprocessing.shared_memory` — Shared memory for direct access across processes

**Source code:** [Lib/multiprocessing/shared_memory.py](https://github.com/python/cpython/tree/3.14/Lib/multiprocessing/shared_memory.py)

Added in version 3.8.

---

A class named `SharedMemory` is supplied here for allocating and managing shared memory that one or more processes can reach on a multicore or symmetric multiprocessor (SMP) machine. The [`multiprocessing.managers`](https://docs.python.org/3.14/library/multiprocessing.html#module-multiprocessing.managers) module additionally supplies `SharedMemoryManager`, a subclass of [`BaseManager`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.managers.BaseManager), to help manage the life-cycle of shared memory, particularly when several separate processes are involved.

Within this module, the term shared memory denotes “POSIX style” shared memory blocks (even though the implementation need not literally be that) rather than “distributed shared memory”. With this form of shared memory, separate processes are able to read from and write to a single common (or shared) region of volatile memory. Although a process is normally restricted to reaching only its own process memory space, shared memory makes it possible to share data between processes without having to instead pass messages that carry that data between them. Moving data directly through memory can yield substantial performance gains relative to moving it through disk or socket or some other communication channel that demands serialization/deserialization plus copying of the data.

 *class *multiprocessing.shared_memory.SharedMemory(*name=None*, *create=False*, *size=0*, ***, *track=True*)

Build an instance of the `SharedMemory` class to either make a fresh shared memory block or connect to an already existing one. A unique name is given to every shared memory block. Through this mechanism, one process can make a shared memory block under a chosen name while another process attaches to that very same block by referencing that same name.

Being a means for sharing data between processes, shared memory blocks can persist beyond the original process that brought them into being. Once a given process has no further need for a shared memory block that other processes may still rely on, that process should invoke the `close()` method. After no process at all still needs a shared memory block, the `unlink()` method ought to be invoked so that cleanup is handled correctly.

Parameters:

- **name** ([*str*](https://docs.python.org/3.14/library/stdtypes.html#str)* | **None*) – The requested shared memory’s unique name, given as a string. While making a fresh shared memory block, passing `None` (which is the default) as the name causes a fresh name to be produced.

- **create** ([*bool*](https://docs.python.org/3.14/library/functions.html#bool)) – Governs whether a fresh shared memory block gets made (`True`) or an existing one is attached instead (`False`).

- **size** ([*int*](https://docs.python.org/3.14/library/functions.html#int)) – The byte count requested while making a new shared memory block. Since certain platforms opt to hand out memory in chunks sized to that platform’s memory page size, a shared memory block’s actual size can end up larger than or equal to the size that was asked for. The *size* argument is disregarded when attaching to a shared memory block that already exists.

- **track** ([*bool*](https://docs.python.org/3.14/library/functions.html#bool)) – With `True`, the shared memory block is registered with a resource tracker process on platforms whose OS does not handle this on its own. That resource tracker guarantees the shared memory is cleaned up correctly even when every other process holding access to the memory quits without doing so. Python processes that descend from a shared ancestor via [`multiprocessing`](https://docs.python.org/3.14/library/multiprocessing.html#module-multiprocessing) facilities all rely on one common resource tracker process, and those processes manage the lifetime of shared memory segments automatically among themselves. Any Python process spawned by some other route gets its own resource tracker once it reaches shared memory with *track* turned on. The consequence is that the shared memory gets removed by the resource tracker belonging to whichever process exits first. So as to sidestep this problem, those working with [`subprocess`](https://docs.python.org/3.14/library/subprocess.html#module-subprocess) or with standalone Python processes ought to give *track* the value `False` whenever some other process is already handling that bookkeeping. On Windows, *track* is disregarded, since Windows performs its own tracking and removes shared memory automatically as soon as every handle to it is closed.

Changed in version 3.13: Added the *track* parameter.

[Subject index](INDEX.md) · [Continue](shared-memory-close-and-unlink.md)
