# Python 2.4 changes: Sorted builtin, numeric behavior and module launching

(All changes to `sort()` contributed by Raymond Hettinger.)

- A fresh built-in function `sorted(iterable)` exists that behaves like the in-place [`list.sort()`](https://docs.python.org/3.14/library/stdtypes.html#list.sort) method yet is usable within expressions. The distinctions are:

- the input is allowed to be any iterable;

- a freshly made copy gets sorted, while the original stays untouched; and

- the expression yields the new sorted copy

```python
>>> L = [9,7,8,3,2,4,1,6,5]
>>> [10+i for i in sorted(L)]       # usable in a list comprehension
[11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> L                               # original is left unchanged
[9,7,8,3,2,4,1,6,5]
>>> sorted('Monty Python')          # any iterable may be an input
[' ', 'M', 'P', 'h', 'n', 'n', 'o', 'o', 't', 't', 'y', 'y']

>>> # List the contents of a dict sorted by key values
>>> colormap = dict(red=1, blue=2, green=3, black=4, yellow=5)
>>> for k, v in sorted(colormap.iteritems()):
...     print k, v
...
black 4
blue 2
green 3
red 1
yellow 5

```

(Contributed by Raymond Hettinger.)

- Integer operations are no longer going to set off an `OverflowWarning`. That `OverflowWarning` warning is slated to vanish in Python 2.5.

- The interpreter acquired a fresh switch, [`-m`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-m), which takes a name, hunts for the matching module on `sys.path`, and then executes that module as a script. As an example, you can now invoke the Python profiler via `python -m profile`. (Contributed by Nick Coghlan.)

- The `eval(expr, globals, locals)` and `execfile(filename, globals, locals)` functions, along with the `exec` statement, now accept any mapping type as the *locals* parameter. Earlier, this had to be an ordinary Python dictionary. (Contributed by Raymond Hettinger.)

- The [`zip()`](https://docs.python.org/3.14/library/functions.html#zip) built-in function together with `itertools.izip()` now hand back an empty list when invoked without arguments. Formerly they would raise a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) exception. This renders them more apt for use alongside variable length argument lists:

```python
>>> def transpose(array):
...    return zip(*array)
...
>>> transpose([(1,2,3), (4,5,6)])
[(1, 4), (2, 5), (3, 6)]
>>> transpose([])
[]

```

(Contributed by Raymond Hettinger.)

- Hitting a failure during the import of a module no longer leaves behind a partially initialized module object inside `sys.modules`. That leftover incomplete module object used to trick subsequent imports of that same module into succeeding, which produced baffling errors. (Fixed by Tim Peters.)

- [`None`](https://docs.python.org/3.14/library/constants.html#None) has become a constant; any code that assigns a fresh value to the name `None` now amounts to a syntax error. (Contributed by Raymond Hettinger.)

[Subject index](INDEX.md) · [Previous source section](core-language-changes.md) · [Next source section](optimizations.md) · [Release/subject declaration](pep-218-built-in-set-objects.md) · [Release/subject declaration](core-language-changes.md)
