# What's New In Python 3.4 / Summary - Release Highlights - asyncio, ensurepip, enum, marshal, pathlib, select, selectors, statistics, tracemalloc

### What's New In Python 3.4

Author:

R. David Murray <[rdmurray@bitdance.com](mailto:rdmurray%40bitdance.com)> (Editor)

This document covers the additions that distinguish Python 3.4 from its predecessor 3.3. The 3.4 release shipped on March 16, 2014. The complete record is available in the [changelog](https://docs.python.org/3.4/whatsnew/changelog.html).

See also

[**PEP 429**](https://peps.python.org/pep-0429/): Python 3.4 Release Schedule

### Summary - Release Highlights

New syntax features:

- This release introduced no fresh syntax additions.

Other new features:

- pip should always be available ([**PEP 453**](https://peps.python.org/pep-0453/)).

- Newly created file descriptors are non-inheritable ([**PEP 446**](https://peps.python.org/pep-0446/)).

- command line option for isolated mode ([bpo-16499](https://bugs.python.org/issue?@action=redirect&bpo=16499)).

- better handling for codecs that fall outside text encoding territory (several issues).

- A ModuleSpec Type for the Import System ([**PEP 451**](https://peps.python.org/pep-0451/)). (Affects importer authors.)

- The [`marshal`](https://docs.python.org/3.14/library/marshal.html#module-marshal) format has been made more compact and efficient ([bpo-16475](https://bugs.python.org/issue?@action=redirect&bpo=16475)).

New library modules:

- [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio): New provisional API for asynchronous IO ([**PEP 3156**](https://peps.python.org/pep-3156/)).

- [`ensurepip`](https://docs.python.org/3.14/library/ensurepip.html#module-ensurepip): Bootstrapping the pip installer ([**PEP 453**](https://peps.python.org/pep-0453/)).

- [`enum`](https://docs.python.org/3.14/library/enum.html#module-enum): Support for enumeration types ([**PEP 435**](https://peps.python.org/pep-0435/)).

- [`pathlib`](https://docs.python.org/3.14/library/pathlib.html#module-pathlib): Object-oriented filesystem paths ([**PEP 428**](https://peps.python.org/pep-0428/)).

- [`selectors`](https://docs.python.org/3.14/library/selectors.html#module-selectors): Efficient, high-level I/O multiplexing layered on top of the [`select`](https://docs.python.org/3.14/library/select.html#module-select) module's primitives (a piece of [**PEP 3156**](https://peps.python.org/pep-3156/)).

- [`statistics`](https://docs.python.org/3.14/library/statistics.html#module-statistics): A basic numerically stable statistics library ([**PEP 450**](https://peps.python.org/pep-0450/)).

- [`tracemalloc`](https://docs.python.org/3.14/library/tracemalloc.html#module-tracemalloc): Trace Python memory allocations ([**PEP 454**](https://peps.python.org/pep-0454/)).

Significantly improved library modules:

-

[Subject index](INDEX.md) · [Next source section](language-and-library-release-highlights.md)
