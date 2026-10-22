# tracemalloc: `tracemalloc.Filter`

### Filter

 *class *tracemalloc.Filter(*inclusive: [bool](https://docs.python.org/3.14/library/functions.html#bool)*, *filename_pattern: [str](https://docs.python.org/3.14/library/stdtypes.html#str)*, *lineno: [int](https://docs.python.org/3.14/library/functions.html#int) = None*, *all_frames: [bool](https://docs.python.org/3.14/library/functions.html#bool) = False*, *domain: [int](https://docs.python.org/3.14/library/functions.html#int) = None*)

Filter applied to traces of memory blocks.

For the syntax of *filename_pattern*, consult the [`fnmatch.fnmatch()`](https://docs.python.org/3.14/library/fnmatch.html#fnmatch.fnmatch) function. A `'.pyc'` file extension is swapped for `'.py'`.

Examples:

- `Filter(True, subprocess.__file__)` keeps only the traces belonging to the [`subprocess`](https://docs.python.org/3.14/library/subprocess.html#module-subprocess) module

- `Filter(False, tracemalloc.__file__)` drops the traces of the `tracemalloc` module

- `Filter(False, "<unknown>")` drops empty tracebacks

Changed in version 3.5: A `'.pyo'` file extension no longer gets swapped for `'.py'`.

Changed in version 3.6: Added the `domain` attribute.

[Subject index](INDEX.md) · [Previous](domainfilter.md) · [Continue](filter.md) · [Owning module, declaration or section: tracemalloc](tracemalloc-trace-memory-allocations.md)
