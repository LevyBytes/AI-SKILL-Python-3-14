# C API Stability

### C API Stability

Except where the docs say otherwise, the Backwards Compatibility Policy, [**PEP 387**](https://peps.python.org/pep-0387/), governs Python's C API. The bulk of its changes keep source compatibility, usually by adding new API and nothing more. Altering or dropping existing API happens only once a deprecation window passes or when a serious problem demands it.

Across a single minor release, CPython's Application Binary Interface (ABI) stays compatible in both directions (assuming identical build settings; consult Platform Considerations below). Thus a binary built for Python 3.10.0 runs on 3.10.8 and the reverse holds too, yet it must be rebuilt on its own for 3.9.x and 3.11.x.

The C API splits into two tiers, each carrying its own stability expectations:

- Unstable API, which can shift between minor versions with no deprecation period. The `PyUnstable` prefix on names flags it.

- Limited API, which holds compatible over a span of minor releases. With `Py_LIMITED_API` defined, `Python.h` reveals only this subset.

More detail on each appears further down.

Names that begin with an underscore, for instance `_Py_InternalState`, are private API liable to change without warning even between patch releases. Should you find you need such API, think about contacting the [CPython developers](https://discuss.python.org/c/core-dev/c-api/30) about introducing public API to cover your scenario.

[Subject index](INDEX.md) · [Following source contract](unstable-c-api.md)
