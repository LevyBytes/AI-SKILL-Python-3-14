# -X perf_jit

- `-X perf_jit` turns on support for the Linux `perf` profiler together with DWARF support. With this option supplied, the `perf` profiler can report Python calls using DWARF information. The option exists only on certain platforms and does nothing where the current system lacks support. Its default value is "off". See also `PYTHON_PERF_JIT_SUPPORT` and [Python support for the Linux perf profiler](https://docs.python.org/3.14/howto/perf_profiling.html#perf-profiling).

Added in version 3.13.

[Subject index](INDEX.md) · [Previous source section](x-perf.md) · [Following source section](x-disable-remote-debug.md)
