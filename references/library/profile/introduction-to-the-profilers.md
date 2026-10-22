# Introduction to the profilers

### Introduction to the profilers

`cProfile` and `profile` deliver *deterministic profiling* of Python programs. A *profile* is a collection of statistics describing how frequently and for how long the various parts of a program ran. The `pstats` module can turn those statistics into reports.

Within the Python standard library there are two separate implementations of the same profiling interface:

1.

`cProfile` is the one suggested for most people; it is a C extension whose overhead is modest enough to make it fit for profiling programs that run a long time. It is based on `lsprof`, contributed by Brett Rosen and Ted Czotter.

2.

`profile` is a pure Python module that `cProfile` mimics in its interface, but it piles considerable overhead onto the programs it profiles. When you are trying to extend the profiler somehow, this module may make the job easier. It was originally designed and written by Jim Roskind.

Note

The profiler modules are built to produce an execution profile of a given program, not to serve as benchmarks (for benchmarking, reach for [`timeit`](https://docs.python.org/3.14/library/timeit.html#module-timeit), which gives reasonably accurate results). This is especially true when benchmarking Python code against C code: the profilers add overhead for Python code but not for C-level functions, so the C code would look faster than any Python code.

[Subject index](INDEX.md) · [Previous](the-python-profilers.md) · [Continue](profiler-quickstart-overview.md)
