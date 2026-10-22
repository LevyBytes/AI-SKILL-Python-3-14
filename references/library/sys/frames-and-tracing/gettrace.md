# sys.gettrace

sys.gettrace()

Fetch the trace function as installed by `settrace()`.

**CPython implementation detail:** The `gettrace()` function exists solely to support building debuggers, profilers, coverage tools and similar utilities. Because its behavior belongs to the implementation platform instead of the language definition, certain Python implementations may not offer it at all.

[API family](INDEX.md) · [sys context index](../INDEX.md).
