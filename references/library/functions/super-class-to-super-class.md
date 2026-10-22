# Built-in Functions

*class *super

 *class *super(*type*, *object_or_type=None*, */*)

Hand back a proxy object that forwards method calls to a parent or sibling class of *type*. This comes in handy for getting at inherited methods that a class has overridden.

Whatever you pass as *object_or_type* sets the [method resolution order](https://docs.python.org/3.14/glossary.html#term-method-resolution-order) that gets searched. That search kicks off at the class immediately following *type*.

As an illustration, suppose the [`__mro__`](https://docs.python.org/3.14/reference/datamodel.html#type.__mro__) of *object_or_type* runs `D -> B -> C -> A -> object` and *type* holds `B`; then `super()` searches `C -> A -> object`.

The [`__mro__`](https://docs.python.org/3.14/reference/datamodel.html#type.__mro__) attribute on the class tied to *object_or_type* spells out the method resolution search order that both `getattr()` and `super()` follow. That attribute is dynamic and may shift any time the inheritance hierarchy gets revised.

Leave out the second argument and the super object you get back is unbound. Pass an object as the second argument and `isinstance(obj, type)` has to hold. Pass a type as the second argument and `issubclass(type2, type)` has to hold (which serves classmethods well).

Invoking it straight inside an ordinary method of a class lets you drop both arguments ("zero-argument `super()`"). Then *type* becomes the enclosing class, and *obj* becomes the first argument of the function wrapped most immediately around it (usually `self`). (Consequently, zero-argument `super()` won't behave as you'd want inside nested functions, generator expressions included, which quietly produce nested functions.)

*super* lends itself to two standard scenarios. Within a single-inheritance class hierarchy, *super* lets you point at parent classes without spelling out their names, which keeps the code easier to maintain. This usage tracks closely with how *super* works in other programming languages.

The other scenario backs cooperative multiple inheritance inside a dynamic execution environment. That scenario belongs to Python alone — you won't see it in statically compiled languages or in ones that permit single inheritance only. It opens the door to "diamond diagrams," where several base classes each define the same method. Sound design demands that those implementations share one calling signature throughout (since the call order is settled at runtime, since that order adapts as the class hierarchy shifts, and since that order may take in sibling classes that weren't known ahead of runtime).

In either scenario, a standard superclass call reads like this:

```python
class C(B):
    def method(self, arg):
        super().method(arg)    # This does the same thing as:
                               # super(C, self).method(arg)

```

Beyond method lookups, `super()` serves attribute lookups too. One scenario for this is reaching [descriptors](https://docs.python.org/3.14/glossary.html#term-descriptor) in a parent or sibling class.

Keep in mind that `super()` is built as a piece of the binding mechanism for explicit dotted attribute lookups such as `super().__getitem__(name)`. It manages that by furnishing its own [`__getattribute__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getattribute__) method that walks classes in a predictable order suited to cooperative multiple inheritance. For that reason, `super()` has no defined behavior for implicit lookups through statements or operators such as `super()[name]`.

Bear in mind too that, the zero argument form aside, `super()` may be used outside methods. The two argument form pins down the arguments precisely and builds the right references. The zero argument form functions solely inside a class definition, because the compiler supplies the details needed to correctly fetch the class under construction, as well as to reach the current instance for ordinary methods.

For hands-on advice on building cooperative classes with `super()`, consult the [guide to using super()](https://rhettinger.wordpress.com/2011/05/26/super-considered-super/).

Changed in version 3.14: A `super` object can now be [`pickleable`](https://docs.python.org/3.14/library/pickle.html#module-pickle) as well as [`copyable`](https://docs.python.org/3.14/library/copy.html#module-copy).

[Subject index](INDEX.md) · [Previous](sum.md) · [Continue](tuple-class.md) · [Owning module, declaration or section: Built-in Functions](INDEX.md)
