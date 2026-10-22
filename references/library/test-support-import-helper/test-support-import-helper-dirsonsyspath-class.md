# test.support.import_helper: `test.support.import_helper.DirsOnSysPath`

*class *test.support.import_helper.DirsOnSysPath(**paths*)

A context manager that, for the span of its block, tacks directories onto [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path).

It takes a snapshot of [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path), appends whichever directories were handed in as positional arguments, and once the context closes it restores `sys.path` back to that saved snapshot.

Take note that *every* change to [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path) made inside the context manager's body, replacing the object included, gets rolled back when the block finishes.

[Subject index](INDEX.md) · [Previous](test-support-import-helper-cleanimport-class.md) · [Continue](../test-support-warnings-helper/warning-test-suppression-and-checks.md) · [Owning module, declaration or section: test.support.import_helper](import-test-cache-and-bytecode-helpers.md)
