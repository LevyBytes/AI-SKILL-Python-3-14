# `__annotations__` Quirks

### `__annotations__` Quirks

Throughout every Python 3 release, a function object will lazily conjure an annotations dict whenever none has been declared on it. You may drop the `__annotations__` attribute with `del fn.__annotations__`, yet should you read `fn.__annotations__` afterward, the object simply manufactures a fresh empty dict, stashes it, and returns it as its annotations. Removing a function's annotations before it has lazily built that dict raises an `AttributeError`, and running `del fn.__annotations__` two times back to back is sure to raise an `AttributeError` every time.

From Python 3.10 onward, every point made in the paragraph above holds for class and module objects as well.

Under any Python 3 release, you're allowed to assign `None` to `__annotations__` on a function object. Even so, a later read of that object's annotations via `fn.__annotations__` will lazily spin up an empty dictionary, just as the opening paragraph here describes. Modules and classes behave differently in every Python version: they let you set `__annotations__` to whatever Python value you like and hold on to exactly that value.

When Python stringizes annotations on your behalf (by way of `from __future__ import annotations`) and you give a string as an annotation, that string ends up quoted on top of being a string. The net result is an annotation quoted *twice.* Here's an illustration:

```python
from __future__ import annotations
def foo(a: "str"): pass

print(foo.__annotations__)

```

The output here is `{'a': "'str'"}`. Calling that a “quirk” is a stretch; it appears in this list only on the off chance it catches you off guard.

Read `__annotations__` off a class that uses a custom metaclass and you may run into surprising behaviour; [**749**](https://peps.python.org/pep-0749/#pep749-metaclasses) collects a few examples. Sidestep these quirks by going through [`annotationlib.get_annotations()`](https://docs.python.org/3.14/library/annotationlib.html#annotationlib.get_annotations) on Python 3.14+ or [`inspect.get_annotations()`](https://docs.python.org/3.14/library/inspect.html#inspect.get_annotations) on Python 3.10+. For older Pythons, dodge the same bugs by pulling the annotations out of the class's [`__dict__`](https://docs.python.org/3.14/reference/datamodel.html#type.__dict__) — for instance, `cls.__dict__.get('__annotations__', None)`.

On certain Python releases, a class instance may carry an `__annotations__` attribute, but relying on that is unsupported. When you need an instance's annotations, get at its class through [`type()`](https://docs.python.org/3.14/library/functions.html#type) — for example, `annotationlib.get_annotations(type(myinstance))` on Python 3.14+.

[Subject index](INDEX.md) · [Previous source context](best-practices-for-annotations-in-any-python-version.md) · [Following source context](../migrating-optparse-code-to-argparse/migrating-optparse-code-to-argparse.md)
