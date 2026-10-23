# What's New In Python 3.10 / inspect - inspect

### inspect

If a module leaves `__loader__` undefined, the code now drops back to `__spec__.loader`. (Contributed by Brett Cannon in [bpo-42133](https://bugs.python.org/issue?@action=redirect&bpo=42133).)

Add [`inspect.get_annotations()`](https://docs.python.org/3.14/library/inspect.html#inspect.get_annotations), a helper that safely derives the annotations attached to an object. It sidesteps the oddities of reading annotations across differing object kinds, and it presumes very little about whatever object it inspects. `inspect.get_annotations()` is additionally able to correctly un-stringize stringized annotations. Going forward, `inspect.get_annotations()` is treated as the recommended route for reading the annotations dict on any Python object; further guidance on handling annotations well is documented at [Annotations Best Practices](https://docs.python.org/3.14/howto/annotations.html#annotations-howto). In a related change, [`inspect.signature()`](https://docs.python.org/3.14/library/inspect.html#inspect.signature), [`inspect.Signature.from_callable()`](https://docs.python.org/3.14/library/inspect.html#inspect.Signature.from_callable), and `inspect.Signature.from_function()` now invoke `inspect.get_annotations()` to fetch annotations. Consequently `inspect.signature()` and `inspect.Signature.from_callable()` gain the ability to un-stringize stringized annotations too. (Contributed by Larry Hastings in [bpo-43817](https://bugs.python.org/issue?@action=redirect&bpo=43817).)

[Subject index](INDEX.md) · [Previous source section](importlib-metadata.md) · [Next source section](itertools.md) · [Release/subject declaration](summary-release-highlights.md)
