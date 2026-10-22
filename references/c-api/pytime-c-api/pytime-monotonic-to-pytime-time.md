# Clock Functions

### Clock Functions

Each function below accepts a pointer to a PyTime_t and stores into it the reading of a given clock. Refer to the corresponding Python function's documentation for the specifics of each clock.

A return of `0` signals success, while `-1` (accompanied by a set exception) signals failure.

When an integer overflow occurs, the [`PyExc_OverflowError`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyExc_OverflowError) exception is raised and `*result` is clamped within the `[PyTime_MIN; PyTime_MAX]` range. (On today's machines, such overflows usually stem from a system clock that is configured incorrectly.)

Like every other C API (barring explicit exceptions), these functions require an [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state) at the call site.

 int PyTime_Monotonic(PyTime_t *result)

Read the monotonic clock. See [`time.monotonic()`](https://docs.python.org/3.14/library/time.html#time.monotonic) for important details on this clock.

 int PyTime_PerfCounter(PyTime_t *result)

Read the performance counter. See [`time.perf_counter()`](https://docs.python.org/3.14/library/time.html#time.perf_counter) for important details on this clock.

 int PyTime_Time(PyTime_t *result)

Read the “wall clock” time. See [`time.time()`](https://docs.python.org/3.14/library/time.html#time.time) for details important on this clock.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pytime-c-api.md) · [Previous source contract](pytime-t-to-pytime-max.md) · [Following source contract](pytime-monotonicraw-to-pytime-timeraw.md)
