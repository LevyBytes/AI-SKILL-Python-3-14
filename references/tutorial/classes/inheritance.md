# 9.5. Inheritance

### 9.5. Inheritance

Naturally, no language feature could truly earn the name "class" without offering inheritance. The syntax used to define a derived class is as follows:

```python
class DerivedClassName(BaseClassName):
    <statement-1>
    .
    .
    .
    <statement-N>

```

The name `BaseClassName` has to be defined within a namespace that the scope holding the derived class definition can reach. Instead of a base class name, you may also write other arbitrary expressions. That can come in handy, for example, when the base class lives in a different module:

```python
class DerivedClassName(modname.BaseClassName):

```

Carrying out a derived class definition unfolds just the way it does for a base class. As the class object gets built, the base class is kept in memory. This serves to resolve attribute references: when a sought-after attribute can't be found within the class, the search moves on to the base class. The rule applies recursively if the base class is itself derived from yet another class.

Creating an instance of a derived class works no differently from any other: `DerivedClassName()` produces a fresh instance of that class. A method reference resolves like so — the matching class attribute is looked up, walking down the line of base classes when needed, and the reference holds good provided that lookup turns up a function object.

A derived class is free to override the methods it inherits from its base classes. Since a method enjoys no special standing when it calls another method on the same object, a base-class method that invokes a second method declared in that same base class can wind up landing on a derived-class method that has overridden it. (For C++ programmers: every Python method is, in effect, `virtual`.)

Often an overriding method in a derived class wants to build on, rather than wholly swap out, the base-class method of the same name. Calling the base-class method directly is straightforward: simply call `BaseClassName.methodname(self, arguments)`. Clients occasionally find this handy too. (Bear in mind it only works when the base class is reachable as `BaseClassName` in the global scope.)

Two built-in functions in Python deal with inheritance:

- Reach for [`isinstance()`](https://docs.python.org/3.14/library/functions.html#isinstance) to test an instance’s type: `isinstance(obj, int)` comes back `True` solely when `obj.__class__` is [`int`](https://docs.python.org/3.14/library/functions.html#int) or any class descended from `int`.

- Reach for [`issubclass()`](https://docs.python.org/3.14/library/functions.html#issubclass) to test class inheritance: `issubclass(bool, int)` yields `True`, given that [`bool`](https://docs.python.org/3.14/library/functions.html#bool) derives from [`int`](https://docs.python.org/3.14/library/functions.html#int). By contrast `issubclass(float, int)` yields `False`, since [`float`](https://docs.python.org/3.14/library/functions.html#float) does not derive from `int`.

[Subject index](INDEX.md) · [Previous source section](random-remarks.md) · [Following source section](multiple-inheritance.md)
