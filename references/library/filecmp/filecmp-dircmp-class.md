# filecmp: `filecmp.dircmp`

### The `dircmp` class

 *class *filecmp.dircmp(*a*, *b*, *ignore=None*, *hide=None*, ***, *shallow=True*)

Build a fresh directory-comparison object for weighing directories `a` and `b` against one another. The `ignore` argument is a roster of names to skip, falling back to `filecmp.DEFAULT_IGNORES`; the `hide` argument is a roster of names to conceal, falling back to `[os.curdir, os.pardir]`.

By default the `dircmp` class weighs files using the `shallow` style of comparison laid out for `filecmp.cmp()`, governed through the `shallow` parameter.

Changed in version 3.13: Added the *shallow* parameter.

These methods are supplied by the `dircmp` class:

[Subject index](INDEX.md) · [Previous](filecmp-cmp-to-filecmp-clear-cache.md) · [Continue](filecmp-dircmp-report-to-filecmp-dircmp-report-full-closure.md) · [Owning module, declaration or section: filecmp](filecmp-cmp-to-filecmp-clear-cache.md)
