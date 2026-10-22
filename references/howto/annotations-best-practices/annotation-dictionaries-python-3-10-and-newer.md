# Accessing The Annotations Dict Of An Object In Python 3.10 And Newer

### Accessing The Annotations Dict Of An Object In Python 3.10 And Newer

A fresh standard-library function, [`inspect.get_annotations()`](https://docs.python.org/3.14/library/inspect.html#inspect.get_annotations), arrived with Python 3.10. Across the 3.10 through 3.13 releases, reaching for it is the recommended route to the annotations dict of any object that carries annotations. As a bonus, it can “un-stringize” stringized annotations on your behalf.

Python 3.14 ships a brand-new [`annotationlib`](https://docs.python.org/3.14/library/annotationlib.html#module-annotationlib) module dedicated to handling annotations. Among its offerings is an [`annotationlib.get_annotations()`](https://docs.python.org/3.14/library/annotationlib.html#annotationlib.get_annotations) function that now takes the place of [`inspect.get_annotations()`](https://docs.python.org/3.14/library/inspect.html#inspect.get_annotations).

Should [`inspect.get_annotations()`](https://docs.python.org/3.14/library/inspect.html#inspect.get_annotations) not suit your situation for whatever reason, you can reach the `__annotations__` data member by hand. The recommended approach here shifted at 3.10 too: from Python 3.10 onward, `o.__annotations__` is promised to *always* succeed on Python functions, classes, and modules. When you know for sure that the object before you is one of those three *specific* kinds, just read `o.__annotations__` directly to obtain its annotations dict.

That said, callables of other kinds–those built by [`functools.partial()`](https://docs.python.org/3.14/library/functools.html#functools.partial), say–might lack a defined `__annotations__` attribute altogether. To read the `__annotations__` of an object whose nature you can't be sure of, the recommended pattern from 3.10 forward is a three-argument [`getattr()`](https://docs.python.org/3.14/library/functions.html#getattr) call, such as `getattr(o, '__annotations__', None)`.

In releases prior to 3.10, reading `__annotations__` off a class that declares none of its own, yet descends from a parent that does, handed you back the parent’s `__annotations__`. From Python 3.10 forward, what you get for the child class is an empty dict instead.

[Subject index](INDEX.md) · [Previous source context](annotations-best-practices.md) · [Following source context](annotation-dictionaries-python-3-9-and-older.md)
