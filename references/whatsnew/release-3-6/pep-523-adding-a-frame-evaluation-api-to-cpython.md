# What's New In Python 3.6 / PEP 523: Adding a frame evaluation API to CPython

### PEP 523: Adding a frame evaluation API to CPython

Python hands you broad control over how code runs, yet one corner stayed off-limits: the evaluation of frame objects. Anyone wanting to step into frame evaluation from Python had no real avenue short of directly fiddling with function pointers on defined functions.

[**PEP 523**](https://peps.python.org/pep-0523/) flips that by exposing an API that makes frame evaluation swappable down at the C level. This opens the door for tooling such as debuggers and JITs to step into frame evaluation ahead of Python code starting to run. With it you can plug in alternative evaluation implementations for Python code, follow frame evaluation, and so on.

This API sits outside the limited C API and bears a private marking to convey that its use is meant to stay narrow and to suit only highly specific, low-level scenarios. The API's semantics will shift alongside Python whenever required.

See also

[**PEP 523**](https://peps.python.org/pep-0523/) — Adding a frame evaluation API to CPython

PEP written by Brett Cannon and Dino Viehland.

[Subject index](INDEX.md) · [Previous source section](new-dict-implementation.md) · [Next source section](pythonmalloc-environment-variable.md) · [Release/subject declaration](summary-release-highlights.md)
