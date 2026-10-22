# Python 3.12.0 beta 1 / c api / perfmaps

[gh-103295](https://github.com/python/cpython/issues/103295): Brought in [`PyUnstable_WritePerfMapEntry()`](https://docs.python.org/3.14/c-api/perfmaps.html#c.PyUnstable_WritePerfMapEntry), [`PyUnstable_PerfMapState_Init()`](https://docs.python.org/3.14/c-api/perfmaps.html#c.PyUnstable_PerfMapState_Init) and [`PyUnstable_PerfMapState_Fini()`](https://docs.python.org/3.14/c-api/perfmaps.html#c.PyUnstable_PerfMapState_Fini). With these, extension modules — JIT compilers above all — can append to perf-map files in a thread-safe way. The [Python support for the Linux perf profiler](https://docs.python.org/3.14/howto/perf_profiling.html) leans on these same APIs to record entries inside the perf-map file.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
