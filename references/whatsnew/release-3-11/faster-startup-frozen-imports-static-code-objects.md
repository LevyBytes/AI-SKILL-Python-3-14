# What's New In Python 3.11 / Faster Startup / Frozen imports / Static code objects

### Faster Startup

#### Frozen imports / Static code objects

To accelerate module loading, Python keeps [bytecode](https://docs.python.org/3.14/glossary.html#term-bytecode) cached inside the [__pycache__](https://docs.python.org/3.14/tutorial/modules.html#tut-pycache) directory.

Back in 3.10, running a Python module went like this:

```text
Read __pycache__ -> Unmarshal -> Heap allocated code object -> Evaluate

```

Within Python 3.11, the core modules that Python startup depends on are "frozen". What that means is the interpreter statically allocates their [Code Objects](https://docs.python.org/3.14/c-api/code.html#codeobjects) (and bytecode). Doing so trims the module execution process down to fewer steps:

```text
Statically allocated code object -> Evaluate

```

Within Python 3.11, interpreter startup has gotten 10-15% quicker. Short-running programs that use Python feel a sizable benefit from this.

[Subject index](INDEX.md) · [Previous source section](faster-cpython.md) · [Next source section](faster-runtime-cheaper-lazy-python-frames.md) · [Release/subject declaration](summary-release-highlights.md)
