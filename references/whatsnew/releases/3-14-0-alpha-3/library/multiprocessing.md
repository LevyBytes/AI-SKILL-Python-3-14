# Python 3.14.0 alpha 3 / library / multiprocessing

[gh-88110](https://github.com/python/cpython/issues/88110): A [`multiprocessing.Process`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.Process) no longer reports a `.exitcode` of 1 on a successful run; this previously happened with the `"fork"` start method alongside a [`concurrent.futures.ThreadPoolExecutor`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor).

[gh-97514](https://github.com/python/cpython/issues/97514): The control socket for the [`multiprocessing`](https://docs.python.org/3.14/library/multiprocessing.html#module-multiprocessing) forkserver start method gained authentication, restricting control to processes holding the authentication key minted by whichever process spawned the forkserver. Compared with the earlier [gh-97514](https://github.com/python/cpython/issues/97514) work, this means filesystem permissions are no longer the sole gatekeeper.

Across every platform that supports forkserver, swapping file descriptors for control pipes with the forked worker now demands that an explicit acknowledgement byte travel back over the socket once the exchange completes. Verifying all of this becomes far simpler as a result.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
