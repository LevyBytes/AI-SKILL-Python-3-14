# importlib.resources.abc – Abstract base classes for resources

# Importlib.Resources.Abc, Importlib.Resources

## Overview

Spans two areas: importlib.resources.abc – Abstract base classes for resources; and importlib.resources – Package resource reading, opening and access.

## importlib.resources.abc – Abstract base classes for resources

*abstractmethod *open_resource(*resource*)

Hands back an opened [file-like object](https://docs.python.org/3.14/glossary.html#term-file-like-object) set up to read the *resource* in binary.

Should the resource be missing, [`FileNotFoundError`](https://docs.python.org/3.14/library/exceptions.html#FileNotFoundError) gets raised.

 *abstractmethod *resource_path(*resource*)

Hands back the file system path pointing at the *resource*.

Where the resource has no actual presence on the file system, raise [`FileNotFoundError`](https://docs.python.org/3.14/library/exceptions.html#FileNotFoundError).

 *abstractmethod *is_resource(*path*)

Hands back `True` when the given *path* counts as a resource. Where *path* is absent, [`FileNotFoundError`](https://docs.python.org/3.14/library/exceptions.html#FileNotFoundError) gets raised.

Changed in version 3.10: The argument *name* was renamed to *path*.

 *abstractmethod *contents()

Hands back an [iterable](https://docs.python.org/3.14/glossary.html#term-iterable) of strings spanning the package's contents. Bear in mind there's no requirement that every name the iterator yields be a genuine resource — for instance, it's fine to yield names where `is_resource()` would come back false.

Permitting non-resource names to surface caters to cases where the way a package and its resources get stored is known ahead of time and those non-resource names prove handy. Yielding subdirectory names, say, is permitted, so that once you know the package and resources sit on the file system, you can put those subdirectory names to direct use.

This abstract method yields an iterable holding no items.

[Subject index](INDEX.md) · [Continue](importlib-resources-abc-resourcereader-class.md) · [Previous](importlib-resources-abc-resourcereader-class.md) · [Continue](traversable-resource-interface.md) · [Owning module, declaration or section: importlib.resources.abc](importlib-resources-abc-resourcereader-class.md) · [Owning module, declaration or section: importlib.resources.abc.ResourceReader](importlib-resources-abc-resourcereader-class.md)
