# 3.3.3. Customizing class creation

### 3.3.3. Customizing class creation

Each time a class inherits from a different class, `__init_subclass__()` runs on that parent class. This makes it possible to author classes that alter how their subclasses behave. The mechanism is a close cousin of class decorators, except that class decorators touch only the one class they decorate, whereas `__init_subclass__` applies exclusively to subclasses created later from the class that defines the method.

 *classmethod *object.__init_subclass__(*cls*)

Invoked every time the enclosing class is subclassed. Here *cls* refers to the new subclass. When written as an ordinary instance method, this method is implicitly turned into a class method.

The keyword arguments handed to a new class are forwarded to the parent class's `__init_subclass__`. To stay compatible with other classes that also use `__init_subclass__`, you should pull off the keyword arguments you require and forward the rest to the base class, like this:

```python
class Philosopher:
    def __init_subclass__(cls, /, default_name, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.default_name = default_name

class AustralianPhilosopher(Philosopher, default_name="Bruce"):
    pass

```

The default `object.__init_subclass__` is a no-op, except that it raises an error whenever it receives any arguments.

Note

The `metaclass` hint is consumed by the remainder of the type machinery and is never handed to `__init_subclass__` implementations. The real metaclass (as opposed to the explicit hint) is reachable via `type(cls)`.

Added in version 3.6.

As a class is built, `type.__new__()` walks over the class variables and triggers callbacks on any that carry a `__set_name__()` hook.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](special-method-names.md) · [Previous source section](object-slots.md) · [Following source section](object-set-name.md)
