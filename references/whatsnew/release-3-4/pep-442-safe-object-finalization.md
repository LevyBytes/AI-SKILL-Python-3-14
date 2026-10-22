# What's New In Python 3.4 / PEP 442: Safe Object Finalization

### PEP 442: Safe Object Finalization

[**PEP 442**](https://peps.python.org/pep-0442/) sheds the longstanding restrictions and oddities surrounding object finalization inside CPython. Thanks to it, objects carrying [`__del__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__del__) methods, along with generators holding [`finally`](https://docs.python.org/3.14/reference/compound_stmts.html#finally) clauses, are able to be finalized even while caught up in a reference cycle.

Riding on this change, module globals will no longer be aggressively reset to [`None`](https://docs.python.org/3.14/library/constants.html#None) as the interpreter shuts down in the common case, leaning instead on how the cyclic garbage collector normally behaves. That sidesteps an entire family of shutdown-time interpreter errors, typically tied to `__del__` methods, which had dogged Python ever since cyclic GC arrived.

See also

[**PEP 442**](https://peps.python.org/pep-0442/) ? Safe object finalization

PEP written and implemented by Antoine Pitrou.

[Subject index](INDEX.md) · [Previous source section](pep-445-customization-of-cpython-memory-allocators.md) · [Next source section](pep-456-secure-and-interchangeable-hash-algorithm.md) · [Release/subject declaration](release-highlights.md)
