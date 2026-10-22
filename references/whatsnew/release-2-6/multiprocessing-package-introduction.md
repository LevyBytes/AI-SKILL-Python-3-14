# Python 2.6 changes: Multiprocessing package introduction and worker example

### PEP 371: The `multiprocessing` Package

With the new [`multiprocessing`](https://docs.python.org/3.14/library/multiprocessing.html#module-multiprocessing) package, Python programs can spin up new processes that carry out a computation and hand a result back to the parent. Parent and child processes are able to talk to each other through queues and pipes, coordinate their work with locks and semaphores, and share basic arrays of data.

[Subject index](INDEX.md) · [Previous source section](pep-370-per-user-site-packages-directory.md) · [Release/subject declaration](python-3-0.md) · [Following release/subject continuation](pep-371-the-multiprocessing-package-factorial-and-factorial.md)
