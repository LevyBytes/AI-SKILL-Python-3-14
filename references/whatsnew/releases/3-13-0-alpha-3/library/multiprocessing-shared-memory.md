# Python 3.13.0 alpha 3 / library / multiprocessing shared memory

[gh-82300](https://github.com/python/cpython/issues/82300): A `track` parameter joins [`multiprocessing.shared_memory.SharedMemory`](https://docs.python.org/3.14/library/multiprocessing.shared_memory.html#multiprocessing.shared_memory.SharedMemory), letting you use shared memory blocks without registering them with the POSIX resource tracker that otherwise frees them automatically once the process exits.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
