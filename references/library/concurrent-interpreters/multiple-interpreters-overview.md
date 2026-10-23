# concurrent.interpreters`concurrent.interpreters` - Multiple interpreters in the same process

## concurrent.interpreters - Multiple interpreters in the same process

### `concurrent.interpreters` - Multiple interpreters in the same process

Added in version 3.14.

**Source code:** [Lib/concurrent/interpreters](https://github.com/python/cpython/tree/3.14/Lib/concurrent/interpreters)

---

Sitting atop the lower-level `_interpreters` module, the `concurrent.interpreters` module builds friendlier, higher-level interfaces.

Its chief aim is to hand you a basic API for managing interpreters (a.k.a. “subinterpreters”) and for running work inside them. To run something you mostly switch over to an interpreter (within the current thread) and invoke a function in that execution context.

When it comes to concurrency, the interpreters on their own — and this module — give you little beyond isolation, and isolation by itself buys you nothing. Real concurrency arrives separately by way of [`threads`](https://docs.python.org/3.14/library/threading.html#module-threading) See below

See also

[`InterpreterPoolExecutor`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.InterpreterPoolExecutor)

Marries threads to interpreters behind an interface you already know.

[Isolating Extension Modules](https://docs.python.org/3.14/howto/isolating-extensions.html#isolating-extensions-howto)

Steps for reworking an extension module so it copes with multiple interpreters.

[**PEP 554**](https://peps.python.org/pep-0554/)

[**PEP 734**](https://peps.python.org/pep-0734/)

[**PEP 684**](https://peps.python.org/pep-0684/)

[Availability](https://docs.python.org/3.14/library/intro.html#availability): not WASI.

On WebAssembly this module is either inoperative or missing. Turn to [WebAssembly platforms](https://docs.python.org/3.14/library/intro.html#wasm-availability) for the details.

[Subject index](INDEX.md) · [Continue](key-details.md)
