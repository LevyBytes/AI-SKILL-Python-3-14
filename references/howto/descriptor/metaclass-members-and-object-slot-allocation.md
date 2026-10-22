# Type metaclass installs members and Object allocates slot storage

Attaching member objects to the class variables is handled by the `type.__new__()` method:

```python
class Type(type):
    'Simulate how the type metaclass adds member objects for slots'

    def __new__(mcls, clsname, bases, mapping, **kwargs):
        'Emulate type_new() in Objects/typeobject.c'
        # type_new() calls PyTypeReady() which calls add_methods()
        slot_names = mapping.get('slot_names', [])
        for offset, name in enumerate(slot_names):
            mapping[name] = Member(name, clsname, offset)
        return type.__new__(mcls, clsname, bases, mapping, **kwargs)

```

Producing instances that carry slots in place of an instance dictionary falls to the [`object.__new__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__new__) method. A rough pure Python simulation appears here:

```python
class Object:
    'Simulate how object.__new__() allocates memory for __slots__'

    def __new__(cls, *args, **kwargs):
        'Emulate object_new() in Objects/typeobject.c'
        inst = super().__new__(cls)
        if hasattr(cls, 'slot_names'):
            empty_slots = [null] * len(cls.slot_names)
            object.__setattr__(inst, '_slotvalues', empty_slots)
        return inst

    def __setattr__(self, name, value):
        'Emulate _PyObject_GenericSetAttrWithDict() Objects/object.c'
        cls = type(self)
        if hasattr(cls, 'slot_names') and name not in cls.slot_names:
            raise AttributeError(
                f'{cls.__name__!r} object has no attribute {name!r}'
            )
        super().__setattr__(name, value)

    def __delattr__(self, name):
        'Emulate _PyObject_GenericSetAttrWithDict() Objects/object.c'
        cls = type(self)
        if hasattr(cls, 'slot_names') and name not in cls.slot_names:
            raise AttributeError(
                f'{cls.__name__!r} object has no attribute {name!r}'
            )
        super().__delattr__(name)

```

[Subject index](INDEX.md) · [Slots reject misspellings and enable immutable attributes](slots-reject-misspellings-and-enable-immutable-attributes.md) · [Slots memory, speed and cached_property constraints](slots-memory-speed-and-cached-property-constraints.md) · [Member descriptor simulation and null sentinel](member-descriptor-simulation-and-null-sentinel.md) · [Using the complete slots simulation and inspecting failures](using-the-complete-slots-simulation-and-inspecting-failures.md) · [Previous source context](member-descriptor-simulation-and-null-sentinel.md) · [Following source context](using-the-complete-slots-simulation-and-inspecting-failures.md)
