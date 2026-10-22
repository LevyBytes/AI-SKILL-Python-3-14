# Raw Clock Functions

### Raw Clock Functions

These resemble the clock functions, except they leave no exception set when an error occurs and they impose no requirement that the caller hold an [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state).

When they succeed, a value of `0` is returned.

Should they fail, `*result` is set to `0` and `-1` is returned, *without* any exception being set. Determining what went wrong requires that you [attach](https://docs.python.org/3.14/glossary.html#term-attached-thread-state) a [thread state](https://docs.python.org/3.14/glossary.html#term-thread-state) and invoke the ordinary (non-`Raw`) variant. Keep in mind the ordinary function may complete successfully even though the `Raw` form did not.

 int PyTime_MonotonicRaw(PyTime_t *result)

Comparable to `PyTime_Monotonic()`, except no exception is set on error and no [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state) is required.

 int PyTime_PerfCounterRaw(PyTime_t *result)

Comparable to `PyTime_PerfCounter()`, except no exception is set on error and no [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state) is required.

 int PyTime_TimeRaw(PyTime_t *result)

Comparable to `PyTime_Time()`, except no exception is set on error and no [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state) is required.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pytime-c-api.md) · [Previous source contract](pytime-monotonic-to-pytime-time.md) · [Following source contract](pytime-assecondsdouble.md)
