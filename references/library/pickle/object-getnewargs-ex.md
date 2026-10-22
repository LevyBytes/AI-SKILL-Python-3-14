# pickle: `object.__getnewargs_ex__()`

### Pickling Class Instances

This section describes the general mechanisms at your disposal for defining, customizing, and controlling how class instances are pickled and unpickled.

In most cases no extra code is needed to make instances picklable. By default, pickle uses introspection to fetch the class and the attributes of an instance. When a class instance is unpickled, its [`__init__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__init__) method is generally *not* run. The default behaviour first builds an uninitialized instance and then restores the saved attributes. The code below shows an implementation of this behaviour:

```python
def save(obj):
    return (obj.__class__, obj.__dict__)

def restore(cls, attributes):
    obj = cls.__new__(cls)
    obj.__dict__.update(attributes)
    return obj

```

A class can override the default behaviour by supplying one or more of these special methods:

 object.__getnewargs_ex__()

[Subject index](INDEX.md) · [Previous](what-can-be-pickled-and-unpickled.md) · [Owning module, declaration or section: pickle](pickle-python-object-serialization.md) · [Required continuation of the source contract](object-getnewargs-to-object-setstate.md)
