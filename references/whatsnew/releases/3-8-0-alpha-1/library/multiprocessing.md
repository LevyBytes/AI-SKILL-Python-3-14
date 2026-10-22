# Python 3.8.0 alpha 1 / library / multiprocessing

[bpo-33929](https://bugs.python.org/issue?@action=redirect&bpo=33929): multiprocessing: Resolved a race condition inside Popen of multiprocessing.popen_spawn_win32. The child process now clones the read end of pipe rather than "stealing" it. Earlier, that read end of pipe was "stolen" by the child process, yet a handle leaked whenever the child had been terminated before it managed to steal the handle away from the parent process.

[bpo-35813](https://bugs.python.org/issue?@action=redirect&bpo=35813): A shared memory submodule was added to multiprocessing, removing the requirement to serialize data between processes

[bpo-33329](https://bugs.python.org/issue?@action=redirect&bpo=33329): Repair a multiprocessing regression affecting newer glibcs

[bpo-22872](https://bugs.python.org/issue?@action=redirect&bpo=22872): Once the queue is closed, [`multiprocessing.Queue.put()`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.Queue.put) and [`multiprocessing.Queue.get()`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.Queue.get) now raise [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) rather than [`AssertionError`](https://docs.python.org/3.14/library/exceptions.html#AssertionError) and [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) respectively. Zackery Spytz wrote the patch.

[bpo-35491](https://bugs.python.org/issue?@action=redirect&bpo=35491): [`multiprocessing`](https://docs.python.org/3.14/library/multiprocessing.html#module-multiprocessing): Add `Pool.__repr__()` and improve `BaseProcess.__repr__()` (now carrying pid and parent pid) to make debugging easier. The Pool state constant values are now strings rather than integers; as an example, the `RUN` value becomes `'RUN'` instead of `0`.

[bpo-35152](https://bugs.python.org/issue?@action=redirect&bpo=35152): Permit transmitting over 2 GB in one shot across a multiprocessing connection on systems other than Windows.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
