# timeit / Python Interface: `timeit.Timer`, `timeit()`, `autorange()`, `repeat()`, `print_exc()`

*class *timeit.Timer(*stmt='pass'*, *setup='pass'*, *timer=&lt;timer function&gt;*, *globals=None*)

Class for timing execution speed of small code snippets.

The constructor accepts a statement to be timed, a further statement serving for setup, and a timer function. Each statement defaults to `'pass'`; the timer function depends on the platform (consult the module doc string). *stmt* and *setup* are also permitted to hold several statements split by `;` or newlines, provided they carry no multi-line string literals. By default the statement runs inside timeit's namespace; you can steer that behavior by handing a namespace to *globals*.

To gauge the execution time of the first statement, reach for the `timeit()` method. The `repeat()` and `autorange()` methods are convenience methods that invoke `timeit()` several times.

The execution time of *setup* is kept out of the overall timed execution run.

The *stmt* and *setup* parameters can additionally accept objects callable with no arguments. Doing so embeds calls to them within a timer function that `timeit()` then runs. Note that the timing overhead grows a touch in that case, owing to the extra function calls.

Changed in version 3.5: The optional *globals* parameter was added.

 timeit(*number=1000000*)

Time *number* executions of the main statement. This runs the setup statement a single time, then hands back how long it takes to run the main statement a number of times. The default timer reports seconds as a float. The argument states how many loop iterations to perform, with one million as the fallback. Whichever main statement, setup statement and timer function apply are all supplied by way of the constructor.

Note

By default, `timeit()` switches off [garbage collection](https://docs.python.org/3.14/glossary.html#term-garbage-collection) for the duration of the timing. The upside of this approach is that it renders separate timings more comparable. The downside is that GC may form an important part of the performance of the function under measurement. Where that holds, GC can be switched back on as the opening statement in the *setup* string. For instance:

```python
timeit.Timer('for i in range(10): oct(i)', 'gc.enable()').timeit()

```

 autorange(*callback=None*)

Automatically determine how many times to call `timeit()`.

This convenience function invokes `timeit()` again and again until the cumulative time >= 0.2 second, then reports back the pair it settled on (the loop count together with how long those loops ran). Drawing on the rising values 1, 2, 5, 10, 20, 50, … in turn, it keeps calling `timeit()` until the elapsed time hits at least 0.2 seconds.

Where *callback* is supplied and is not `None`, it gets invoked after each trial with two arguments: `callback(number, time_taken)`.

Added in version 3.6.

 repeat(*repeat=5*, *number=1000000*)

Call `timeit()` a few times.

This convenience function invokes `timeit()` over and over, handing back a list of results. The first argument fixes how many times `timeit()` gets called. The second argument fixes the *number* argument for `timeit()`.

Note

There's a pull toward computing mean and standard deviation off the result vector and reporting those. That, however, is of little value. Typically, the smallest value sets a lower bound on how quickly your machine can run the given code snippet; the larger values in the result vector usually stem not from any variability in Python's speed, but from other processes meddling with your timing accuracy. So the [`min()`](https://docs.python.org/3.14/library/functions.html#min) of the result is likely the sole number worth your attention. Beyond that, take in the whole vector and lean on common sense in place of statistics.

Changed in version 3.7: For *repeat*, the default went up from 3 to 5.

 print_exc(*file=None*)

Helper to print a traceback from the timed code.

Typical use:

```python
t = Timer(...)       # outside the try/except
try:
    t.timeit(...)    # or t.repeat(...)
except Exception:
    t.print_exc()

```

The edge over the standard traceback is that source lines within the compiled template get shown. The optional *file* argument steers where the traceback goes; it defaults to [`sys.stderr`](https://docs.python.org/3.14/library/sys.html#sys.stderr).

[Subject index](INDEX.md) · [Previous](timeit-timeit-to-timeit-default-timer.md) · [Continue](command-line-interface.md) · [Owning module, declaration or section: timeit](timeit-measure-execution-time-of-small-code-snippets.md) · [Owning module, declaration or section: Python Interface](timeit-timeit-to-timeit-default-timer.md)
