# multiprocessing: `multiprocessing.Manager()`

### Managers

Managers offer a means of creating data that can be shared among separate processes, even across a network between processes on different machines. A manager object steers a server process that oversees *shared objects*. Other processes get at the shared objects by way of proxies.

 multiprocessing.Manager()

Gives back a started `SyncManager` object usable for sharing objects among processes. The manager object returned corresponds to a spawned child process and carries methods that create shared objects and hand back the matching proxies.

Manager processes get shut down the moment they are garbage collected or their parent process exits. The manager classes live in the `multiprocessing.managers` module:

[Subject index](INDEX.md) · [Previous](multiprocessing-sharedctypes-synchronized.md) · [Continue](multiprocessing-managers-basemanager-class.md) · [Owning module, declaration or section: multiprocessing](multiprocessing-process-based-parallelism.md)
