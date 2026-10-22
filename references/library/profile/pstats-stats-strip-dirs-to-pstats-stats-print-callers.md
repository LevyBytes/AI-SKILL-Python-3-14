# profile: `strip_dirs()`, `add()`, `dump_stats()`, `sort_stats()`, `reverse_order()`, `print_stats()`, `print_callers()`

strip_dirs()

This `Stats` class method strips every leading path component off file names. It is quite handy for shrinking the printout so it fits within (roughly) 80 columns. The method changes the object, and the stripped information is gone for good. Once a strip operation is done, the object is treated as having its entries in a "random" order, just as right after object initialization and loading. Should `strip_dirs()` make two function names indistinguishable (they sit on the same line of the same filename and share the same function name), the statistics for those two entries get rolled into one entry.

 add(**filenames*)

This `Stats` class method folds additional profiling information into the current profiling object. Its arguments should point to filenames produced by the matching version of `profile.run()` or `cProfile.run()`. Statistics for functions named identically (re: file, line, name) are automatically merged into single function statistics.

 dump_stats(*filename*)

Write the data held by the `Stats` object out to a file called *filename*. That file gets created when it is absent and overwritten when it is already present. This matches the identically named method on the `profile.Profile` and `cProfile.Profile` classes.

 sort_stats(**keys*)

This method changes the `Stats` object by ordering it according to the criteria you supply. The argument can be either a string or a SortKey enum that names the basis of a sort (example: `'time'`, `'name'`, `SortKey.TIME` or `SortKey.NAME`). The SortKey enums argument has the edge over the string argument in being more robust and less prone to error.

When you provide more than one key, the later keys act as secondary criteria wherever every earlier-selected key compares equal. For instance, `sort_stats(SortKey.NAME, SortKey.FILE)` orders all the entries by their function name and breaks any ties (matching function names) by ordering on file name.

With the string argument, you may abbreviate any key name, provided the abbreviation stays unambiguous.

The following are the valid string and SortKey:

| Valid String Arg | Valid enum Arg | Meaning |
| --- | --- | --- |
| `'calls'` | SortKey.CALLS | call count |
| `'cumulative'` | SortKey.CUMULATIVE | cumulative time |
| `'cumtime'` | N/A | cumulative time |
| `'file'` | N/A | file name |
| `'filename'` | SortKey.FILENAME | file name |
| `'module'` | N/A | file name |
| `'ncalls'` | N/A | call count |
| `'pcalls'` | SortKey.PCALLS | primitive call count |
| `'line'` | SortKey.LINE | line number |
| `'name'` | SortKey.NAME | function name |
| `'nfl'` | SortKey.NFL | name/file/line |
| `'stdname'` | SortKey.STDNAME | standard name |
| `'time'` | SortKey.TIME | internal time |
| `'tottime'` | N/A | internal time |

Note that every sort on statistics runs in descending order (putting the most time-consuming items first), whereas searches by name, file, and line number run in ascending (alphabetical) order. The fine distinction between `SortKey.NFL` and `SortKey.STDNAME` is that the standard name sorts on the name as printed, so the embedded line numbers end up compared in a peculiar way. For instance, lines 3, 20, and 40 would (when the file names matched) come out in the string order 20, 3 and 40. `SortKey.NFL`, by contrast, compares the line numbers numerically. In fact, `sort_stats(SortKey.NFL)` is the same as `sort_stats(SortKey.NAME, SortKey.FILENAME, SortKey.LINE)`.

To stay backward compatible, the numeric arguments `-1`, `0`, `1`, and `2` are still accepted. They map to `'stdname'`, `'calls'`, `'time'`, and `'cumulative'` in turn. Once you use this older numeric form, just one sort key (the numeric one) takes effect, and any further arguments are quietly dropped.

Added in version 3.7: Added the SortKey enum.

 reverse_order()

This `Stats` class method flips the ordering of the basic list held within the object. Keep in mind that by default the choice of ascending versus descending order is made correctly from the sort key you selected.

 print_stats(**restrictions*)

This `Stats` class method prints out a report of the form described in the `profile.run()` definition.

The printing order follows the last `sort_stats()` operation performed on the object (subject to the caveats noted in `add()` and `strip_dirs()`).

Any arguments supplied (if any) can serve to pare the list down to the significant entries. To begin with, the list is taken as the full set of profiled functions. A restriction is either an integer (picking how many lines to keep), or a decimal fraction from 0.0 up to and including 1.0 (picking a percentage of the lines), or a string treated as a regular expression (matched against the printed standard name). When several restrictions are given, they are applied one after another. For example:

```python
print_stats(.1, 'foo:')

```

would first cut the printing down to the first 10% of the list, and then print only those functions belonging to filename `.*foo:`. In contrast, the command:

```python
print_stats('foo:', .1)

```

would narrow the list to every function whose file name is `.*foo:`, and then go on to print only the first 10% of them.

 print_callers(**restrictions*)

This `Stats` class method prints a list of every function that called each function in the profiled database. The ordering matches what `print_stats()` produces, and the meaning of the restricting argument is the same as well. Each caller gets its own line. The exact format varies a little depending on which profiler made the stats:

- With `profile`, a number appears in parentheses after each caller to indicate how many times that particular call happened. As a convenience, a second number, without parentheses, repeats on the right the cumulative time spent in the function.

- With `cProfile`, three numbers come before each caller: how many times that particular call occurred, along with the total and cumulative times the current function used up while that particular caller was invoking it.

[Subject index](INDEX.md) · [Previous](pstats-stats-class.md) · [Continue](pstats-stats-print-callees-to-pstats-stats-get-stats-profile.md) · [Owning module, declaration or section: pstats.Stats](pstats-stats-class.md) · [Owning module, declaration or section: The `Stats` Class](pstats-stats-class.md)
