# Python 3.9.0 alpha 5 / library / multiprocessing

[bpo-39360](https://bugs.python.org/issue?@action=redirect&bpo=39360): All workers are now made to exit when a `multiprocessing.Pool` is finalized implicitly through multiprocessing's module finalization handlers. The earlier deadlock — triggered whenever the Pool was not cleanly finalized through the context manager or through a `multiprocessing.Pool.terminate` call — is thereby resolved. Batuhan Taskaya and Pablo Galindo wrote the patch.

[bpo-39850](https://bugs.python.org/issue?@action=redirect&bpo=39850): Where the running platform offers abstract sockets, [`multiprocessing`](https://docs.python.org/3.14/library/multiprocessing.html#module-multiprocessing) now accepts abstract socket addresses. Whenever addresses are generated arbitrarily (for instance during the default construction of [`multiprocessing.connection.Listener`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.connection.Listener) objects), abstract sockets take precedence so as to sidestep the scenario where a temporary-file-generated address exceeds the size allowed for an AF_UNIX socket address. Pablo Galindo wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
