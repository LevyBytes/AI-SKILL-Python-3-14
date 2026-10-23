# resource - Resource Usage

### Resource Usage

The functions below let you pull back resource usage figures:

 resource.getrusage(*who*)

This function yields an object setting out the resources used up by either the running process or its children, picked out via the *who* parameter. That *who* parameter ought to be given as one of the `RUSAGE_*` constants covered below.

A simple example:

```python
from resource import *
import time

# a non CPU-bound task
time.sleep(3)
print(getrusage(RUSAGE_SELF))

# a CPU-bound task
for i in range(10 ** 8):
   _ = 1 + 1
print(getrusage(RUSAGE_SELF))

```

Every field of the returned value spells out how one specific system resource got used, for instance the time spent running in user mode or the count of times the process was paged out of main memory. A handful of values hinge on the clock tick interval, such as the quantity of memory the process is occupying.

To preserve backward compatibility, the returned value can also be reached as a tuple of 16 elements.

Within the returned value the `ru_utime` and `ru_stime` fields are floating-point values giving, respectively, the time spent running in user mode and the time spent running in system mode. Every other value is an integer. Turn to the *[getrusage(2)](https://manpages.debian.org/getrusage(2))* man page for thorough notes on these values. What follows is a short rundown:

| Index | Field | Resource |
| --- | --- | --- |
| `0` | `ru_utime` | time in user mode (float seconds) |
| `1` | `ru_stime` | time in system mode (float seconds) |
| `2` | `ru_maxrss` | maximum resident set size |
| `3` | `ru_ixrss` | shared memory size |
| `4` | `ru_idrss` | unshared memory size |
| `5` | `ru_isrss` | unshared stack size |
| `6` | `ru_minflt` | page faults not requiring I/O |
| `7` | `ru_majflt` | page faults requiring I/O |
| `8` | `ru_nswap` | number of swap outs |
| `9` | `ru_inblock` | block input operations |
| `10` | `ru_oublock` | block output operations |
| `11` | `ru_msgsnd` | messages sent |
| `12` | `ru_msgrcv` | messages received |
| `13` | `ru_nsignals` | signals received |
| `14` | `ru_nvcsw` | voluntary context switches |
| `15` | `ru_nivcsw` | involuntary context switches |

Should an invalid *who* parameter be supplied, this function raises a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError). On rare occasions it may also raise the `error` exception.

 resource.getpagesize()

Hands back the byte count of a system page. (That figure need not coincide with the hardware page size.)

The `RUSAGE_*` symbols below get handed to the `getrusage()` function to indicate which processes the information should cover.

 resource.RUSAGE_SELF

Hand to `getrusage()` to ask for the resources used by the calling process, which amounts to the combined resources used by every thread inside the process.

 resource.RUSAGE_CHILDREN

Hand to `getrusage()` to ask for the resources used by child processes of the calling process that have terminated and been waited for.

 resource.RUSAGE_BOTH

Hand to `getrusage()` to ask for the resources used by the current process and its child processes together. It may not be present on every system.

 resource.RUSAGE_THREAD

Hand to `getrusage()` to ask for the resources used by the current thread. It may not be present on every system.

Added in version 3.2.

[Subject index](INDEX.md) · [Previous](resource-rlimit-vmem-to-resource-rlimit-kqueues.md) · [Continue](../rlcompleter/rlcompleter-completer-class.md) · [Owning module, declaration or section: resource](resource-error.md)
