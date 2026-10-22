# Accessing The Annotations Dict Of An Object In Python 3.9 And Older

### Accessing The Annotations Dict Of An Object In Python 3.9 And Older

On Python 3.9 and earlier, getting at an object's annotations dict is far more involved than it is on the later releases. The root of the trouble is a design defect in those older Pythons, one that specifically concerns class annotations.

For every other sort of object–functions, callables in general, and modules–the recommended way to fetch the annotations dict matches what 3.10 advises, provided you're not invoking [`inspect.get_annotations()`](https://docs.python.org/3.14/library/inspect.html#inspect.get_annotations): turn to a three-argument [`getattr()`](https://docs.python.org/3.14/library/functions.html#getattr) to read the object's `__annotations__` attribute.

Regrettably, that same advice falls short for classes. Here's why: because `__annotations__` is optional on a class, and because a class picks up attributes from its bases, reading a class's `__annotations__` attribute can unintentionally hand back the annotations dict belonging to a *base class.* Consider this:

```python
class Base:
    a: int = 3
    b: str = 'abc'

class Derived(Base):
    pass

print(Derived.__annotations__)

```

What gets printed is the annotations dict belonging to `Base` rather than `Derived`.

You'll need a distinct branch in your code for when the object under inspection turns out to be a class (`isinstance(o, type)`). For that branch, the recommended approach leans on an implementation quirk of Python 3.9 and earlier: when a class does define annotations, they live in that class's [`__dict__`](https://docs.python.org/3.14/reference/datamodel.html#type.__dict__) dictionary. Because a class might or might not have any defined, the recommended move is to invoke the [`get()`](https://docs.python.org/3.14/library/stdtypes.html#dict.get) method on the class dict.

Pulling those pieces together, the snippet below safely reads the `__annotations__` attribute off an arbitrary object on Python 3.9 and earlier:

```python
if isinstance(o, type):
    ann = o.__dict__.get('__annotations__', None)
else:
    ann = getattr(o, '__annotations__', None)

```

Once that code has run, `ann` will hold either a dictionary or `None`. It's worth confirming the type of `ann` with [`isinstance()`](https://docs.python.org/3.14/library/functions.html#isinstance) before you probe it any further.

Keep in mind that certain unusual or broken type objects might be missing a [`__dict__`](https://docs.python.org/3.14/reference/datamodel.html#type.__dict__) attribute, so as an added precaution you might also route access to `__dict__` through [`getattr()`](https://docs.python.org/3.14/library/functions.html#getattr).

[Subject index](INDEX.md) · [Previous source context](annotation-dictionaries-python-3-10-and-newer.md) · [Following source context](manually-un-stringizing-stringized-annotations.md)
