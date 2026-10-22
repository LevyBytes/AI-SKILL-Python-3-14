# multiprocessing — Logging

### Logging

Logging gets a measure of support. Be aware, though, that since the [`logging`](https://docs.python.org/3.14/library/logging.html#module-logging) package skips process-shared locks, messages coming from separate processes can (according to the handler type) end up jumbled together.

 multiprocessing.get_logger()

Gives back the logger that `multiprocessing` uses. A new one gets created if needed.

When first created, the logger has level [`logging.NOTSET`](https://docs.python.org/3.14/library/logging.html#logging.NOTSET) and no default handler. By default, messages sent to this logger do not propagate up to the root logger.

Be aware that on Windows, what child processes inherit from the parent process's logger is only its level – every other tweak to the logger does not carry over.

 multiprocessing.log_to_stderr(*level=None*)

This function makes a call to `get_logger()` but, beyond handing back the logger that get_logger creates, it attaches a handler that routes output to [`sys.stderr`](https://docs.python.org/3.14/library/sys.html#sys.stderr) using format `'[%(levelname)s/%(processName)s] %(message)s'`. You can adjust the logger's `levelname` by passing a `level` argument.

An example session with logging switched on appears below:

```python
>>> import multiprocessing, logging
>>> logger = multiprocessing.log_to_stderr()
>>> logger.setLevel(logging.INFO)
>>> logger.warning('doomed')
[WARNING/MainProcess] doomed
>>> m = multiprocessing.Manager()
[INFO/SyncManager-...] child process calling self.run()
[INFO/SyncManager-...] created temp directory /.../pymp-...
[INFO/SyncManager-...] manager serving at '/.../listener-...'
>>> del m
[INFO/MainProcess] sending shutdown message to manager
[INFO/SyncManager-...] manager exiting with exitcode 0

```

For a full table of logging levels, see the [`logging`](https://docs.python.org/3.14/library/logging.html#module-logging) module.

[Subject index](INDEX.md) · [Previous](authentication-keys.md) · [Continue](multiprocessing-pool-threadpool-class.md) · [Owning module, declaration or section: multiprocessing](multiprocessing-process-based-parallelism.md)
