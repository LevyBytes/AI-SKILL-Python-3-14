# Python 3.10.0 alpha 1 / core and builtins / text and unicode

[bpo-41006](https://bugs.python.org/issue?@action=redirect&bpo=41006): The `encodings.latin_1` module no longer loads during startup. It is brought in only when serving as the filesystem encoding or the stdio encoding.

[bpo-41094](https://bugs.python.org/issue?@action=redirect&bpo=41094): Repairs decoding faults from audit when files carrying non-ASCII names are opened under a non-UTF-8 locale.

[bpo-41076](https://bugs.python.org/issue?@action=redirect&bpo=41076): Seeds the parser ahead of time with where the f-string expression sits rather than the f-string as a whole, letting us avoid shifting the AST node locations once parsing wraps up.

[bpo-40521](https://bugs.python.org/issue?@action=redirect&bpo=40521): Every interpreter now keeps its own free lists, singletons and caches:

  - Free lists: float, tuple, list, dict, frame, context, asynchronous generator, MemoryError.

  - Singletons: empty tuple, empty bytes string, empty Unicode string, single byte character, single Unicode (latin1) character.

  - Slice cache.

These are no longer common to all interpreters.

[bpo-40904](https://bugs.python.org/issue?@action=redirect&bpo=40904): A potential segfault was corrected in the new PEG parser when it parses an f-string that holds valueless yield statements (`f"{yield}"`). Pablo Galindo wrote the fix.

[bpo-40780](https://bugs.python.org/issue?@action=redirect&bpo=40780): Resolved an edge case in which g-style string formatting of a float neglected to strip trailing zeros.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
