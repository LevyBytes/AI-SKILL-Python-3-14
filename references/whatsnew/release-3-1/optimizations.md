# What’s New In Python 3.1 / Optimizations - json

### Optimizations

Significant speed gains have been folded in:

- Largely coded in Python, the new I/O library (laid out in [**PEP 3116**](https://peps.python.org/pep-3116/)) soon turned into a troublesome chokepoint under Python 3.0. Under Python 3.1, that I/O library was rewritten from scratch in C, running 2 to 20 times faster according to the workload. For those who want to tinker, the pure Python edition remains reachable through the `_pyio` module.

(Contributed by Amaury Forgeot d’Arc and Antoine Pitrou.)

- A heuristic was added so the garbage collector skips tracking tuples and dicts that contain nothing but untrackable objects. Depending on how a program uses datatypes, this can shrink the collections and thereby the garbage collection cost on programs that run a long time.

(Contributed by Antoine Pitrou, [bpo-4688](https://bugs.python.org/issue?@action=redirect&bpo=4688).)

- Turning on a configure option called `--with-computed-gotos` where the compiler permits it (notably: gcc, SunPro, icc) builds the bytecode evaluation loop around a fresh dispatch scheme, delivering gains of as much as 20% according to the platform, the compiler, and the benchmark.

(Contributed by Antoine Pitrou along with a number of other participants, [bpo-4753](https://bugs.python.org/issue?@action=redirect&bpo=4753)).

- Decoding UTF-8, UTF-16 and LATIN-1 now runs two to four times faster.

(Contributed by Antoine Pitrou and Amaury Forgeot d’Arc, [bpo-4868](https://bugs.python.org/issue?@action=redirect&bpo=4868).)

- A C extension was given to the [`json`](https://docs.python.org/3.14/library/json.html#module-json) module to lift its speed considerably. On top of that, the API changed so json deals only with [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) and not with [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes). That shift lines the module up tightly with the [JSON specification](https://json.org/), which is laid out in terms of Unicode.

(Bob Ippolito contributed it; Antoine Pitrou and Benjamin Peterson ported it to Py3.1; [bpo-4136](https://bugs.python.org/issue?@action=redirect&bpo=4136).)

- During unpickling, the attribute names of pickled objects now get interned. That trims memory use and lets pickles come out smaller.

(Contributed by Jake McGuire and Antoine Pitrou; [bpo-5084](https://bugs.python.org/issue?@action=redirect&bpo=5084).)

[Subject index](INDEX.md) · [Previous source section](imap-import-and-pickle-module-changes.md) · [Next source section](idle.md) · [Release/subject declaration](pep-372-ordered-dictionaries.md)
