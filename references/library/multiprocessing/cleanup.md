# multiprocessing - Cleanup

#### Cleanup

A proxy object relies on a weakref callback so that, upon being garbage collected, it removes its own registration from the manager that owns its referent.

A shared object gets deleted from the manager process once no proxies refer to it any longer.

[Subject index](INDEX.md) · [Previous](manager-proxy-contract.md) · [Continue](multiprocessing-pool-pool-class.md) · [Owning module, declaration or section: multiprocessing](multiprocessing-process-based-parallelism.md)
