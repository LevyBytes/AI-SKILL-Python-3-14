# 3.3.2.3. Invoking Descriptors

#### 3.3.2.3. Invoking Descriptors

Broadly, a descriptor is an object attribute exhibiting “binding behavior”, one whose attribute access has been overridden by methods within the descriptor protocol: `__get__()`, `__set__()`, and `__delete__()`. When any of those methods are defined for an object, that object is called a descriptor.

The default behavior for attribute access is to fetch, set, or delete the attribute from an object’s dictionary. For example, `a.x` carries a lookup chain that opens with `a.__dict__['x']`, then `type(a).__dict__['x']`, and proceeds through the base classes of `type(a)` while leaving out metaclasses.

Yet should the looked-up value be an object defining one of the descriptor methods, then Python may supersede the default behavior and invoke the descriptor method in its place. Where this happens within the precedence chain hinges on which descriptor methods were defined and how they were invoked.

The departure point for descriptor invocation is a binding, `a.x`. How the arguments are gathered hinges on `a`:

Direct Call

The simplest and rarest call arises when user code invokes a descriptor method directly: `x.__get__(a)`.

Instance Binding

When binding to an object instance, `a.x` is converted into the call: `type(a).__dict__['x'].__get__(a, type(a))`.

Class Binding

When binding to a class, `A.x` is converted into the call: `A.__dict__['x'].__get__(None, A)`.

Super Binding

A dotted lookup like `super(A, a).x` scans `a.__class__.__mro__` for a base class `B` coming after `A` and then gives back `B.__dict__['x'].__get__(a, A)`. Where `x` is not a descriptor, it is given back unchanged.

For instance bindings, the precedence of descriptor invocation hinges on which descriptor methods are defined. A descriptor may define any mix of `__get__()`, `__set__()` and `__delete__()`. Should it leave `__get__()` undefined, then accessing the attribute returns the descriptor object itself unless a value sits in the object’s instance dictionary. Should the descriptor define `__set__()` and/or `__delete__()`, it is a data descriptor; should it define neither, it is a non-data descriptor. Typically, data descriptors define both `__get__()` and `__set__()`, while non-data descriptors hold just the `__get__()` method. Data descriptors with `__get__()` and `__set__()` (and/or `__delete__()`) defined always supersede a redefinition within an instance dictionary. By contrast, non-data descriptors can be superseded by instances.

Python methods (those decorated with [`@staticmethod`](https://docs.python.org/3.14/library/functions.html#staticmethod) and [`@classmethod`](https://docs.python.org/3.14/library/functions.html#classmethod) included) are realized as non-data descriptors. Consequently, instances can redefine and supersede methods. This lets individual instances pick up behaviors departing from other instances of the same class.

The [`property()`](https://docs.python.org/3.14/library/functions.html#property) function is realized as a data descriptor. Consequently, instances cannot supersede the behavior of a property.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](special-method-names.md) · [Owning language section](customizing-attribute-access.md) · [Previous source section](object-objclass.md) · [Following source section](slots.md)
