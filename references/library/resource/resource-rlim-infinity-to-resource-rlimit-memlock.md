# resource: CPU, file, memory and process resource limits

### Resource Limits

You can cap resource consumption through the `setrlimit()` function covered below. Two ceilings govern each resource: one soft and one hard. Whatever the soft limit holds is the value presently applied, and over the course of its run a process may push that value down or up. The soft limit must never climb above the hard limit. As for the hard limit, it can be brought down to any figure at or above the soft limit, yet it cannot be pushed up. (Raising a hard limit is reserved for processes whose effective UID is that of the super-user.)

Exactly which resources may be capped depends on the system. They are documented in the *[getrlimit(2)](https://manpages.debian.org/getrlimit(2))* man page. Those resources enumerated below are honoured whenever the underlying operating system honours them; resources the operating system cannot inspect or govern are left undefined in this module on such platforms.

 resource.RLIM_INFINITY

Constant used to represent the limit for an unlimited resource.

 resource.getrlimit(*resource*)

Hands back a tuple `(soft, hard)` carrying the present soft and hard limits for *resource*. Raises [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) when an invalid resource is named, or `error` when the underlying system call fails in an unexpected way.

 resource.setrlimit(*resource*, *limits*)

Establishes fresh consumption limits for *resource*. The *limits* argument has to be a tuple `(soft, hard)` of two integers spelling out the new limits. Passing `RLIM_INFINITY` as a value lets you ask for a limit that is unlimited.

Raises [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) when an invalid resource is named, when the new soft limit climbs above the hard limit, or when a process attempts to push up its own hard limit. Naming a limit of `RLIM_INFINITY` while the hard or system limit on that resource is itself capped will likewise raise a `ValueError`. Although a process whose effective UID is super-user may ask for any legitimate limit value, unlimited included, a `ValueError` is still raised should the requested limit overshoot the limit the system imposes.

`setrlimit` can additionally raise `error` whenever the underlying system call fails.

VxWorks only supports setting `RLIMIT_NOFILE`.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `resource.setrlimit` with arguments `resource`, `limits`.

 resource.prlimit(*pid*, *resource*[, *limits*])

Rolls `setrlimit()` and `getrlimit()` together into a single function, with the added ability to read and write the resource limits of any process you choose. Should *pid* be 0, the call targets the running process. Here *resource* and *limits* mean what they do in `setrlimit()`, the difference being that *limits* may be omitted.

With *limits* left out, the function returns the *resource* limit belonging to process *pid*. With *limits* supplied, the process's *resource* limit is set and the limit that was in place beforehand is returned.

Raises [`ProcessLookupError`](https://docs.python.org/3.14/library/exceptions.html#ProcessLookupError) when *pid* cannot be located and [`PermissionError`](https://docs.python.org/3.14/library/exceptions.html#PermissionError) when the user lacks `CAP_SYS_RESOURCE` over the process.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `resource.prlimit` with arguments `pid`, `resource`, `limits`.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Linux >= 2.6.36 with glibc >= 2.13.

Added in version 3.4.

The symbols here name resources whose use can be regulated via the `setrlimit()` and `getrlimit()` functions covered below. Each symbol's value is precisely the same constant that C programs employ.

The available resources are listed in the Unix man page for *[getrlimit(2)](https://manpages.debian.org/getrlimit(2))*. Bear in mind that systems do not all share one symbol or one value for a given resource. This module makes no effort to paper over platform differences — any symbol not defined on a platform simply will not be exposed by the module on that platform.

 resource.RLIMIT_CORE

The largest core file, measured in bytes, that the running process is permitted to write. Where a bigger core would be needed to hold the whole process image, this can leave behind only a partial core file.

 resource.RLIMIT_CPU

The ceiling, in seconds, on the processor time a process is allowed to consume. Once that ceiling is passed, the process receives a [`SIGXCPU`](https://docs.python.org/3.14/library/signal.html#signal.SIGXCPU) signal. (Consult the [`signal`](https://docs.python.org/3.14/library/signal.html#module-signal) module documentation for guidance on trapping this signal and doing something worthwhile with it, such as flushing open files out to disk.)

 resource.RLIMIT_FSIZE

The maximum size of a file which the process may create.

 resource.RLIMIT_DATA

The maximum size (in bytes) of the process's heap.

 resource.RLIMIT_STACK

The upper bound, in bytes, on the running process's call stack. In a multi-threaded process this bears solely on the main thread's stack.

 resource.RLIMIT_RSS

The largest resident set size that ought to be granted to the process.

 resource.RLIMIT_NPROC

The maximum number of processes the current process may create.

 resource.RLIMIT_NOFILE

The maximum number of open file descriptors for the current process.

 resource.RLIMIT_OFILE

The BSD name for `RLIMIT_NOFILE`.

 resource.RLIMIT_MEMLOCK

The maximum address space which may be locked in memory.

[Subject index](INDEX.md) · [Previous](resource-error.md) · [Continue](resource-rlimit-vmem-to-resource-rlimit-kqueues.md) · [Owning module, declaration or section: resource](resource-error.md)
