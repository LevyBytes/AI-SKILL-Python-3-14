# What’s New in Python 2.7 / Optimizations — pickle

### Optimizations

A number of speed improvements went in:

- A fresh opcode handles the opening setup for [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statements, fetching the [`__enter__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__enter__) and [`__exit__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__exit__) methods. (Provided by Benjamin Peterson.)

- There is a frequent allocation pattern the garbage collector now copes with much better: creating many objects while freeing none of them. Earlier this drove garbage collection toward quadratic cost, but the count of full collections now climbs more slowly as the heap fills up. The revised rule fires a full pass only after the middle generation has been collected 10 times and when the survivors from that middle generation amount to more than 10% of the objects sitting in the oldest generation. (Martin von Löwis suggested it and Antoine Pitrou implemented it; [bpo-4074](https://bugs.python.org/issue?@action=redirect&bpo=4074).)

- The garbage collector now steers clear of tracking plain containers that cannot take part in a reference cycle. As of Python 2.7 that covers tuples and dicts whose contents are atomic types (ints, strings, and the like). By extension, a dict holding tuples of atomic types is also left untracked. The upshot is cheaper collections, because the collector has fewer objects to examine and walk. (Provided by Antoine Pitrou; [bpo-4688](https://bugs.python.org/issue?@action=redirect&bpo=4688).)

- Internally, long integers are now kept either in base `2**15` or in base `2**30`, with the choice fixed when Python is built. They used to be held in base `2**15` without exception. The base `2**30` representation brings sizable speedups on 64-bit hardware, although benchmark numbers on 32-bit hardware turned out mixed. For that reason the default settles on base `2**30` for 64-bit machines and base `2**15` for 32-bit ones; on Unix a new configure flag `--enable-big-digits` lets you override that default.

Beyond the speed gains, the change should go unnoticed by end users, save for one detail: for the sake of testing and debugging there is a new structseq `sys.long_info` that reports the internal layout, telling you how many bits each digit holds and how many bytes the C type that stores a digit occupies:

```python
>>> import sys
>>> sys.long_info
sys.long_info(bits_per_digit=30, sizeof_digit=4)

```

(Provided by Mark Dickinson; [bpo-4258](https://bugs.python.org/issue?@action=redirect&bpo=4258).)

A separate round of work trimmed long objects by a few bytes apiece, shaving off 2 bytes on 32-bit systems and 6 on 64-bit ones. Mark Dickinson did this work; [bpo-5260](https://bugs.python.org/issue?@action=redirect&bpo=5260).

- Division of long integers has been sped up by tightening its inner loop, swapping multiplications for shifts, and removing a needless extra iteration. Across various benchmarks, long integer divide and modulo operations come out 50% to 150% quicker. (Provided by Mark Dickinson; [bpo-5512](https://bugs.python.org/issue?@action=redirect&bpo=5512).) Bitwise operations have likewise gotten much quicker, starting from an initial patch by Gregory Smith; [bpo-1087418](https://bugs.python.org/issue?@action=redirect&bpo=1087418).

- The `%` implementation now detects when the left operand is a Python string and takes a special path for it, which yields a 1–3% gain for programs that lean on `%` with strings a lot, such as templating libraries. (Done by Collin Winter; [bpo-5176](https://bugs.python.org/issue?@action=redirect&bpo=5176).)

- When a list comprehension carries an `if` condition, it now compiles down to quicker bytecode. Antoine Pitrou wrote the patch, and Jeffrey Yasskin then back-ported it to 2.7; [bpo-4715](https://bugs.python.org/issue?@action=redirect&bpo=4715).

- Rendering an integer or long integer as a decimal string got faster thanks to a dedicated base-10 path that replaces the general routine for arbitrary bases. (Patch from Gawain Bolton; [bpo-6713](https://bugs.python.org/issue?@action=redirect&bpo=6713).)

- For the string-like types (strings, Unicode strings, and [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) objects), the `split()`, `replace()`, `rindex()`, `rpartition()`, and `rsplit()` methods now lean on a fast reverse-search algorithm in place of a one-character-at-a-time scan. On occasion that runs as much as 10 times faster. (Added by Florent Xicluna; [bpo-7462](https://bugs.python.org/issue?@action=redirect&bpo=7462) and [bpo-7622](https://bugs.python.org/issue?@action=redirect&bpo=7622).)

- To cut the memory footprint of objects produced by unpickling, the [`pickle`](https://docs.python.org/3.14/library/pickle.html#module-pickle) and `cPickle` modules now intern attribute-name strings automatically. (Provided by Jake McGuire; [bpo-5084](https://bugs.python.org/issue?@action=redirect&bpo=5084).)

- A dedicated path for dictionaries in the `cPickle` module now cuts the time it takes to pickle them roughly in half. (Provided by Collin Winter; [bpo-5670](https://bugs.python.org/issue?@action=redirect&bpo=5670).)

[Subject index](INDEX.md) · [Previous source section](interpreter-changes.md) · [Next source section](standard-library-module-changes.md) · [Release/subject declaration](the-future-for-python-2-x.md)
