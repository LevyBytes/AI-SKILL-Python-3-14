# What's New In Python 3.11 / Faster Runtime / PEP 659: Specializing Adaptive Interpreter

> (Contributed by Pablo Galindo and Mark Shannon in [bpo-45256](https://bugs.python.org/issue?@action=redirect&bpo=45256).)

#### PEP 659: Specializing Adaptive Interpreter

One of the cornerstone pieces of the Faster CPython project is [**PEP 659**](https://peps.python.org/pep-0659/). The core notion: even though Python is a dynamic language, the majority of code contains stretches where types and objects shift only rarely. That idea goes by the name *type stability*.

While running, Python tries to spot recurring patterns plus type stability throughout the code being executed. From there Python swaps the present operation for a more specialized variant. That specialized operation takes fast paths reserved for those particular types/use cases, and these generally beat the generic equivalents. Out of this comes a further idea termed *inline caching*, in which Python stashes the outcomes of costly operations right inside the [bytecode](https://docs.python.org/3.14/glossary.html#term-bytecode).

On top of that, the specializer folds particular common instruction pairs into a single superinstruction, which cuts the execution overhead.

Specialization only kicks in once Python spots code that is "hot" (run several times). That keeps Python from squandering effort on run-once code. Should code turn overly dynamic, or the usage shift, Python is also able to de-specialize. Because specialization gets retried on a regular basis and each attempt is fairly cheap, it can adjust to fresh conditions.

> (PEP written by Mark Shannon, with ideas inspired by Stefan Brunthaler. See [**PEP 659**](https://peps.python.org/pep-0659/) for more information. Implementation by Mark Shannon and Brandt Bucher, with additional help from Irit Katriel and Dennis Sweeney.)

| Operation | Form | Specialization | Operation speedup (up to) | Contributor(s) |
| --- | --- | --- | --- | --- |
| Binary operations | `x + x` `x - x` `x * x` | Adding, multiplying, and subtracting for widely-used types like `int`, `float` and `str` follow tailored fast paths keyed to the values' underlying types. | 10% | Mark Shannon, Donghee Na, Brandt Bucher, Dennis Sweeney |
| Subscript | `a[i]` | Indexing into container types like `list`, `tuple` and `dict` reaches straight into the backing data structures. A custom `__getitem__()` subscript is likewise inlined, much as Inlined Python function calls are. | 10-25% | Irit Katriel, Mark Shannon |
| Store subscript | `a[i] = z` | Built on the subscript specialization described just above. | 10-25% | Dennis Sweeney |
| Calls | `f(arg)` `C(arg)` | When you invoke widespread builtin (C) functions and types like `len()` and `str`, the runtime jumps straight to their C version, sidestepping the internal calling convention. | 20% | Mark Shannon, Ken Jin |
| Load global variable | `print` `len` | An entry's position within the globals/builtins namespace gets cached, so fetching globals and builtins costs zero namespace lookups. | [1] | Mark Shannon |
| Load attribute | `o.attr` | This mirrors how global variables load. Caching the attribute's slot inside the class or object namespace means attribute reads usually take zero namespace lookups. | [2] | Mark Shannon |
| Load methods for call | `o.meth()` | The method's real address is stored in the cache. Resolving a method no longer costs any namespace lookups, including classes carrying lengthy inheritance chains. | 10-20% | Ken Jin, Mark Shannon |
| Store attribute | `o.attr = z` | Built on the same idea as the load attribute optimization. | 2% in pyperformance | Mark Shannon |
| Unpack Sequence | `*seq` | Tuned for everyday containers like `list` and `tuple`, skipping the internal calling convention. | 8% | Brandt Bucher |

[Subject index](INDEX.md) · [Previous source section](faster-runtime-inlined-python-function-calls.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](faster-runtime-cheaper-lazy-python-frames.md) · [Next source section](misc.md)
