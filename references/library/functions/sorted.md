# sorted

sorted(*iterable*, */*, ***, *key=None*, *reverse=False*)

Hand back a freshly sorted list built from whatever *iterable* contains.

It accepts two optional arguments, both of which have to be passed as keywords.

The *key* argument names a one-argument function used to pull a comparison key out of each element in *iterable* (say, `key=str.lower`). Its default is `None`, in which case the elements are compared directly.

*reverse* is a boolean. When it's `True`, the list's elements get sorted as though every comparison had been flipped.

Reach for [`functools.cmp_to_key()`](https://docs.python.org/3.14/library/functools.html#functools.cmp_to_key) when you want to turn a legacy *cmp* function into a *key* function.

Python promises that the built-in `sorted()` function is stable. Calling a sort stable means it pledges to leave equal-comparing elements in their existing relative order — handy when you sort across several passes (say, by department first and then by salary grade).

Sorting relies solely on `<` comparisons among the items. Supplying an [`__lt__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__lt__) method is enough on its own to sort, yet [**PEP 8**](https://peps.python.org/pep-0008/) advises that you implement the full set of six [rich comparisons](https://docs.python.org/3.14/reference/expressions.html#comparisons). Doing so wards off bugs that crop up when the same data flows through other ordering tools like `max()`, which lean on a different underlying method. Providing all six comparisons additionally heads off confusion in mixed-type comparisons, which may invoke the reflected [`__gt__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__gt__) method.

To see sorting examples plus a short sorting walkthrough, head to [Sorting Techniques](https://docs.python.org/3.14/howto/sorting.html#sortinghowto).

[Builtin task index](INDEX.md).
