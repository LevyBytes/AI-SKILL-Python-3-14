# Python 3.13.0 alpha 1 / library / concurrent futures

[gh-109047](https://github.com/python/cpython/issues/109047): Within [`concurrent.futures`](https://docs.python.org/3.14/library/concurrent.futures.html#module-concurrent.futures): the *executor manager thread* now traps exceptions while placing an item onto the *call queue*. As Python finalizes, spawning a fresh thread may now raise [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError). When that happens the exception is caught and `terminate_broken()` gets called. Victor Stinner authored this patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
