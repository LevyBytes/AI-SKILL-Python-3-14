# Python 3.13.0 beta 1 / library / functions and types

[gh-118225](https://github.com/python/cpython/issues/118225): A new `copy_replace()` method on `PhotoImage` copies a region from one image into another, optionally applying pixel zooming or subsampling. A *from_coords* parameter was added to the `PhotoImage` methods `copy()`, `zoom()` and `subsample()`. The `copy()` method on `PhotoImage` additionally gained *zoom* and *subsample* parameters.

[gh-100242](https://github.com/python/cpython/issues/100242): Aligns the pure Python `functools.partial.__new__` more closely with the C implementation by no longer simply checking always for an attribute named `'func'` on the first argument of `partial`. Both the Python and the C versions instead run an `isinstance(func, partial)` check against that first argument of `partial`.

[bpo-32839](https://bugs.python.org/issue?@action=redirect&bpo=32839): Adds the `after_info()` method to Tkinter widgets.

[gh-111744](https://github.com/python/cpython/issues/111744): Calls to `breakpoint()` and `pdb.set_trace()` now drop into the debugger right after the call instead of waiting until the following line runs.

[gh-101732](https://github.com/python/cpython/issues/101732): Reach for a Y2038 compatible openssl time function wherever one exists.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
