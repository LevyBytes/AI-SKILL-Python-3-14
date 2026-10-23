# weakref - Example

### Example

This small example shows how an application can lean on object IDs to fetch back objects it has run across before. Those object IDs can then live in other data structures without compelling the objects to stay alive, yet whenever the objects are still around they remain fetchable by ID.

```python
import weakref

_id2obj_dict = weakref.WeakValueDictionary()

def remember(obj):
    oid = id(obj)
    _id2obj_dict[oid] = obj
    return oid

def id2obj(oid):
    return _id2obj_dict[oid]

```

[Subject index](INDEX.md) · [Previous](weak-reference-objects.md) · [Continue](finalizer-objects.md) · [Owning module, declaration or section: weakref](weakref-ref-class.md)
