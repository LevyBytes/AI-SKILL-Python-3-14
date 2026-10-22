# Odds and Ends

### Odds and Ends

- When you need locale-aware sorting, reach for [`locale.strxfrm()`](https://docs.python.org/3.14/library/locale.html#locale.strxfrm) as a key function, or [`locale.strcoll()`](https://docs.python.org/3.14/library/locale.html#locale.strcoll) as a comparison function. This is called for because what counts as “alphabetical” order differs from one culture to the next, even when the alphabet itself is identical.

- The *reverse* parameter preserves sort stability all the same (so records sharing equal keys keep their original sequence). Curiously, you can reproduce the same outcome without that parameter at all by applying the built-in [`reversed()`](https://docs.python.org/3.14/library/functions.html#reversed) function two times over:

```pycon
>>> data = [('red', 1), ('blue', 1), ('red', 2), ('blue', 2)]
>>> standard_way = sorted(data, key=itemgetter(0), reverse=True)
>>> double_reversed = list(reversed(sorted(reversed(data), key=itemgetter(0))))
>>> assert standard_way == double_reversed
>>> standard_way
[('red', 1), ('red', 2), ('blue', 1), ('blue', 2)]

```

- When the sort routines weigh two objects against each other, they rely on `<`. Because of that, giving a class its own default ordering is straightforward: just define an [`__lt__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__lt__) method:

```pycon
>>> Student.__lt__ = lambda self, other: self.age < other.age
>>> sorted(student_objects)
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

```

Be aware, though, that `<` may resort to [`__gt__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__gt__) whenever [`__lt__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__lt__) has not been defined (consult [`object.__lt__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__lt__) for how this plays out). So you don't get caught off guard, [**PEP 8**](https://peps.python.org/pep-0008/) advises defining every one of the six comparison methods. To ease that chore, the [`total_ordering()`](https://docs.python.org/3.14/library/functools.html#functools.total_ordering) decorator is on hand.

- A key function doesn't have to draw solely on the objects under sort; it is free to consult outside resources as well. Suppose, for example, that the student grades live in a dictionary - those can then drive the ordering of an entirely separate list of student names:

```pycon
>>> students = ['dave', 'john', 'jane']
>>> newgrades = {'john': 'F', 'jane':'A', 'dave': 'C'}
>>> sorted(students, key=newgrades.__getitem__)
['jane', 'dave', 'john']

```

[Subject index](INDEX.md) · [Previous source context](strategies-for-unorderable-types-and-values.md) · [Following source context](partial-sorts.md)
