# 9.5.1. Multiple Inheritance

### 9.5.1. Multiple Inheritance

A flavor of multiple inheritance is supported by Python as well. A class declaration that names several base classes takes this shape:

```python
class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>

```

In the most basic cases, and for nearly all intents, you can picture the hunt for attributes inherited from a parent as depth-first and left-to-right, never revisiting the same class where the hierarchy overlaps. So when an attribute isn’t turned up in `DerivedClassName`, the lookup moves to `Base1`, then (recursively) into the base classes of `Base1`; failing there it tries `Base2`, and onward in that fashion.

The reality is a touch more involved than that: the method resolution order shifts dynamically so that cooperative calls to [`super()`](https://docs.python.org/3.14/library/functions.html#super) work. Certain other multiple-inheritance languages dub this scheme call-next-method, and it outdoes the super call you’d find in single-inheritance languages.

Such dynamic ordering can’t be avoided, because every instance of multiple inheritance shows at least one diamond relationship (where some parent class is reachable by more than one path from the class at the bottom). Take [`object`](https://docs.python.org/3.14/library/functions.html#object), which every class inherits from — so any multiple-inheritance case yields several routes back to `object`. So that no base class is reached twice, the dynamic algorithm flattens the lookup order while honoring the left-to-right sequence each class specifies, visiting every parent a single time, and staying monotonic (which is to say a class can gain a subclass without disturbing the precedence order of its parents). Together these traits let you craft dependable, extensible classes under multiple inheritance. The deeper write-up is at [The Python 2.3 Method Resolution Order](https://docs.python.org/3.14/howto/mro.html#python-2-3-mro).

[Subject index](INDEX.md) · [Previous source section](inheritance.md) · [Following source section](private-variables.md)
