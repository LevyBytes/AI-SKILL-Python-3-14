# Instant User's Manual — Contract: -s <sort_order>

-s <sort_order>

Names one of the `sort_stats()` sort values to order the output by. This takes effect only when `-o` is absent.

 -m &lt;module&gt;

Indicates that a module is under profiling instead of a script.

Added in version 3.7: Added the `-m` option to `cProfile`.

Added in version 3.8: Added the `-m` option to `profile`.

The `Stats` class of the `pstats` module offers an assortment of methods for working with and printing the data stored in a profile results file:

```python
import pstats
from pstats import SortKey
p = pstats.Stats('restats')
p.strip_dirs().sort_stats(-1).print_stats()

```

The `strip_dirs()` method stripped the superfluous path off every module name. The `sort_stats()` method ordered all the entries by the standard module/line/name string that is printed. The `print_stats()` method printed every statistic. You might give the following sort calls a try:

```python
p.sort_stats(SortKey.NAME)
p.print_stats()

```

The first call actually orders the list by function name, while the second prints out the statistics. Here are a few interesting calls worth experimenting with:

```python
p.sort_stats(SortKey.CUMULATIVE).print_stats(10)

```

This orders the profile by the cumulative time in a function and then prints only the ten most significant lines. When you want to grasp which algorithms are eating the time, the line above is the one to reach for.

If instead you wanted to see which functions were looping heavily and consuming a lot of time, you would do:

```python
p.sort_stats(SortKey.TIME).print_stats(10)

```

to order by the time spent inside each function, and then print the statistics for the top ten functions.

You could also try:

```python
p.sort_stats(SortKey.FILENAME).print_stats('__init__')

```

This orders all the statistics by file name and then prints statistics only for the class init methods (since they are written with `__init__` in them). As one last example, you might try:

```python
p.sort_stats(SortKey.TIME, SortKey.CUMULATIVE).print_stats(.5, 'init')

```

Here the statistics are ordered using time as the primary key and cumulative time as the secondary key, after which a slice of them is printed. Precisely, the list is first pared back to 50% (re: `.5`) of how big it started, then only lines that contain `init` survive, and that sub-sub-list gets printed.

If you were curious about which functions called the functions above, you could now (`p` is still sorted by the most recent criteria) do:

```python
p.print_callers(.5, 'init')

```

and you would obtain a list of callers for each of the functions listed.

If you want more capability, you will have to read the manual, or guess what the functions below do:

```python
p.print_callees()
p.add('restats')

```

When run as a script, the `pstats` module acts as a statistics browser that reads and inspects profile dumps. It provides a simple line-oriented interface (built with [`cmd`](https://docs.python.org/3.14/library/cmd.html#module-cmd)) together with interactive help.

[Subject index](INDEX.md) · [Previous](profiler-quickstart-overview.md) · [Continue](profile-run-to-profile-runctx.md) · [Owning module, declaration or section: Instant User's Manual](profiler-quickstart-overview.md)
