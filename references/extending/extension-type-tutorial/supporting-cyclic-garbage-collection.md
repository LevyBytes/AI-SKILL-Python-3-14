# Supporting cyclic garbage collection

### 2.4. Supporting cyclic garbage collection

A [cyclic garbage collector (GC)](https://docs.python.org/3.14/glossary.html#term-garbage-collection) ships with Python and is able to spot objects no longer required even while their reference counts remain above zero. Such situations arise when objects form cycles. Take this case for instance:

```pycon
>>> l = []
>>> l.append(l)
>>> del l

```

What we do here is build a list referring to itself. Once deleted, a reference to it still lingers from within itself. Therefore its reference count never reaches zero. Happily, Python's cyclic garbage collector will in time recognize the list as garbage and reclaim it.

Back in the `Custom` example's second iteration, any sort of object was permitted in the `first` or `last` attributes [4]. Furthermore, the second and third iterations permitted subclassing `Custom`, and a subclass might tack on arbitrary attributes. Either of these two situations means `Custom` objects can become part of cycles:

```pycon
>>> import custom3
>>> class Derived(custom3.Custom): pass
...
>>> n = Derived()
>>> n.some_attribute = n

```

So that a `Custom` instance caught in a reference cycle gets correctly identified and reclaimed by the cyclic GC, our `Custom` type has to populate two extra slots and switch on a flag that activates those slots:

[Subject index](INDEX.md) · [Previous source section](providing-finer-control-over-data-attributes-and-tp-new.md) · [Next source section](supporting-cyclic-garbage-collection-and-custom-init.md)
