# sys.activate_stack_trampoline

sys.activate_stack_trampoline(*backend*, */*)

Turns on the stack profiler trampoline *backend*. The sole backend that is supported is `"perf"`.

You can’t turn on stack trampolines while the JIT is running.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Linux.

Added in version 3.12.

See also

- [Python support for the Linux perf profiler](https://docs.python.org/3.14/howto/perf_profiling.html#perf-profiling)

- [https://perf.wiki.kernel.org](https://perf.wiki.kernel.org)

[API family](INDEX.md) · [sys context index](../INDEX.md).
