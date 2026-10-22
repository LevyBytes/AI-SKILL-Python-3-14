# What's New In Python 3.11 / Faster Runtime / Cheaper, lazy Python frames — inspect, sys

> (Contributed by Eric Snow, Guido van Rossum and Kumar Aditya in many issues.)

### Faster Runtime

#### Cheaper, lazy Python frames

Every time Python invokes a Python function, a Python frame carrying execution information gets created. Here are the new frame optimizations:

- Streamlined the frame creation process.

- Sidestepped memory allocation by liberally recycling frame space on the C stack.

- Pared the internal frame struct down to only the essential information. Earlier, frames carried surplus debugging and memory management information.

Old-style [frame objects](https://docs.python.org/3.14/reference/datamodel.html#frame-objects) now come into being solely when a debugger asks, or when Python introspection functions like [`sys._getframe()`](https://docs.python.org/3.14/library/sys.html#sys._getframe) and [`inspect.currentframe()`](https://docs.python.org/3.14/library/inspect.html#inspect.currentframe) request them. The bulk of user code triggers no frame object creation whatsoever. The upshot is that almost every Python function call has gained significant speed. Our pyperformance numbers showed a 3-7% speedup.

[Subject index](INDEX.md) · [Previous source section](faster-startup-frozen-imports-static-code-objects.md) · [Next source section](faster-runtime-inlined-python-function-calls.md) · [Release/subject declaration](summary-release-highlights.md)
