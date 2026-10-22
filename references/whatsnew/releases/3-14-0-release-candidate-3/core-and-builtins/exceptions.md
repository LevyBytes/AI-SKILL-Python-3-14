# Python 3.14.0 release candidate 3 / core and builtins / exceptions

[gh-71810](https://github.com/python/cpython/issues/71810): Throw [`OverflowError`](https://docs.python.org/3.14/library/exceptions.html#OverflowError) from `(-1).to_bytes()` during signed conversions whenever the byte count equals zero. Sergey B Kirpichev contributed the patch.

[gh-138372](https://github.com/python/cpython/issues/138372): Repair the [`SyntaxWarning`](https://docs.python.org/3.14/library/exceptions.html#SyntaxWarning) raised for faulty subscript expressions that contain [template string literals](https://docs.python.org/3.14/reference/lexical_analysis.html#t-strings). Brian Schubert contributed the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
