# doctest — What's the Execution Context?

### What's the Execution Context?

Out of the box, on every occasion `doctest` locates a docstring to test, it works from a *shallow copy* of `M`'s globals, so that the act of running tests leaves the module's actual globals untouched, and so that one test inside `M` can't scatter crumbs that inadvertently let some other test succeed. The practical effect is that examples may freely reference any names bound at top-level inside `M`, plus names bound earlier in the docstring currently running. What examples cannot reach are names bound within other docstrings.

If you'd rather, you can compel use of a dict of your own as the execution context by handing `globs=your_dict` along to `testmod()` or `testfile()`.

[Subject index](INDEX.md) · [Previous](how-are-docstring-examples-recognized.md) · [Continue](doctest-exception-testing-overview.md) · [Owning module, declaration or section: doctest](interactive-example-testing-overview.md)
