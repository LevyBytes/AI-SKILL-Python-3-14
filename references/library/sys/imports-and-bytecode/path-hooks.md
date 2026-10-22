# sys.path_hooks

sys.path_hooks

A list of callables that accept a path argument and attempt to construct a [finder](https://docs.python.org/3.14/glossary.html#term-finder) for that path. When a finder can be built, the callable should return it; otherwise it should raise [`ImportError`](https://docs.python.org/3.14/library/exceptions.html#ImportError).

Originally specified in [**PEP 302**](https://peps.python.org/pep-0302/).

[API family](INDEX.md) · [sys context index](../INDEX.md).
