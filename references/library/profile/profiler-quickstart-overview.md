# Instant User's Manual - Section introduction and initial examples

### Instant User's Manual

This section is here for users who "don't want to read the manual." It gives a very short overview and lets a user quickly profile an existing application.

To profile a function that takes a single argument, you can do:

```python
import cProfile
import re
cProfile.run('re.compile("foo|bar")')

```

(Use `profile` instead of `cProfile` if the latter is not available on your system.)

Running that would execute [`re.compile()`](https://docs.python.org/3.14/library/re.html#re.compile) and print profile results resembling these:

```python
      214 function calls (207 primitive calls) in 0.002 seconds

Ordered by: cumulative time

ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
     1    0.000    0.000    0.001    0.001 <string>:1(<module>)
     1    0.000    0.000    0.001    0.001 __init__.py:250(compile)
     1    0.000    0.000    0.001    0.001 __init__.py:289(_compile)
     1    0.000    0.000    0.000    0.000 _compiler.py:759(compile)
     1    0.000    0.000    0.000    0.000 _parser.py:937(parse)
     1    0.000    0.000    0.000    0.000 _compiler.py:598(_code)
     1    0.000    0.000    0.000    0.000 _parser.py:435(_parse_sub)

```

That opening line tells us 214 calls were tracked. Among those calls, 207 were *primitive*, meaning the call did not arise through recursion. The line after it, `Ordered by: cumulative time`, says the output is ordered by the `cumtime` values. The column headings are:

ncalls

for the number of calls.

tottime

for the total time the given function itself took (leaving out the time used by calls into sub-functions)

percall

is `tottime` divided by `ncalls`

cumtime

is the accumulated time spent in this function plus every subfunction (from when it was entered until it exited). This number holds up *even* for recursive functions.

percall

is `cumtime` divided by the primitive calls

filename:lineno(function)

provides the respective data of each function

Where two numbers appear in the first column (say `3/1`), the function recursed. The second number counts the primitive calls and the first counts the total calls. Note that when a function does not recurse these two numbers match, and only the one figure is shown.

Rather than printing the output once the profile run finishes, you can store the results in a file by handing a filename to the `run()` function:

```python
import cProfile
import re
cProfile.run('re.compile("foo|bar")', 'restats')

```

The `pstats.Stats` class loads profile results out of a file and can format them in a number of ways.

The files `cProfile` and `profile` may also be run as a script in order to profile another script. For instance:

```python
python -m cProfile [-o output_file] [-s sort_order] (-m module | myscript.py)

```

 -o <output_file>

Writes the profile results to a file instead of to stdout.

[Subject index](INDEX.md) · [Previous](introduction-to-the-profilers.md) · [Continue](instant-user-s-manual-contract-s-sort-order.md)
