# What's new in Python 3.14 / A new type of interpreter

### A new type of interpreter

CPython gains a fresh interpreter variety. In place of one sprawling C `case` statement, it threads tail calls between compact C functions, each handling an individual Python opcode. On some newer toolchains this interpreter yields a notable speed boost. Early measurements point to a geometric-mean improvement of 3-5% across the standard `pyperformance` benchmark suite, varying with platform and architecture. That comparison uses Python 3.14 compiled by Clang 19 without the new interpreter as its baseline.

For the moment this interpreter runs only under Clang 19 or later on the x86-64 and AArch64 architectures. That said, an upcoming GCC release is anticipated to add support as well.

Opting in is required for now. Turning on profile-guided optimization is strongly advised alongside the new interpreter, since that is the sole tested-and-validated setup for the performance gains. Additional details are at [`--with-tail-call-interp`](https://docs.python.org/3.14/using/configure.html#cmdoption-with-tail-call-interp).

Note

Don't mix this up with [tail call optimization](https://en.wikipedia.org/wiki/Tail_call) of Python functions, something CPython does not presently implement.

This fresh interpreter variety amounts to an internal implementation detail of the CPython interpreter. The observable behavior of Python programs stays exactly the same. Performance may rise, yet nothing else shifts.

[Subject index](INDEX.md) · [Previous source section](pep-768-safe-external-debugger-interface.md) · [Next source section](free-threaded-mode-improvements.md) · [Release/subject declaration](summary-release-highlights.md)
