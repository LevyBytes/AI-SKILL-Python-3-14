# What’s New in Python 2.6 / Other Language Changes — math

```python
class C(object):
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x

class D(C):
    @C.x.getter
    def x(self):
        return self._x * 2

    @x.setter
    def x(self, value):
        self._x = value / 2

```

- A number of the built-in set type’s methods now take several iterables: `intersection()`, `intersection_update()`, `union()`, `update()`, `difference()` and `difference_update()`.

```python
>>> s=set('1234567890')
>>> s.intersection('abc123', 'cdf246')  # Intersection between all inputs
set(['2'])
>>> s.difference('246', '789')
set(['1', '0', '3', '5'])

```

(Contributed by Raymond Hettinger.)

- A range of floating-point capabilities arrived. The [`float()`](https://docs.python.org/3.14/library/functions.html#float) function now maps the string `nan` to an IEEE 754 Not A Number value; likewise `+inf` becomes positive infinity and `-inf` becomes negative infinity. It does so on any platform whose semantics follow IEEE 754. (Contributed by Christian Heimes; [bpo-1635](https://bugs.python.org/issue?@action=redirect&bpo=1635).)

The [`math`](https://docs.python.org/3.14/library/math.html#module-math) module also picks up `isinf()` and `isnan()`, which report true when their floating-point argument is infinite or Not A Number respectively. ([bpo-1640](https://bugs.python.org/issue?@action=redirect&bpo=1640))

New conversion functions turn floating-point numbers into hexadecimal strings ([bpo-3008](https://bugs.python.org/issue?@action=redirect&bpo=3008)). They move floats to and from a string form while avoiding the rounding errors that arise in decimal-to-binary conversion. Floats get a [`hex()`](https://docs.python.org/3.14/library/functions.html#hex) method that produces such a string form, and the `float.fromhex()` method turns a string back into a number:

```python
>>> a = 3.75
>>> a.hex()
'0x1.e000000000000p+1'
>>> float.fromhex('0x1.e000000000000p+1')
3.75
>>> b=1./3
>>> b.hex()
'0x1.5555555555555p-2'

```

- A small numerical refinement: on systems that recognize signed zeros (-0 and +0), building a complex number out of two floats now causes the [`complex()`](https://docs.python.org/3.14/library/functions.html#complex) constructor to keep the sign of the zero. (Fixed by Mark T. Dickinson; [bpo-1507](https://bugs.python.org/issue?@action=redirect&bpo=1507).)

- A class that inherits a `__hash__()` method from a parent may assign `__hash__ = None` to declare itself non-hashable. Doing so causes `hash(obj)` to raise a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError), and the class is not reported as realizing the `Hashable` ABC.

Reach for this once you have written a `__cmp__()` or `__eq__()` method that judges objects by value rather than by identity. Every object carries a default hash method keyed on `id(obj)`. Since there is no clean way to strip away an inherited `__hash__()` method, assigning `None` was chosen as the override mechanism. Down at the C level, extensions may point `tp_hash` at [`PyObject_HashNotImplemented()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_HashNotImplemented). (Fixed by Nick Coghlan and Amaury Forgeot d’Arc; [bpo-2235](https://bugs.python.org/issue?@action=redirect&bpo=2235).)

- The [`GeneratorExit`](https://docs.python.org/3.14/library/exceptions.html#GeneratorExit) exception now derives from [`BaseException`](https://docs.python.org/3.14/library/exceptions.html#BaseException) rather than [`Exception`](https://docs.python.org/3.14/library/exceptions.html#Exception). Consequently a handler written as `except Exception:` will not accidentally trap `GeneratorExit`. (Contributed by Chad Austin; [bpo-1537](https://bugs.python.org/issue?@action=redirect&bpo=1537).)

- Generator objects pick up a `gi_code` attribute pointing at the original code object that underlies the generator. (Contributed by Collin Winter; [bpo-1473257](https://bugs.python.org/issue?@action=redirect&bpo=1473257).)

- Alongside positional parameters, the [`compile()`](https://docs.python.org/3.14/library/functions.html#compile) built-in function now also takes keyword arguments. (Contributed by Thomas Wouters; [bpo-1444529](https://bugs.python.org/issue?@action=redirect&bpo=1444529).)

-

[Subject index](INDEX.md) · [Previous source section](core-language-changes.md) · [Next source section](complex-parsing-and-language-behavior.md) · [Release/subject declaration](python-3-0.md) · [Release/subject declaration](core-language-changes.md)
