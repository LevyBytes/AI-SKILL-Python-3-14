# bisect — `bisect` — Array bisection algorithm

## bisect — Array bisection algorithm

### `bisect` — Array bisection algorithm

**Source code:** [Lib/bisect.py](https://github.com/python/cpython/tree/3.14/Lib/bisect.py)

---

This module helps you keep a list in sorted order without resorting the whole thing after every insertion. With long lists whose items carry costly comparison operations, that can beat repeated linear searches or recurrent re-sorting.

The reason the module bears the name `bisect` is that it leans on a straightforward bisection algorithm to get its job done. In contrast to other bisection utilities that hunt for a particular value, the functions here aim to pinpoint an insertion point. For that reason, they never invoke an [`__eq__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__eq__) method to judge whether a value has turned up. They invoke only the [`__lt__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__lt__) method, returning an insertion point situated between values in an array.

Note

The functions making up this module aren't thread-safe. Running `bisect` functions on one shared sequence from several threads at once can lead to undefined behaviour. By the same token, if some other thread mutates the supplied sequence while a `bisect` function is busy with it, the outcome is undefined. As an example, calling `insort_left()` against the same list across multiple threads may leave that list unsorted.

The functions made available are these:

 bisect.bisect_left(*a*, *x*, *lo=0*, *hi=len(a)*, ***, *key=None*)

Pinpoints where *x* should be inserted within *a* so that sorted order holds. You can pass *lo* and *hi* to mark out the slice of the list to weigh; left unset, the whole list is considered. Where *x* already sits in *a*, the insertion point falls ahead of (to the left of) any entries already there. The value returned works as the first argument to `list.insert()`, on the assumption that *a* is sorted to begin with.

The insertion point *ip* that comes back splits the array *a* into a pair of slices, where `all(elem < x for elem in a[lo : ip])` holds for the left slice and `all(elem >= x for elem in a[ip : hi])` holds for the right slice.

The *key* parameter names a [key function](https://docs.python.org/3.14/glossary.html#term-key-function) of one argument, used to pull a comparison key out of each element in the array. So that searching of complex records remains possible, this key function is not applied to the *x* value.

When *key* is `None`, elements get compared straight off and no key function is invoked.

Changed in version 3.10: Added the *key* parameter.

 bisect.bisect_right(*a*, *x*, *lo=0*, *hi=len(a)*, ***, *key=None*)

 bisect.bisect(*a*, *x*, *lo=0*, *hi=len(a)*, ***, *key=None*)

Akin to `bisect_left()`, except the insertion point it returns lands after (to the right of) any entries of *x* already present in *a*.

The insertion point *ip* that comes back divides the array *a* into a pair of slices, where `all(elem <= x for elem in a[lo : ip])` holds for the left slice and `all(elem > x for elem in a[ip : hi])` holds for the right slice.

Changed in version 3.10: Added the *key* parameter.

 bisect.insort_left(*a*, *x*, *lo=0*, *hi=len(a)*, ***, *key=None*)

Places *x* into *a* while keeping sorted order.

To begin with, this function calls `bisect_left()` to find an insertion point. After that, it calls the [`insert()`](https://docs.python.org/3.14/library/stdtypes.html#sequence.insert) method on *a* so that *x* goes in at the right spot and sort order is preserved.

So that records can be inserted into a table, the *key* function (where one exists) is applied to *x* during the search step yet skipped for the insertion step.

Bear in mind that the *O*(log *n*) search is overshadowed by the sluggish *O*(*n*) insertion step.

Changed in version 3.10: Added the *key* parameter.

 bisect.insort_right(*a*, *x*, *lo=0*, *hi=len(a)*, ***, *key=None*)

 bisect.insort(*a*, *x*, *lo=0*, *hi=len(a)*, ***, *key=None*)

Akin to `insort_left()`, but it slots *x* into *a* following any entries of *x* already there.

Here the function starts by calling `bisect_right()` to determine an insertion point. It then calls the [`insert()`](https://docs.python.org/3.14/library/stdtypes.html#sequence.insert) method on *a* to drop *x* into the proper spot and uphold sort order.

To allow records to be inserted into a table, the *key* function (if one is supplied) gets applied to *x* for the search step but not for the insertion step.

Do remember that the *O*(log *n*) search is outweighed by the slow *O*(*n*) insertion step.

Changed in version 3.10: Added the *key* parameter.

[Subject index](INDEX.md) · [Continue](performance-notes.md)
