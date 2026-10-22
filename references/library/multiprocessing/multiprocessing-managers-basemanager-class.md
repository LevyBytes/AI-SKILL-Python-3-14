# multiprocessing: `multiprocessing.managers.BaseManager`

*class *multiprocessing.managers.BaseManager(*address=None*, *authkey=None*, *serializer='pickle'*, *ctx=None*, ***, *shutdown_timeout=1.0*)

Create a BaseManager object.

After it exists, you should call `start()` or `get_server().serve_forever()` to make certain the manager object points to a started manager process.

*address* is the address on which the manager process waits for incoming connections. When *address* is `None`, an arbitrary one gets picked.

[Subject index](INDEX.md) · [Previous](multiprocessing-manager.md) · [Owning module, declaration or section: multiprocessing](multiprocessing-process-based-parallelism.md) · [Owning module, declaration or section: Managers](multiprocessing-manager.md) · [Required continuation of the source contract](manager-start-and-type-registration.md)
