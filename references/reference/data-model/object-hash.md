# object.__hash__(*self*)

object.__hash__(*self*)

Invoked by the built-in function [`hash()`](https://docs.python.org/3.14/library/functions.html#hash) and for operations on members of hashed collections such as [`set`](https://docs.python.org/3.14/library/stdtypes.html#set), [`frozenset`](https://docs.python.org/3.14/library/stdtypes.html#frozenset), and [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict). The `__hash__()` method should return an integer. Its sole mandatory property is that objects comparing equal share an identical hash value; it is recommended to combine the hash values of the object’s components that also figure in object comparison by bundling them into a tuple and hashing that tuple. Example:

```python
def __hash__(self):
    return hash((self.name, self.nick, self.color))

```

Note

[`hash()`](https://docs.python.org/3.14/library/functions.html#hash) shortens the value coming back from an object’s custom `__hash__()` method down to the size of a [`Py_ssize_t`](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t). On 64-bit builds that is generally 8 bytes, dropping to 4 bytes for 32-bit builds. When an object’s `__hash__()` has to work across builds of differing bit widths, take care to verify the width on every supported build. A simple route is `python -c "import sys; print(sys.hash_info.width)"`.

Should a class skip defining an `__eq__()` method, it ought not define a `__hash__()` operation either; should it define `__eq__()` while skipping `__hash__()`, its instances will be unusable as items in hashable collections. Should a class define mutable objects and implement an `__eq__()` method, it ought not implement `__hash__()`, because the implementation of [hashable](https://docs.python.org/3.14/glossary.html#term-hashable) collections demands that a key’s hash value stay immutable (when the object’s hash value shifts, it ends up in the wrong hash bucket).

User-defined classes carry `__eq__()` and `__hash__()` methods by default (inherited from the [`object`](https://docs.python.org/3.14/library/functions.html#object) class); through them, every object compares unequal (apart from itself) and `x.__hash__()` produces a fitting value such that `x == y` entails both that `x is y` and `hash(x) == hash(y)`.

Any class that overrides `__eq__()` yet leaves `__hash__()` undefined will have its `__hash__()` implicitly set to `None`. Once a class’s `__hash__()` method is `None`, the class’s instances raise a fitting [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) the moment a program tries to fetch their hash value, and they are likewise correctly flagged as unhashable during an `isinstance(obj, collections.abc.Hashable)` check.

Should a class that overrides `__eq__()` need to keep the `__hash__()` implementation inherited from a parent class, the interpreter has to be informed of this directly by assigning `__hash__ = <ParentClass>.__hash__`.

Should a class that does not override `__eq__()` want to turn off hash support, it ought to add `__hash__ = None` within the class body. A class that defines its own `__hash__()` deliberately raising a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) would be wrongly flagged as hashable by an `isinstance(obj, collections.abc.Hashable)` call.

Note

By default, the `__hash__()` values for str and bytes objects are “salted” using an unpredictable random value. While they stay fixed inside one individual Python process, they cannot be predicted across separate runs of Python.

The purpose is to guard against a denial-of-service brought on by deliberately chosen inputs that take advantage of the worst-case performance of dict insertion, *O*(*n*2) complexity. Consult [https://ocert.org/advisories/ocert-2011-003.html](https://ocert.org/advisories/ocert-2011-003.html) for the details.

Altering hash values has an effect on the iteration order of sets. Python has never offered guarantees concerning this ordering (and it commonly differs between 32-bit and 64-bit builds).

Consult also [`PYTHONHASHSEED`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONHASHSEED).

Changed in version 3.3: Hash randomization is turned on by default.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](special-method-names.md) · [Owning language section](object-new.md) · [Previous source section](object-lt-object-le-object-eq-object-ne-object-gt-object-ge.md) · [Following source section](object-bool.md)
