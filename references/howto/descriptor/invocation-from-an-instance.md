# Invocation from an instance

### Invocation from an instance

Instance lookup walks a chain of namespaces, ranking data descriptors first, then instance variables, then non-data descriptors, then class variables, and finally [`__getattr__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getattr__) when one is supplied.

When a descriptor turns up for `a.x`, it is called as: `desc.__get__(a, type(a))`.

The dotted-lookup logic resides in [`object.__getattribute__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getattribute__). What follows is a pure Python equivalent:

```python
def find_name_in_mro(cls, name, default):
    "Emulate _PyType_Lookup() in Objects/typeobject.c"
    for base in cls.__mro__:
        if name in vars(base):
            return vars(base)[name]
    return default

def object_getattribute(obj, name):
    "Emulate PyObject_GenericGetAttr() in Objects/object.c"
    null = object()
    objtype = type(obj)
    cls_var = find_name_in_mro(objtype, name, null)
    descr_get = getattr(type(cls_var), '__get__', null)
    if descr_get is not null:
        if (hasattr(type(cls_var), '__set__')
            or hasattr(type(cls_var), '__delete__')):
            return descr_get(cls_var, obj, objtype)     # data descriptor
    if hasattr(obj, '__dict__') and name in vars(obj):
        return vars(obj)[name]                          # instance variable
    if descr_get is not null:
        return descr_get(cls_var, obj, objtype)         # non-data descriptor
    if cls_var is not null:
        return cls_var                                  # class variable
    raise AttributeError(name)

```

Note that the [`__getattribute__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getattribute__) code contains no [`__getattr__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getattr__) hook. For that reason, calling `__getattribute__()` directly, or through `super().__getattribute__`, skips `__getattr__()` completely.

Rather, the responsibility for invoking [`__getattr__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getattr__) — whenever [`__getattribute__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getattribute__) throws an [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError) — falls to the dot operator and the [`getattr()`](https://docs.python.org/3.14/library/functions.html#getattr) function. A helper function captures their logic:

```python
def getattr_hook(obj, name):
    "Emulate slot_tp_getattr_hook() in Objects/typeobject.c"
    try:
        return obj.__getattribute__(name)
    except AttributeError:
        if not hasattr(type(obj), '__getattr__'):
            raise
    return type(obj).__getattr__(obj, name)             # __getattr__

```

[Subject index](INDEX.md) · [Previous source context](overview-of-descriptor-invocation.md) · [Following source context](invocation-from-a-class.md)
