# Python 2.4 changes: Core language and in-place sorting changes

### Other Language Changes

Below are all the modifications Python 2.4 introduces to the core Python language.

- Decorators applying to functions and methods were introduced ([**PEP 318**](https://peps.python.org/pep-0318/)).

- Built-in [`set()`](https://docs.python.org/3.14/library/stdtypes.html#set) and [`frozenset()`](https://docs.python.org/3.14/library/stdtypes.html#frozenset) types arrived ([**PEP 218**](https://peps.python.org/pep-0218/)). Among the other fresh built-ins is the `reversed(seq)` function ([**PEP 322**](https://peps.python.org/pep-0322/)).

- Generator expressions made their debut ([**PEP 289**](https://peps.python.org/pep-0289/)).

- A number of numeric expressions are no longer capped at values of 32 or 64 bits ([**PEP 237**](https://peps.python.org/pep-0237/)).

- Parentheses may now wrap the roster of names within a `from module import names` statement ([**PEP 328**](https://peps.python.org/pep-0328/)).

- The [`dict.update()`](https://docs.python.org/3.14/library/stdtypes.html#dict.update) method now takes the very same argument shapes the [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict) constructor does. That covers any mapping, any iterable made of key/value pairs, plus keyword arguments. (Contributed by Raymond Hettinger.)

- The string methods `ljust()`, `rjust()`, and `center()` now accept an optional argument for naming a fill character that isn't a space. (Contributed by Raymond Hettinger.)

- Strings additionally acquired an `rsplit()` method that behaves like `split()` except it splits starting from the string's end. (Contributed by Sean Reifschneider.)

```python
>>> 'www.python.org'.split('.', 1)
['www', 'python.org']
'www.python.org'.rsplit('.', 1)
['www.python', 'org']

```

- Three keyword parameters — *cmp*, *key*, and *reverse* — were introduced into the `sort()` method belonging to lists. They streamline several frequent uses of `sort()`. Every one of these parameters is optional.

Regarding the *cmp* parameter, its value ought to be a comparison function accepting two parameters and returning -1, 0, or +1 according to how those parameters compare. That function is then applied to sort the list. Formerly this was the sole parameter that `sort()` would accept.

*key* ought to be a one-parameter function that accepts a list element and yields a comparison key for that element. The list then gets sorted by means of the comparison keys. The example that follows sorts a list without regard to case:

```python
>>> L = ['A', 'b', 'c', 'D']
>>> L.sort()                 # Case-sensitive sort
>>> L
['A', 'D', 'b', 'c']
>>> # Using 'key' parameter to sort list
>>> L.sort(key=lambda x: x.lower())
>>> L
['A', 'b', 'c', 'D']
>>> # Old-fashioned way
>>> L.sort(cmp=lambda x,y: cmp(x.lower(), y.lower()))
>>> L
['A', 'b', 'c', 'D']

```

That final example, employing the *cmp* parameter, represents the former approach to a case-insensitive sort. Although it functions, it runs more slowly than a *key* parameter does. Using *key* invokes the `lower()` method a single time per list element, whereas *cmp* invokes it twice for every comparison, so *key* cuts down on calls to the `lower()` method.

When key functions and comparison functions are simple, you can frequently sidestep a [`lambda`](https://docs.python.org/3.14/reference/expressions.html#lambda) expression by relying on an unbound method instead. As an illustration, the case-insensitive sort shown above is most cleanly written as:

```python
>>> L.sort(key=str.lower)
>>> L
['A', 'b', 'c', 'D']

```

Lastly, the *reverse* parameter accepts a Boolean value. When the value is true, the list will be ordered in reverse. Rather than `L.sort(); L.reverse()`, you can now simply write `L.sort(reverse=True)`.

Sorting results are now guaranteed stable. What this means is that two entries holding equal keys come back in the very order in which they were supplied. For instance, you might sort a roster of people by name and then sort that list by age, producing a list ordered by age in which people sharing the same age stay in name-sorted order.

[Subject index](INDEX.md) · [Previous source section](pep-331-locale-independent-float-string-conversions.md) · [Next source section](sorted-builtin-numeric-and-module-launch-changes.md) · [Release/subject declaration](pep-218-built-in-set-objects.md)
