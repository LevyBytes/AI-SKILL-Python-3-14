# sys.path_importer_cache

sys.path_importer_cache

A dictionary that serves as a cache for [finder](https://docs.python.org/3.14/glossary.html#term-finder) objects. Its keys are the paths handed to `sys.path_hooks` and its values are the finders that were discovered. When a path is a valid file system path but `sys.path_hooks` turns up no finder, `None` is stored.

Originally specified in [**PEP 302**](https://peps.python.org/pep-0302/).

[API family](INDEX.md) · [sys context index](../INDEX.md).
