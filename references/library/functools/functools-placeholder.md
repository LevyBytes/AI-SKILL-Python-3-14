# functools: `functools.total_ordering`, `functools.Placeholder`

@functools.total_ordering

Provided a class already defines at least one rich comparison ordering method, this class decorator fills in the others. That cuts down the work of writing out every possible rich comparison operation:

The class is required to define one among [`__lt__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__lt__), [`__le__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__le__), [`__gt__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__gt__), or [`__ge__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__ge__). On top of that, the class ought to provide an [`__eq__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__eq__) method.

For example:

```python
@total_ordering
class Student:
    def _is_valid_operand(self, other):
        return (hasattr(other, "lastname") and
                hasattr(other, "firstname"))
    def __eq__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return ((self.lastname.lower(), self.firstname.lower()) ==
                (other.lastname.lower(), other.firstname.lower()))
    def __lt__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return ((self.lastname.lower(), self.firstname.lower()) <
                (other.lastname.lower(), other.firstname.lower()))

```

Note

Although this decorator makes building well-behaved totally ordered types straightforward, it *does* carry a price: slower execution along with more tangled stack traces for the generated comparison methods. Should performance profiling flag this as a bottleneck for some application, writing out all six rich comparison methods by hand will likely deliver a quick speedup.

Note

This decorator won't try to replace methods already declared on the class *or its superclasses*. That is, when a superclass supplies a comparison operator, *total_ordering* leaves it alone rather than reimplementing it, even where the inherited method is abstract.

Added in version 3.2.

Changed in version 3.4: It is now permitted for the underlying comparison function to hand back `NotImplemented` when it meets unrecognised types.

 functools.Placeholder

A singleton object serving as a sentinel that holds open a slot for positional arguments when you call `partial()` and `partialmethod()`.

Added in version 3.14.

[Subject index](INDEX.md) · [Previous](cache-vowel-pep-and-fibonacci-examples.md) · [Continue](functools-partial.md) · [Owning module, declaration or section: functools](cached-factorial-and-dataset-examples.md)
