# time: `time.sleep()`

time.sleep(*secs*)

Halt the calling thread's execution for the supplied count of seconds. To request a finer-grained sleep time, the argument may be a floating-point number.

Should a signal interrupt the sleep while its handler raises no exception, the sleep begins again with a freshly computed timeout.

How long the suspension actually lasts may exceed the request by some arbitrary margin, owing to how other activity in the system gets scheduled.

Windows implementation

Under Windows, when *secs* is zero the thread gives up what is left of its time slice to whatever other thread stands ready to run. Where no other thread is ready, the function returns at once and the thread keeps executing. From Windows 10 onward the implementation relies on a [high-resolution timer](https://learn.microsoft.com/windows/win32/api/synchapi/nf-synchapi-createwaitabletimerexw) delivering 100 nanoseconds of resolution. When *secs* is zero, `Sleep(0)` gets used.

Unix implementation

- Use `clock_nanosleep()` if available (resolution: 1 nanosecond);

- Or use `nanosleep()` if available (resolution: 1 nanosecond);

- Or use `select()` (resolution: 1 microsecond).

Note

For a "no-op", reach for [`pass`](https://docs.python.org/3.14/reference/simple_stmts.html#pass) rather than `time.sleep(0)`.

When you want to give up the CPU willingly, pick a real-time [scheduling policy](https://docs.python.org/3.14/library/os.html#os-scheduling-policy) and call [`os.sched_yield()`](https://docs.python.org/3.14/library/os.html#os.sched_yield) instead.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `time.sleep` with argument `secs`.

Changed in version 3.5: The function now sleeps for at least *secs* even should a signal interrupt the sleep, unless the signal handler raises an exception (the reasoning is laid out in [**PEP 475**](https://peps.python.org/pep-0475/)).

Changed in version 3.11: Under Unix, the `clock_nanosleep()` and `nanosleep()` functions are now drawn on when available. Under Windows, a waitable timer is now drawn on.

Changed in version 3.13: Raises an auditing event.

[Subject index](INDEX.md) · [Previous](functions.md) · [Continue](time-strftime.md) · [Owning module, declaration or section: time](time-time-access-and-conversions.md) · [Owning module, declaration or section: Functions](time-asctime-to-time-ctime.md)
