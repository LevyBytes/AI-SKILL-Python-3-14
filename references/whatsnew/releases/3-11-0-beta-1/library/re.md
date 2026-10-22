# Python 3.11.0 beta 1 / library / re

[bpo-47256](https://bugs.python.org/issue?@action=redirect&bpo=47256): In the [`re`](https://docs.python.org/3.14/library/re.html#module-re) module, the upper bound on capturing groups is now 1,073,741,823 on a 64-bit build, which deepens how far backtracking can reach.

[gh-91575](https://github.com/python/cpython/issues/91575): Bring case-insensitive matching within the [`re`](https://docs.python.org/3.14/library/re.html#module-re) module up to the newest Unicode release.

[gh-91404](https://github.com/python/cpython/issues/91404): Make [`re`](https://docs.python.org/3.14/library/re.html#module-re) matching faster by adopting computed gotos (also called “threaded code”) where the platform allows it and by stripping out costly pointer indirections.

[gh-90568](https://github.com/python/cpython/issues/90568): Parsing of `\N` escapes for Unicode Named Character Sequences inside a [`regular expression`](https://docs.python.org/3.14/library/re.html#module-re) now raises `re.error` in place of `TypeError`.

[gh-91616](https://github.com/python/cpython/issues/91616): In the [`re`](https://docs.python.org/3.14/library/re.html#module-re) module, repair the [`fullmatch()`](https://docs.python.org/3.14/library/re.html#re.Pattern.fullmatch) mismatch that occurs with Atomic Grouping or Possessive Quantifiers.

[bpo-47227](https://bugs.python.org/issue?@action=redirect&bpo=47227): Hold back expression chaining across additional [`re`](https://docs.python.org/3.14/library/re.html#module-re) parsing errors.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
