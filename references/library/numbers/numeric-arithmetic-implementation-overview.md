# numbers — Implementing the arithmetic operations — Section introduction and initial examples

### Implementing the arithmetic operations

The goal in coding the arithmetic operations is for a mixed-mode operation to land on an implementation written by someone aware of both argument types, or else to promote both operands to the closest built-in type and carry out the work there. Within subtypes of `Integral`, that translates into defining [`__add__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__add__) and [`__radd__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__radd__) like so:

```python
class MyIntegral(Integral):

    def __add__(self, other):
        if isinstance(other, MyIntegral):
            return do_my_adding_stuff(self, other)
        elif isinstance(other, OtherTypeIKnowAbout):
            return do_my_other_adding_stuff(self, other)
        else:
            return NotImplemented

    def __radd__(self, other):
        if isinstance(other, MyIntegral):
            return do_my_adding_stuff(other, self)
        elif isinstance(other, OtherTypeIKnowAbout):
            return do_my_other_adding_stuff(other, self)
        elif isinstance(other, Integral):
            return int(other) + int(self)
        elif isinstance(other, Real):
            return float(other) + float(self)
        elif isinstance(other, Complex):
            return complex(other) + complex(self)
        else:
            return NotImplemented

```

A mixed-type operation across subclasses of `Complex` breaks down into 5 separate cases. Everything in the code above that does not mention `MyIntegral` or `OtherTypeIKnowAbout` I will call “boilerplate”. Take `a` as an instance of `A`, itself a subtype of `Complex` (`a : A <: Complex`), and `b : B <: Complex`. Look at `a + b`:

1.

Should `A` provide an [`__add__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__add__) that takes `b`, everything is fine.

2.

Were `A` to drop into the boilerplate and return something from [`__add__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__add__), we would overlook that `B` might have a smarter [`__radd__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__radd__); hence the boilerplate ought to give back [`NotImplemented`](https://docs.python.org/3.14/library/constants.html#NotImplemented) out of `__add__()`. (Alternatively `A` need not define `__add__()` whatsoever.)

3.

Next, the [`__radd__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__radd__) belonging to `B` is given its turn. Provided it takes `a`, everything is fine.

4.

If it too retreats to the boilerplate, no further methods remain to attempt, which makes this the spot for the default implementation to reside.

5.

When `B <: A`, Python reaches for `B.__radd__` ahead of `A.__add__`. That is acceptable, since it was built knowing about `A` and can therefore deal with such instances before handing off to `Complex`.

Where `A <: Complex` and `B <: Real` share nothing more between them, the fitting common operation is the one going through the built-in [`complex`](https://docs.python.org/3.14/library/functions.html#complex), and both of the [`__radd__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__radd__) s settle there, giving `a+b == b+a`.

Since the bulk of the operations on a particular type will look much alike, a helper function that churns out both the forward and reverse forms of any operator can come in handy. As one example, [`fractions.Fraction`](https://docs.python.org/3.14/library/fractions.html#fractions.Fraction) employs:

[Subject index](INDEX.md) · [Previous](adding-more-numeric-abcs.md) · [Continue](numbers-and-fallback-operator.md) · [Owning module, declaration or section: numbers](numbers-number-class.md)
