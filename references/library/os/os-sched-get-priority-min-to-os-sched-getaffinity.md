# os: Scheduler priorities, parameters and CPU affinity

os.sched_get_priority_min(*policy*)

Get the minimum priority value for *policy*. Here *policy* names one of the scheduling-policy constants listed earlier.

 os.sched_get_priority_max(*policy*)

Get the maximum priority value for *policy*. Here *policy* names one of the scheduling-policy constants listed earlier.

 os.sched_setscheduler(*pid*, *policy*, *param*, */*)

Set the scheduling policy for the process carrying PID *pid*. A *pid* of 0 stands for the calling process. Here *policy* names one of the scheduling-policy constants listed earlier. *param* is a `sched_param` instance.

 os.sched_getscheduler(*pid*, */*)

Return the scheduling policy for the process carrying PID *pid*. A *pid* of 0 stands for the calling process. The result is one of the scheduling-policy constants listed earlier.

 os.sched_setparam(*pid*, *param*, */*)

Set the scheduling parameters for the process carrying PID *pid*. A *pid* of 0 stands for the calling process. *param* is a `sched_param` instance.

 os.sched_getparam(*pid*, */*)

Return the scheduling parameters as a `sched_param` instance for the process carrying PID *pid*. A *pid* of 0 stands for the calling process.

 os.sched_rr_get_interval(*pid*, */*)

Return the round-robin quantum in seconds for the process carrying PID *pid*. A *pid* of 0 stands for the calling process.

 os.sched_yield()

Voluntarily give up the CPU. See *[sched_yield(2)](https://manpages.debian.org/sched_yield(2))* for details.

 os.sched_setaffinity(*pid*, *mask*, */*)

Confine the process carrying PID *pid* (or the current process when zero) to a set of CPUs. *mask* is an iterable of integers that names the set of CPUs the process should be confined to.

 os.sched_getaffinity(*pid*, */*)

Return the set of CPUs that the process carrying PID *pid* is confined to.

When *pid* is zero, return the set of CPUs that the calling thread of the current process is confined to.

See also the `process_cpu_count()` function.

[Subject index](INDEX.md) · [Previous](os-sched-param-class.md) · [Continue](os-confstr-to-os-extsep.md) · [Owning module, declaration or section: os](os-error-to-os-name.md) · [Owning module, declaration or section: Interface to the scheduler](os-sched-other-to-os-sched-reset-on-fork.md)
