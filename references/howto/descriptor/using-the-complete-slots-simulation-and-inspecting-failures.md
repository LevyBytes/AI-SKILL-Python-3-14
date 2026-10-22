# Using the complete slots simulation and inspecting failures

To put the simulation to work in an actual class, simply derive from `Object` and assign the [metaclass](https://docs.python.org/3.14/glossary.html#term-metaclass) as `Type`:

```python
class H(Object, metaclass=Type):
    'Instance variables stored in slots'

    slot_names = ['x', 'y']

    def __init__(self, x, y):
        self.x = x
        self.y = y

```

By now the metaclass has installed member objects for *x* and *y*:

```python
>>> from pprint import pp
>>> pp(dict(vars(H)))
{'__module__': '__main__',
 '__doc__': 'Instance variables stored in slots',
 'slot_names': ['x', 'y'],
 '__init__': <function H.__init__ at 0x7fb5d302f9d0>,
 'x': <Member 'x' of 'H'>,
 'y': <Member 'y' of 'H'>}

```

Each instance that gets created comes with a `slot_values` list in which its attributes live:

```pycon
>>> h = H(10, 20)
>>> vars(h)
{'_slotvalues': [10, 20]}
>>> h.x = 55
>>> vars(h)
{'_slotvalues': [55, 20]}

```

An exception is raised by misspelled or unassigned attributes:

```pycon
>>> h.xz
Traceback (most recent call last):
    ...
AttributeError: 'H' object has no attribute 'xz'

```

[Subject index](INDEX.md) · [Slots reject misspellings and enable immutable attributes](slots-reject-misspellings-and-enable-immutable-attributes.md) · [Slots memory, speed and cached_property constraints](slots-memory-speed-and-cached-property-constraints.md) · [Member descriptor simulation and null sentinel](member-descriptor-simulation-and-null-sentinel.md) · [Type metaclass installs members and Object allocates slot storage](metaclass-members-and-object-slot-allocation.md) · [Previous source context](metaclass-members-and-object-slot-allocation.md)
