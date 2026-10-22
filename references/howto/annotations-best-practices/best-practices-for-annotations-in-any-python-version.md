# Best Practices For `__annotations__` In Any Python Version

### Best Practices For `__annotations__` In Any Python Version

- Steer clear of writing to an object's `__annotations__` member yourself. Leave the job of setting `__annotations__` to Python.

- Should you write to an object's `__annotations__` member directly anyway, make a point of always assigning a `dict` object.

- Refrain from reading `__annotations__` straight off any object. Reach instead for [`annotationlib.get_annotations()`](https://docs.python.org/3.14/library/annotationlib.html#annotationlib.get_annotations) (Python 3.14+) or [`inspect.get_annotations()`](https://docs.python.org/3.14/library/inspect.html#inspect.get_annotations) (Python 3.10+).

- If you do go and read an object's `__annotations__` member directly, confirm it is a dictionary before you start inspecting what it holds.

- Leave `__annotations__` dicts alone rather than altering them.

- Don't go removing an object's `__annotations__` attribute.

[Subject index](INDEX.md) · [Previous source context](manually-un-stringizing-stringized-annotations.md) · [Following source context](annotations-quirks.md)
