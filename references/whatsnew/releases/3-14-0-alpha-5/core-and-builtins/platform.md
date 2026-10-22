# Python 3.14.0 alpha 5 / core and builtins / platform

[gh-128563](https://github.com/python/cpython/issues/128563): CPython has gained a new interpreter variety. This one drives its instruction handlers with tail calls. Early benchmarks point to a 7-11% geometric mean speedup on pyperformance (varying by platform), reaching as much as 30% on Python-intensive workloads. For now this interpreter runs only under newer compilers like `clang-19`; the rest keep using the old interpreter. Ken Jin wrote the patch, drawing on ideas for implementing it within CPython from Mark Shannon, Garret Gu, Haoran Xu, and Josh Haberman.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
