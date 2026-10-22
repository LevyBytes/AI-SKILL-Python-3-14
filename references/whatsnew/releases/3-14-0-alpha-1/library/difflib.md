# Python 3.14.0 alpha 1 / library / difflib

[gh-119105](https://github.com/python/cpython/issues/119105): The `DIffer.compare()` of `difflib` (and therefore `ndiff` as well) can no longer be pushed into cubic-time behavior or unbounded recursion, and tends to run faster in everyday cases too. Output may differ in a few situations, though that should be uncommon. The accuracy of diffs is untouched. A handful of similar lines that sit far apart might now show up as one being deleted and the other added, whereas previously they appeared on neighbouring output lines with markup that highlighted the intraline differences.

[gh-115801](https://github.com/python/cpython/issues/115801): Throw `TypeError` whenever a string reaches [`difflib.unified_diff()`](https://docs.python.org/3.14/library/difflib.html#difflib.unified_diff) or [`difflib.context_diff()`](https://docs.python.org/3.14/library/difflib.html#difflib.context_diff).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
