# What's New In Python 3.9 / Summary ? Release highlights — ast, graphlib, grp, math, operator, os, pwd, random, resource, select, struct, termios, time, zlib, zoneinfo

### What's New In Python 3.9

Editor:

?ukasz Langa

These notes describe what changed in Python 3.9 relative to its predecessor 3.8. The 3.9 line shipped on October 5, 2020. The exhaustive list lives in the [changelog](https://docs.python.org/3.14/whatsnew/changelog.html#changelog).

See also

[**PEP 596**](https://peps.python.org/pep-0596/) - Python 3.9 Release Schedule

### Summary — Release highlights

New syntax features:

- [**PEP 584**](https://peps.python.org/pep-0584/), union operators added to `dict`;

- [**PEP 585**](https://peps.python.org/pep-0585/), type hinting generics in standard collections;

- [**PEP 614**](https://peps.python.org/pep-0614/), relaxed grammar restrictions on decorators.

New built-in features:

- [**PEP 616**](https://peps.python.org/pep-0616/), string methods to remove prefixes and suffixes.

New features in the standard library:

- [**PEP 593**](https://peps.python.org/pep-0593/), flexible function and variable annotations;

- [`os.pidfd_open()`](https://docs.python.org/3.14/library/os.html#os.pidfd_open) added that allows process management without races and signals.

Interpreter improvements:

- [**PEP 573**](https://peps.python.org/pep-0573/), fast access to module state from methods of C extension types;

- [**PEP 617**](https://peps.python.org/pep-0617/), CPython now uses a new parser based on PEG;

- several Python builtins (range, tuple, set, frozenset, list, dict) now run faster thanks to [**PEP 590**](https://peps.python.org/pep-0590/) vectorcall;

- garbage collection does not block on resurrected objects;

- several Python modules (`_abc`, `audioop`, `_bz2`, `_codecs`, `_contextvars`, `_crypt`, `_functools`, `_json`, `_locale`, [`math`](https://docs.python.org/3.14/library/math.html#module-math), [`operator`](https://docs.python.org/3.14/library/operator.html#module-operator), [`resource`](https://docs.python.org/3.14/library/resource.html#module-resource), [`time`](https://docs.python.org/3.14/library/time.html#module-time), `_weakref`) have adopted multiphase initialization per PEP 489;

- several standard library modules (`audioop`, [`ast`](https://docs.python.org/3.14/library/ast.html#module-ast), [`grp`](https://docs.python.org/3.14/library/grp.html#module-grp), `_hashlib`, [`pwd`](https://docs.python.org/3.14/library/pwd.html#module-pwd), `_posixsubprocess`, [`random`](https://docs.python.org/3.14/library/random.html#module-random), [`select`](https://docs.python.org/3.14/library/select.html#module-select), [`struct`](https://docs.python.org/3.14/library/struct.html#module-struct), [`termios`](https://docs.python.org/3.14/library/termios.html#module-termios), [`zlib`](https://docs.python.org/3.14/library/zlib.html#module-zlib)) have moved to the stable ABI per PEP 384.

New library modules:

- [**PEP 615**](https://peps.python.org/pep-0615/), the IANA Time Zone Database now ships inside the standard library via the [`zoneinfo`](https://docs.python.org/3.14/library/zoneinfo.html#module-zoneinfo) module;

- a routine that performs topological sorting over a graph now arrives in the fresh [`graphlib`](https://docs.python.org/3.14/library/graphlib.html#module-graphlib) module.

Release process changes:

- [**PEP 602**](https://peps.python.org/pep-0602/), CPython adopts an annual release cycle.

[Subject index](INDEX.md) · [Next source section](you-should-check-for-deprecationwarning-in-your-code.md)
