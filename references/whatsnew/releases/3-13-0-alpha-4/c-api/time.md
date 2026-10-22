# Python 3.13.0 alpha 4 / c api / time

[gh-110850](https://github.com/python/cpython/issues/110850): The PyTime C API was added, comprising:

  - The [`PyTime_t`](https://docs.python.org/3.14/c-api/time.html#c.PyTime_t) type.

  - The [`PyTime_MIN`](https://docs.python.org/3.14/c-api/time.html#c.PyTime_MIN) and [`PyTime_MAX`](https://docs.python.org/3.14/c-api/time.html#c.PyTime_MAX) constants.

  - The [`PyTime_AsSecondsDouble()`](https://docs.python.org/3.14/c-api/time.html#c.PyTime_AsSecondsDouble), [`PyTime_Monotonic()`](https://docs.python.org/3.14/c-api/time.html#c.PyTime_Monotonic), [`PyTime_PerfCounter()`](https://docs.python.org/3.14/c-api/time.html#c.PyTime_PerfCounter), and [`PyTime_Time()`](https://docs.python.org/3.14/c-api/time.html#c.PyTime_Time) functions.

Victor Stinner authored this patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
