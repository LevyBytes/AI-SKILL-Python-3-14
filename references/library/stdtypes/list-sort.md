# stdtypes / list, tuple, range / Lists: `sort()`

sort(***, *key=None*, *reverse=False*)

This method sorts the list in place, relying solely on `<` comparisons between items. Exceptions go unsuppressed — if any comparison operation fails, the whole sort operation fails (and the list is apt to be left partly modified).

`sort()` takes two arguments that may be supplied only by keyword ([keyword-only arguments](https://docs.python.org/3.14/glossary.html#keyword-only-parameter)):

*key* names a function of one argument used to pull a comparison key out of every list element (`key=str.lower`, for example). Each list item's corresponding key gets computed a single time and then reused throughout the whole sort. A default of `None` means list items get sorted directly with no separate key value computed.

The [`functools.cmp_to_key()`](https://docs.python.org/3.14/library/functools.html#functools.cmp_to_key) utility lets you turn a 2.x-style *cmp* function into a *key* function.

*reverse* is a boolean value. Set to `True`, it sorts the list elements as though every comparison had been reversed.

To stay frugal with space when sorting a large sequence, this method alters the sequence in place. As a reminder that it works by side effect, it gives back no sorted sequence (call [`sorted()`](https://docs.python.org/3.14/library/functions.html#sorted) to explicitly ask for a brand-new sorted list instance).

The `sort()` method is guaranteed to be stable. A sort counts as stable when it promises to leave the relative order of equal-comparing elements unchanged — which aids multi-pass sorting (sorting by department, then by salary grade, say).

The [Sorting Techniques](https://docs.python.org/3.14/howto/sorting.html#sortinghowto) page has sorting examples plus a short sorting tutorial.

**CPython implementation detail:** For as long as a list is being sorted, the result of trying to mutate it, or even examine it, is undefined. Python's C implementation makes the list look empty over that span and raises [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) if it can spot that the list got mutated mid-sort.

See also

The [Thread safety for list objects](https://docs.python.org/3.14/library/threadsafety.html#thread-safety-list) page covers the thread-safety guarantees for `list` objects in detail.

[Subject index](INDEX.md) · [Previous](list-class.md) · [Continue](tuple-class.md) · [Owning module, declaration or section: list](list-class.md) · [Owning module, declaration or section: Lists](list-class.md)
