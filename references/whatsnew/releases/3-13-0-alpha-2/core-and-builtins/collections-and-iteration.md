# Python 3.13.0 alpha 2 / core and builtins / collections and iteration

[gh-81137](https://github.com/python/cpython/issues/81137): Mark assignment to a function's `__code__` field deprecated whenever the incoming code object is of a clashing type (for instance, going from a generator to an ordinary function).

[gh-109094](https://github.com/python/cpython/issues/109094): Swap `prev_instr` on the interpreter frame for `instr_ptr`, which targets the start of the instruction now running (or set to run once the frame resumes).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
