# Slots memory, speed and cached_property constraints

3. Conserves memory. Under a 64-bit Linux build, an instance carrying two attributes occupies 48 bytes when `__slots__` is used and 152 bytes when it is not. This [flyweight design pattern](https://en.wikipedia.org/wiki/Flyweight_pattern) probably matters only where you expect to create a great many instances.

4. Boosts speed. With `__slots__`, reading an instance variable runs 35% faster (as benchmarked under Python 3.10 on an Apple M1 processor).

5. Prevents tools such as [`functools.cached_property()`](https://docs.python.org/3.14/library/functools.html#functools.cached_property), which depend on an instance dictionary to operate correctly:

```python
from functools import cached_property

class CP:
    __slots__ = ()                          # Eliminates the instance dict

    @cached_property                        # Requires an instance dict
    def pi(self):
        return 4 * sum((-1.0)**n / (2.0*n + 1.0)
                       for n in reversed(range(100_000)))

```

```pycon
>>> CP().pi
Traceback (most recent call last):
  ...
TypeError: No '__dict__' attribute on 'CP' instance to cache 'pi' property.

```

[Subject index](INDEX.md) · [Slots reject misspellings and enable immutable attributes](slots-reject-misspellings-and-enable-immutable-attributes.md) · [Member descriptor simulation and null sentinel](member-descriptor-simulation-and-null-sentinel.md) · [Type metaclass installs members and Object allocates slot storage](metaclass-members-and-object-slot-allocation.md) · [Using the complete slots simulation and inspecting failures](using-the-complete-slots-simulation-and-inspecting-failures.md) · [Previous source context](slots-reject-misspellings-and-enable-immutable-attributes.md) · [Following source context](member-descriptor-simulation-and-null-sentinel.md)
