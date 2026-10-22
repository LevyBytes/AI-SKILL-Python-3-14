# os: `os.SCHED_OTHER`, `os.SCHED_BATCH`, `os.SCHED_DEADLINE`, `os.SCHED_IDLE`, `os.SCHED_NORMAL`, `os.SCHED_SPORADIC`, `os.SCHED_FIFO`, `os.SCHED_RR`, `os.SCHED_RESET_ON_FORK`

### Interface to the scheduler

These functions govern how the operating system hands a process its CPU time. They exist on only certain Unix platforms. For fuller detail, look through your Unix manpages.

Added in version 3.3.

The scheduling policies below are exposed whenever the operating system supports them.

 os.SCHED_OTHER

The default scheduling policy.

 os.SCHED_BATCH

Scheduling policy for CPU-intensive processes that aims to keep the rest of the computer interactive.

 os.SCHED_DEADLINE

Scheduling policy for tasks bound by deadline constraints.

Added in version 3.14.

 os.SCHED_IDLE

Scheduling policy for background tasks of extremely low priority.

 os.SCHED_NORMAL

Alias for `SCHED_OTHER`.

Added in version 3.14.

 os.SCHED_SPORADIC

Scheduling policy for sporadic server programs.

 os.SCHED_FIFO

A First In First Out scheduling policy.

 os.SCHED_RR

A round-robin scheduling policy.

 os.SCHED_RESET_ON_FORK

You can OR this flag with any other scheduling policy. Once a process carrying this flag forks, the scheduling policy and priority of its child reset to the default.

[Subject index](INDEX.md) · [Previous](os-wifexited-to-os-wtermsig.md) · [Continue](os-sched-param-class.md) · [Owning module, declaration or section: os](os-error-to-os-name.md)
