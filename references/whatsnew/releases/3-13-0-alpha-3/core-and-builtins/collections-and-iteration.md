# Python 3.13.0 alpha 3 / core and builtins / collections and iteration

[gh-112320](https://github.com/python/cpython/issues/112320): For branch instructions the Tier 2 translator now follows a confidence level for remaining “on trace” (that is, not dropping back into the Tier 1 interpreter), derived from how many bits are set in the branch “counter”. Once confidence falls under 1/3rd, trace translation stops.

[gh-113655](https://github.com/python/cpython/issues/113655): The C recursion limit was set to 4000 under Windows and 10000 under Linux/OSX. That range appears close to the sweet spot for keeping safety intact while preserving backwards compatibility.

[gh-113753](https://github.com/python/cpython/issues/113753): Resolved a problem where the finalizer belonging to `PyAsyncGenASend` objects could go uncalled whenever they came from a free list.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
