# Python 3.11.0 alpha 1 / library / time

[bpo-21302](https://bugs.python.org/issue?@action=redirect&bpo=21302): Across Unix platforms, whenever `clock_nanosleep()` is missing yet `nanosleep()` exists, [`time.sleep()`](https://docs.python.org/3.14/library/time.html#time.sleep) will fall back on the `nanosleep()` call. Sleeping with nanosecond granularity becomes possible through `nanosleep()`.

[bpo-21302](https://bugs.python.org/issue?@action=redirect&bpo=21302): Under Windows, [`time.sleep()`](https://docs.python.org/3.14/library/time.html#time.sleep) has switched to a waitable timer whose granularity reaches 100 nanoseconds (10-7 seconds). The earlier behavior offered only millisecond-level granularity, 1 millisecond (10-3 seconds). Benjamin Szőke together with Victor Stinner authored this patch.

[bpo-21302](https://bugs.python.org/issue?@action=redirect&bpo=21302): On Unix platforms, [`time.sleep()`](https://docs.python.org/3.14/library/time.html#time.sleep) now relies on the `clock_nanosleep()` call whenever it exists, letting a sleep interval be expressed down to nanosecond granularity.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
