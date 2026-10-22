# tracemalloc.Traceback: `format()`

total_nframe

The full count of frames that made up the traceback prior to truncation. This attribute may be set to `None` when that information cannot be determined.

Changed in version 3.9: The `Traceback.total_nframe` attribute was added.

 format(*limit=None*, *most_recent_first=False*)

Render the traceback as a list of lines. The [`linecache`](https://docs.python.org/3.14/library/linecache.html#module-linecache) module is used to fetch lines from the source. When *limit* is supplied and positive, render the *limit* most recent frames; when it is negative, render the `abs(limit)` oldest frames instead. When *most_recent_first* is `True`, the formatted frames come back in reversed order, with the most recent frame first rather than last.

Comparable to the [`traceback.format_tb()`](https://docs.python.org/3.14/library/traceback.html#traceback.format_tb) function, except that `format()` leaves out newlines.

Example:

```python
print("Traceback (most recent call first):")
for line in traceback:
    print(line)

```

Output:

```python
Traceback (most recent call first):
  File "test.py", line 9
    obj = Object()
  File "test.py", line 12
    tb = tracemalloc.get_object_traceback(f())

```

[Subject index](INDEX.md) · [Previous](tracemalloc-traceback-class.md) · [Owning module, declaration or section: tracemalloc](tracemalloc-trace-memory-allocations.md) · [Owning module, declaration or section: tracemalloc.Traceback](tracemalloc-traceback-class.md) · [Owning module, declaration or section: Traceback](tracemalloc-traceback-class.md)
