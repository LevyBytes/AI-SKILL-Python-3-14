# timeit — Command-Line Interface

### Command-Line Interface

Invoked as a program from the command line, the form below applies:

```python
python -m timeit [-n N] [-r N] [-u U] [-s S] [-p] [-v] [-h] [statement ...]

```

Where the following options are understood:

 -n N, --number=N

how many times to execute ‘statement’

 -r N, --repeat=N

how many times to repeat the timer (default 5)

 -s S, --setup=S

statement to be executed once initially (default `pass`)

 -p, --process

gauge process time in place of wallclock time, drawing on [`time.process_time()`](https://docs.python.org/3.14/library/time.html#time.process_time) rather than the standard choice, [`time.perf_counter()`](https://docs.python.org/3.14/library/time.html#time.perf_counter)

Added in version 3.3.

 -u, --unit=U

specify a time unit for timer output; can select `nsec`, `usec`, `msec`, or `sec`

Added in version 3.5.

 -v, --verbose

print raw timing results; repeat for more digits precision

 -h, --help

print a short usage message and exit

You can supply a multi-line statement by giving each line as its own statement argument; indented lines are achievable by wrapping an argument in quotes and prefixing leading spaces. Several `-s` options get treated the same way.

Where `-n` is left out, a fitting number of loops gets computed by working through mounting numbers from the sequence 1, 2, 5, 10, 20, 50, … until the total time reaches at least 0.2 seconds.

`default_timer()` measurements are subject to influence from other programs running on the same machine, so when accurate timing matters the soundest move is to repeat the timing a handful of times and keep the best time. The `-r` option suits this; the default of 5 repetitions is most likely sufficient in the majority of cases. You can reach for [`time.process_time()`](https://docs.python.org/3.14/library/time.html#time.process_time) to gauge CPU time.

Note

A certain baseline overhead goes hand in hand with running a pass statement. The code here makes no attempt to mask it, yet you ought to stay mindful of it. You can gauge that baseline overhead by running the program without arguments, and it might vary across Python versions.

[Subject index](INDEX.md) · [Previous](timeit-timer-class-to-timeit-timer-print-exc.md) · [Continue](examples-section-introduction-and-initial-examples.md) · [Owning module, declaration or section: timeit](timeit-measure-execution-time-of-small-code-snippets.md)
