# resource: Address-space, queue, priority and platform resource limits

resource.RLIMIT_VMEM

The biggest span of mapped memory the process is allowed to take up. Typically just an alias of `RLIMIT_AS`.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Solaris, FreeBSD, NetBSD.

 resource.RLIMIT_AS

The largest stretch of address space, in bytes, the process is allowed to claim.

 resource.RLIMIT_MSGQUEUE

The number of bytes that can be allocated for POSIX message queues.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Linux >= 2.6.8.

Added in version 3.4.

 resource.RLIMIT_NICE

The ceiling for the process's nice level (calculated as 20 - rlim_cur).

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Linux >= 2.6.12.

Added in version 3.4.

 resource.RLIMIT_RTPRIO

The ceiling of the real-time priority.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Linux >= 2.6.12.

Added in version 3.4.

 resource.RLIMIT_RTTIME

The cap, expressed in microseconds, on how much CPU time a process may run under real-time scheduling before it issues a blocking syscall.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Linux >= 2.6.25.

Added in version 3.4.

 resource.RLIMIT_SIGPENDING

The number of signals which the process may queue.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Linux >= 2.6.8.

Added in version 3.4.

 resource.RLIMIT_SBSIZE

The ceiling, in bytes, on this user's socket buffer consumption. It thereby caps how much network memory — and by extension how many mbufs — the user can keep at any given moment.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): FreeBSD, NetBSD.

Added in version 3.4.

 resource.RLIMIT_SWAP

The upper bound, in bytes, on swap space that the combined processes of this user id may reserve or consume. The limit takes effect only when bit 1 of the vm.overcommit sysctl is turned on. For a full account of that sysctl, refer to [tuning(7)](https://man.freebsd.org/cgi/man.cgi?query=tuning&sektion=7).

[Availability](https://docs.python.org/3.14/library/intro.html#availability): FreeBSD >= 8.

Added in version 3.4.

 resource.RLIMIT_NPTS

The maximum number of pseudo-terminals created by this user id.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): FreeBSD >= 8.

Added in version 3.4.

 resource.RLIMIT_KQUEUES

The maximum number of kqueues this user id is allowed to create.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): FreeBSD >= 11.

Added in version 3.10.

[Subject index](INDEX.md) · [Previous](resource-rlim-infinity-to-resource-rlimit-memlock.md) · [Continue](resource-getrusage-to-resource-rusage-thread.md) · [Owning module, declaration or section: resource](resource-error.md) · [Owning module, declaration or section: Resource Limits](resource-rlim-infinity-to-resource-rlimit-memlock.md)
