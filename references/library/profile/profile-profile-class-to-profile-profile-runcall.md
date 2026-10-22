# profile: `profile.Profile`, `enable()`, `disable()`, `create_stats()`, `print_stats()`, `dump_stats()`, `run()`, `runctx()`, `runcall()`

*class *profile.Profile(*timer=None*, *timeunit=0.0*, *subcalls=True*, *builtins=True*)

You typically reach for this class only when you need tighter control over profiling than the `cProfile.run()` function gives you.

Through the *timer* argument you can supply a custom timer that measures how long code takes to run. It has to be a function returning a single number that stands for the current time. When that number is an integer, the *timeunit* supplies a multiplier fixing the length of each time unit. As an example, when the timer reports times measured in thousands of seconds, the time unit would be `.001`.

Using the `Profile` class directly lets you format profile results without writing the profile data out to a file:

```python
import cProfile, pstats, io
from pstats import SortKey
pr = cProfile.Profile()
pr.enable()
# ... do something ...
pr.disable()
s = io.StringIO()
sortby = SortKey.CUMULATIVE
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print(s.getvalue())

```

You can likewise employ the `Profile` class as a context manager (this works only in the `cProfile` module. see [Context Manager Types](https://docs.python.org/3.14/library/stdtypes.html#typecontextmanager)):

```python
import cProfile

with cProfile.Profile() as pr:
    # ... do something ...

    pr.print_stats()

```

Changed in version 3.8: Added context manager support.

 enable()

Start collecting profiling data. Only in `cProfile`.

 disable()

Stop collecting profiling data. Only in `cProfile`.

 create_stats()

Halt the gathering of profiling data and store the results internally as the current profile.

 print_stats(*sort=-1*)

Build a `Stats` object from the current profile and write the results out to stdout.

The *sort* parameter sets the order in which the displayed statistics appear. It takes a single key or a tuple of keys for multi-level sorting, just like `Stats.sort_stats`.

Added in version 3.13: `print_stats()` now accepts a tuple of keys.

 dump_stats(*filename*)

Write the results of the current profile to *filename*.

 run(*cmd*)

Profile the cmd via [`exec()`](https://docs.python.org/3.14/library/functions.html#exec).

 runctx(*cmd*, *globals*, *locals*)

Profile the cmd via [`exec()`](https://docs.python.org/3.14/library/functions.html#exec) with the specified global and local environment.

 runcall(*func*, */*, **args*, ***kwargs*)

Profile `func(*args, **kwargs)`

Bear in mind that profiling happens only if the called command or function actually returns. Should the interpreter be terminated (for example through a [`sys.exit()`](https://docs.python.org/3.14/library/sys.html#sys.exit) call while the called command or function runs), no profiling results will be printed.

[Subject index](INDEX.md) · [Previous](profile-run-to-profile-runctx.md) · [Continue](pstats-stats-class.md) · [Owning module, declaration or section: `profile` and `cProfile` Module Reference](profile-run-to-profile-runctx.md)
