# What’s New in Python 2.2 / Multiple Inheritance: The Diamond Rule

### Multiple Inheritance: The Diamond Rule

Multiple inheritance has been rendered handier as well, by reworking the rules that govern how names get resolved. Take this collection of classes (the diagram is lifted from [**PEP 253**](https://peps.python.org/pep-0253/) by Guido van Rossum):

```python
      class A:
        ^ ^  def save(self): ...
       /   \
      /     \
     /       \
    /         \
class B     class C:
    ^         ^  def save(self): ...
     \       /
      \     /
       \   /
        \ /
      class D

```

For classic classes the lookup rule is straightforward yet none too clever; base classes get walked depth-first, moving left to right. Referencing `D.save()` will hunt through classes `D`, `B`, and then `A`, where `save()` turns up and gets returned. `C.save()` would never be reached at all. That’s a problem, since if `C`’s `save()` method is stashing some internal state unique to `C`, skipping the call means that state never gets stashed.

New-style classes use a different algorithm — a touch harder to lay out, but it behaves correctly here. (Be aware that Python 2.3 swaps this algorithm for one that yields identical results in most situations, while delivering better results for truly tangled inheritance graphs.)

1.

Enumerate every base class by walking the classic lookup rule, including a class more than once whenever it’s revisited. For the example above, the roster of visited classes reads [`D`, `B`, `A`, `C`, `A`].

2.

Comb the list for repeated classes. Where any turn up, strip out all but a single occurrence, keeping the *last* one in the list. For the example above, once duplicates are removed the list becomes [`D`, `B`, `C`, `A`].

By this rule, a reference to `D.save()` ends up returning `C.save()`, which is the behaviour we wanted. That lookup rule matches the one Common Lisp uses. A fresh built-in function, [`super()`](https://docs.python.org/3.14/library/functions.html#super), gives you a route to a class’s superclasses without re-coding Python’s algorithm. The form you’ll reach for most often is `super(class, obj)`, which yields a bound superclass object (not the genuine class object). You’ll use this form within methods to invoke a method on the superclass; for instance, `D`’s `save()` method would read like this:

```python
class D (B,C):
    def save (self):
        # Call superclass .save()
        super(D, self).save()
        # Save D's private information here
        ...

```

[`super()`](https://docs.python.org/3.14/library/functions.html#super) is also able to give back unbound superclass objects when invoked as `super(class)` or `super(class1, class2)`, though that likely won’t prove useful all that often.

[Subject index](INDEX.md) · [Previous source section](descriptors.md) · [Next source section](attribute-access.md) · [Release/subject declaration](introduction.md)
