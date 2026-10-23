# multiprocessing - Global start method

### Global start method

Python offers several mechanisms for creating and initializing a process. The global start method establishes the default mechanism for process creation.

A number of multiprocessing functions and methods that may likewise create certain objects will silently set the global start method to the system's default whenever it has not already been set. The global start method can only be set once. If you want a start method other than the system default, you must deliberately set the global start method ahead of calling any such functions or methods, or building any such objects.

[Subject index](INDEX.md) · [Previous](reference.md) · [Continue](multiprocessing-process-class.md) · [Owning module, declaration or section: multiprocessing](multiprocessing-process-based-parallelism.md)
