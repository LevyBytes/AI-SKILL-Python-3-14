# multiprocessing.shared_memory.SharedMemory: `close()`, `unlink()`

close()

Shut the file descriptor/handle to the shared memory belonging to this instance. `close()` ought to be invoked the moment this instance no longer requires access to the shared memory block. The underlying memory may or may not actually be released even after every handle to it is closed, depending on the operating system. Use the `unlink()` method so that cleanup happens correctly.

 unlink()

Remove the underlying shared memory block. Invoke this just a single time for each shared memory block, no matter how many handles reach it, even across other processes. The calls `unlink()` and `close()` may happen in either order, yet attempting to reach data within a shared memory block once `unlink()` has run can trigger memory access errors, which depends on the platform.

On Windows this method does nothing, since closing every handle is the sole means of removing a shared memory block there.

 buf

A memoryview of contents of the shared memory block.

 name

Read-only access to the unique name of the shared memory block.

[Subject index](INDEX.md) · [Previous](multiprocessing-shared-memory-sharedmemory-class.md) · [Continue](sharedmemory-buffer-contract.md) · [Owning module, declaration or section: multiprocessing.shared_memory](multiprocessing-shared-memory-sharedmemory-class.md) · [Owning module, declaration or section: multiprocessing.shared_memory.SharedMemory](multiprocessing-shared-memory-sharedmemory-class.md)
