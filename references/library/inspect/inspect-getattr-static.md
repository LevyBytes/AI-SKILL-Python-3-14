# inspect - Fetching attributes statically

### Fetching attributes statically

Each of [`getattr()`](https://docs.python.org/3.14/library/functions.html#getattr) and [`hasattr()`](https://docs.python.org/3.14/library/functions.html#hasattr) may set code running while it fetches an attribute or tests whether one is present. Descriptors such as properties get invoked, and [`__getattr__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getattr__) along with [`__getattribute__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getattribute__) may fire.

In situations calling for hands-off introspection — documentation tooling being one — that behaviour gets in the way. `getattr_static()` carries a signature much like [`getattr()`](https://docs.python.org/3.14/library/functions.html#getattr), yet it refrains from running any code while pulling attributes.

 inspect.getattr_static(*obj*, *attr*)

 inspect.getattr_static(*obj*, *attr*, *default*)

Fetch attributes while bypassing any dynamic resolution through the descriptor protocol, [`__getattr__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getattr__), or [`__getattribute__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getattribute__).

Note: there are attributes getattr can pull (dynamically created ones, say) that this function might miss, and there are attributes getattr cannot reach (descriptors that throw AttributeError, for instance) that it may turn up. On top of that, it can give back descriptor objects in place of instance members.

Where some other member (a property, say) masks the instance [`__dict__`](https://docs.python.org/3.14/reference/datamodel.html#object.__dict__), this function won’t manage to locate instance members.

Added in version 3.2.

`getattr_static()` leaves descriptors unresolved — slot descriptors and getset descriptors on objects coded in C, to name two. You receive the descriptor object rather than the attribute beneath it.

Code along the lines below lets you deal with them. Bear in mind that calling into arbitrary getset descriptors can set code running:

```python
# example code for resolving the builtin descriptor types
class _foo:
    __slots__ = ['foo']

slot_descriptor = type(_foo.foo)
getset_descriptor = type(type(open(__file__)).name)
wrapper_descriptor = type(str.__dict__['__add__'])
descriptor_types = (slot_descriptor, getset_descriptor, wrapper_descriptor)

result = getattr_static(some_object, 'foo')
if type(result) in descriptor_types:
    try:
        result = result.__get__()
    except AttributeError:
        # descriptors can raise AttributeError to
        # indicate there is no underlying value
        # in which case the descriptor itself will
        # have to do
        pass

```

[Subject index](INDEX.md) · [Previous](inspect-getinnerframes-to-inspect-trace.md) · [Continue](inspect-getgeneratorstate-to-inspect-getasyncgenstate.md) · [Owning module, declaration or section: inspect](inspect-inspect-live-objects.md)
