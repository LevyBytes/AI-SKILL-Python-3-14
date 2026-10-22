# threading: `threading.BoundedSemaphore`

*class *threading.BoundedSemaphore(*value=1*)

Class that provides bounded semaphore objects. A bounded semaphore confirms its present value never rises beyond its starting value. Should it do so, a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised. Most of the time semaphores serve to guard resources of limited capacity. Releasing the semaphore too often signals a bug. When omitted, *value* defaults to 1.

Changed in version 3.3: was previously a factory function, and is now a class.

[Subject index](INDEX.md) · [Previous](threading-semaphore-acquire-to-threading-semaphore-release.md) · [Continue](semaphore-example.md) · [Owning module, declaration or section: threading](threading-thread-based-parallelism.md) · [Owning module, declaration or section: Semaphore objects](threading-semaphore-class.md)
