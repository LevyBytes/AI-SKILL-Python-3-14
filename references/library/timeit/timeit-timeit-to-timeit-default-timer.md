# timeit: `timeit.timeit()`, `timeit.repeat()`, `timeit.default_timer()`

### Python Interface

The module defines three convenience functions and a public class:

 timeit.timeit(*stmt='pass'*, *setup='pass'*, *timer=&lt;default timer&gt;*, *number=1000000*, *globals=None*)

Build a `Timer` instance from the given statement, *setup* code and *timer* function, then run its `timeit()` method for *number* executions. The optional *globals* argument names a namespace within which the code is to run.

Changed in version 3.5: The optional *globals* parameter was added.

 timeit.repeat(*stmt='pass'*, *setup='pass'*, *timer=&lt;default timer&gt;*, *repeat=5*, *number=1000000*, *globals=None*)

Build a `Timer` instance from the given statement, *setup* code and *timer* function, then run its `repeat()` method for the given *repeat* count and *number* executions. The optional *globals* argument names a namespace within which the code is to run.

Changed in version 3.5: The optional *globals* parameter was added.

Changed in version 3.7: The default for *repeat* was raised from 3 to 5.

 timeit.default_timer()

The default timer, forever `time.perf_counter()`, hands back float seconds. As an alternative, `time.perf_counter_ns` hands back integer nanoseconds.

Changed in version 3.3: [`time.perf_counter()`](https://docs.python.org/3.14/library/time.html#time.perf_counter) is now the default timer.

[Subject index](INDEX.md) · [Previous](basic-examples.md) · [Continue](timeit-timer-class-to-timeit-timer-print-exc.md) · [Owning module, declaration or section: timeit](timeit-measure-execution-time-of-small-code-snippets.md)
