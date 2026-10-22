# 8.8. Class definitions

### 8.8. Class definitions

A class definition defines a class object (see section [The standard type hierarchy](https://docs.python.org/3.14/reference/datamodel.html#types)):

```text

classdef:    [decorators] "class" classname [type_params] [inheritance] ":" suite
inheritance: "(" [argument_list] ")"
classname:   identifier
```

A class definition counts as an executable statement. Its inheritance list typically names a set of base classes (consult [Metaclasses](https://docs.python.org/3.14/reference/datamodel.html#metaclasses) for more advanced patterns), so every entry in that list ought to evaluate to a class object that permits subclassing. A class given no inheritance list inherits by default from the base class [`object`](https://docs.python.org/3.14/library/functions.html#object); thus,

```python
class Foo:
    pass

```

is equivalent to

```python
class Foo(object):
    pass

```

Next, the class’s suite runs inside a freshly made execution frame (see [Naming and binding](https://docs.python.org/3.14/reference/executionmodel.html#naming)), with a newly created local namespace and the original global namespace. (Most often the suite holds chiefly function definitions.) Once the class’s suite has finished running, its execution frame goes away, though its local namespace is retained. [5] The interpreter then builds a class object from the inheritance list, taken as the base classes, together with the retained local namespace, taken as the attribute dictionary. Finally the class name is bound to that class object within the original local namespace.

The sequence in which attributes get defined in the class body is kept intact in the new class’s [`__dict__`](https://docs.python.org/3.14/reference/datamodel.html#type.__dict__). Bear in mind this holds true only immediately after the class is built and only for classes declared through the definition syntax.

Class creation can be customized heavily using [metaclasses](https://docs.python.org/3.14/reference/datamodel.html#metaclasses).

Classes admit decoration too: much as with decorating functions,

```python
@f1(arg)
@f2
class Foo: pass

```

is roughly equivalent to

```python
class Foo: pass
Foo = f1(arg)(f2(Foo))

```

Decorator expressions follow the very same evaluation rules that apply to function decorators. The outcome is then bound to the class name.

Changed in version 3.9: Any valid [`assignment_expression`](https://docs.python.org/3.14/reference/expressions.html#grammar-token-python-grammar-assignment_expression) is now allowed as a class decorator. The grammar used to be far stricter; consult [**PEP 614**](https://peps.python.org/pep-0614/) for details.

You may supply a list of type parameters in square brackets placed right after the class’s name. Doing so signals to static type checkers that the class is generic. While running, those type parameters are obtainable from the class’s [`__type_params__`](https://docs.python.org/3.14/reference/datamodel.html#type.__type_params__) attribute. See Generic classes for more.

Changed in version 3.12: Python 3.12 introduced type parameter lists.

**Programmer’s note:** Variables declared within the class definition are class attributes, shared across instances. An instance attribute can be assigned in a method with `self.name = value`. Both kinds of attribute — class and instance — are reachable through the “`self.name`” notation, and when accessed that way an instance attribute conceals a class attribute bearing the same name. Class attributes can serve as defaults for instance attributes, yet placing mutable values there can produce surprising behavior. [Descriptors](https://docs.python.org/3.14/reference/datamodel.html#descriptors) can be used to create instance variables with different implementation details.

See also

[**PEP 3115**](https://peps.python.org/pep-3115/) - Metaclasses in Python 3000

The proposal that moved metaclass declaration to today’s syntax and set out how classes that use metaclasses get built.

[**PEP 3129**](https://peps.python.org/pep-3129/) - Class Decorators

The proposal that brought in class decorators. Decorators for functions and methods had earlier arrived in [**PEP 318**](https://peps.python.org/pep-0318/).

[Subject index](INDEX.md) · [Owning language section](compound-statements.md) · [Previous source section](function-definitions-whats-on-the-telly.md) · [Following source section](coroutine-function-definition.md)
