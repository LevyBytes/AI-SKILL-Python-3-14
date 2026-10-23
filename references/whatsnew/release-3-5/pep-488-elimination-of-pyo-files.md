# What’s New In Python 3.5 / PEP 488: Elimination of PYO files - importlib

> PEP written and implemented by Paul Moore.

### PEP 488: Elimination of PYO files

[**PEP 488**](https://peps.python.org/pep-0488/) retires the whole notion of `.pyo` files. As a result, a single `.pyc` file now stands in for both the unoptimized and the optimized bytecode. So that bytecode does not require endless regeneration, each `.pyc` file may carry an optional `opt-` tag within its name once the bytecode has been optimized. A welcome side effect is that bytecode file names no longer collide when execution happens under either [`-O`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-O) or [`-OO`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-OO). It follows that bytecode files produced via `-O`, and `-OO` are now able to coexist. [`importlib.util.cache_from_source()`](https://docs.python.org/3.14/library/importlib.html#importlib.util.cache_from_source) received an adjusted API to accommodate this shift.

See also

[**PEP 488**](https://peps.python.org/pep-0488/) ? Elimination of PYO files

[Subject index](INDEX.md) · [Previous source section](pep486-launcher-virtual-environment-awareness.md) · [Next source section](pep-489-multi-phase-extension-module-initialization.md) · [Release/subject declaration](summary-release-highlights.md)
