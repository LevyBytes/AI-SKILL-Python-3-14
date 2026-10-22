# What's New In Python 3.11 / FAQ / I don’t see any speedups in my workload. Why?

#### I don’t see any speedups in my workload. Why?

Some workloads simply won't gain anything visible. Programs dominated by I/O time, or those already pushing most arithmetic into a C extension such as NumPy, see little change. For now it's the pure-Python workloads that gain the most from this effort.

On top of that, the pyperformance number is a geometric mean. Within that suite itself a handful of benchmarks regressed a touch, whereas a few others jumped almost 2x faster!

[Subject index](INDEX.md) · [Previous source section](faq-will-cpython-3-11-use-more-memory.md) · [Next source section](faq-is-there-a-jit-compiler.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](faq-how-should-i-write-my-code-to-utilize-these-speedups.md)
