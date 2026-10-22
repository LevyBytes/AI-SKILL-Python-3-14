# 5.6. Replacing the standard import system

### 5.6. Replacing the standard import system

The surest way to swap out the whole import system is to clear the default contents of [`sys.meta_path`](https://docs.python.org/3.14/library/sys.html#sys.meta_path) and put a custom meta path hook entirely in their place.

If changing nothing more than the behaviour of import statements is fine — leaving alone the other APIs that reach into the import system — then swapping out the builtin [`__import__()`](https://docs.python.org/3.14/library/functions.html#import__) function may well do the job.

To block the import of certain modules selectively from a hook placed early on the meta path (instead of switching off the standard import system altogether), it suffices to raise [`ModuleNotFoundError`](https://docs.python.org/3.14/library/exceptions.html#ModuleNotFoundError) straight from [`find_spec()`](https://docs.python.org/3.14/library/importlib.html#importlib.abc.MetaPathFinder.find_spec) rather than handing back `None`. Returning `None` says the meta path search ought to keep going, whereas raising an exception stops it on the spot.

[Subject index](INDEX.md) · [Owning language section](the-import-system.md) · [Previous source section](path-entry-finder-protocol.md) · [Following source section](package-relative-imports.md)
