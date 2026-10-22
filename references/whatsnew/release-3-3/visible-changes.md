# What's New In Python 3.3 / Visible Changes — importlib, sys

### Visible Changes

The Porting Python code portion documents any edits your code might require.

Apart from everything [`importlib`](https://docs.python.org/3.14/library/importlib.html#module-importlib) now reveals, import shows other observable differences. Chief among them, [`sys.meta_path`](https://docs.python.org/3.14/library/sys.html#sys.meta_path) together with [`sys.path_hooks`](https://docs.python.org/3.14/library/sys.html#sys.path_hooks) now hold every meta path finder and path entry hook that import relies on. Earlier those finders stayed implicit, tucked away inside import’s C code rather than openly surfaced. As a result you can readily drop finders or reorder them to suit your purposes.

A further difference: every module carries a `__loader__` attribute that holds whichever loader built it. [**PEP 302**](https://peps.python.org/pep-0302/) was revised to require loaders to supply this attribute, so down the road, after 3rd-party loaders catch up, people will be able to count on it existing. Meanwhile, though, import assigns it on the module after loading.

Per [**PEP 366**](https://peps.python.org/pep-0366/), loaders are additionally meant to assign the `__package__` attribute. Here too, import already populates it for every loader shipped with [`importlib`](https://docs.python.org/3.14/library/importlib.html#module-importlib), and import sets the attribute post-load on its own.

When no finder turns up on [`sys.path_hooks`](https://docs.python.org/3.14/library/sys.html#sys.path_hooks), `None` now goes into [`sys.path_importer_cache`](https://docs.python.org/3.14/library/sys.html#sys.path_importer_cache). Because `imp.NullImporter` is not surfaced directly on `sys.path_hooks`, you can no longer count on it always being there to serve as the value standing for no finder found.

Every remaining difference involves semantic shifts worth weighing as you bring code up to date for Python 3.3, which is why they belong in the Porting Python code portion of this document.

(Implementation by Brett Cannon)

[Subject index](INDEX.md) · [Previous source section](new-apis.md) · [Next source section](other-language-changes.md) · [Release/subject declaration](summary-release-highlights.md)
