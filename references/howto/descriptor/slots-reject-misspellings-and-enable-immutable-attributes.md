# Slots reject misspellings and enable immutable attributes

### Member objects and __slots__

Defining `__slots__` on a class swaps out instance dictionaries for a fixed-length array holding the slot values. From the user's perspective this produces a few consequences:

1. Catches bugs from misspelled attribute assignments right away. The only attribute names permitted are those listed in `__slots__`:

```python
class Vehicle:
    __slots__ = ('id_number', 'make', 'model')

```

```pycon
>>> auto = Vehicle()
>>> auto.id_nubmer = 'VYE483814LQEX'
Traceback (most recent call last):
    ...
AttributeError: 'Vehicle' object has no attribute 'id_nubmer'

```

2. Aids in producing immutable objects, where descriptors govern access to private attributes kept in `__slots__`:

```python
class Immutable:

    __slots__ = ('_dept', '_name')          # Replace the instance dictionary

    def __init__(self, dept, name):
        self._dept = dept                   # Store to private attribute
        self._name = name                   # Store to private attribute

    @property                               # Read-only descriptor
    def dept(self):
        return self._dept

    @property
    def name(self):                         # Read-only descriptor
        return self._name

```

```pycon
>>> mark = Immutable('Botany', 'Mark Watney')
>>> mark.dept
'Botany'
>>> mark.dept = 'Space Pirate'
Traceback (most recent call last):
    ...
AttributeError: property 'dept' of 'Immutable' object has no setter
>>> mark.location = 'Mars'
Traceback (most recent call last):
    ...
AttributeError: 'Immutable' object has no attribute 'location'

```

[Subject index](INDEX.md) · [Slots memory, speed and cached_property constraints](slots-memory-speed-and-cached-property-constraints.md) · [Member descriptor simulation and null sentinel](member-descriptor-simulation-and-null-sentinel.md) · [Type metaclass installs members and Object allocates slot storage](metaclass-members-and-object-slot-allocation.md) · [Using the complete slots simulation and inspecting failures](using-the-complete-slots-simulation-and-inspecting-failures.md) · [Previous source context](class-methods.md) · [Following source context](slots-memory-speed-and-cached-property-constraints.md)
