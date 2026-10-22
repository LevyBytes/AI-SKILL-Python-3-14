# Member descriptor simulation and null sentinel

A truly exact drop-in pure Python version of `__slots__` is out of reach, since the feature relies on direct access to C structures together with control over how object memory gets allocated. That said, we can put together a largely faithful simulation in which a private `_slotvalues` list stands in for the real C structure backing the slots. Member descriptors govern the reads and writes to that private structure:

```python
null = object()

class Member:

    def __init__(self, name, clsname, offset):
        'Emulate PyMemberDef in Include/descrobject.h'
        # Also see descr_new() in Objects/descrobject.c
        self.name = name
        self.clsname = clsname
        self.offset = offset

    def __get__(self, obj, objtype=None):
        'Emulate member_get() in Objects/descrobject.c'
        # Also see PyMember_GetOne() in Python/structmember.c
        if obj is None:
            return self
        value = obj._slotvalues[self.offset]
        if value is null:
            raise AttributeError(self.name)
        return value

    def __set__(self, obj, value):
        'Emulate member_set() in Objects/descrobject.c'
        obj._slotvalues[self.offset] = value

    def __delete__(self, obj):
        'Emulate member_delete() in Objects/descrobject.c'
        value = obj._slotvalues[self.offset]
        if value is null:
            raise AttributeError(self.name)
        obj._slotvalues[self.offset] = null

    def __repr__(self):
        'Emulate member_repr() in Objects/descrobject.c'
        return f'<Member {self.name!r} of {self.clsname!r}>'

```

[Subject index](INDEX.md) · [Slots reject misspellings and enable immutable attributes](slots-reject-misspellings-and-enable-immutable-attributes.md) · [Slots memory, speed and cached_property constraints](slots-memory-speed-and-cached-property-constraints.md) · [Type metaclass installs members and Object allocates slot storage](metaclass-members-and-object-slot-allocation.md) · [Using the complete slots simulation and inspecting failures](using-the-complete-slots-simulation-and-inspecting-failures.md) · [Previous source context](slots-memory-speed-and-cached-property-constraints.md) · [Following source context](metaclass-members-and-object-slot-allocation.md)
