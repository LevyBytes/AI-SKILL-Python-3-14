# Why must dictionary keys be immutable?

### Why must dictionary keys be immutable?

The hash table implementation behind dictionaries uses a hash value derived from the key value to locate the key. Were the key a mutable object, its value might change, and so its hash might change too. Yet because whoever alters the key object has no way to know it was serving as a dictionary key, they can't relocate the entry within the dictionary. Then, on trying to look that same object up in the dictionary, it won't be found, because its hash value now differs. Were you to look up the old value, it wouldn't turn up either, since the value of the object sitting in that hash bin would be different.

If you'd like a dictionary keyed by a list, just convert the list to a tuple beforehand; the function `tuple(L)` produces a tuple holding the same entries as the list `L`. Tuples being immutable, they can therefore serve as dictionary keys.

A few unacceptable solutions that have been put forward:

- Hash lists by their address (object ID). This fails because if you build a new list with the same value it won't be found; for example:

```python
mydict = {[1, 2]: '12'}
print(mydict[[1, 2]])

```

would raise a [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError) exception, since the id of the `[1, 2]` on the second line is not the same as the one on the first line. Stated otherwise, dictionary keys ought to be compared with `==`, not with [`is`](https://docs.python.org/3.14/reference/expressions.html#is).

- Take a copy when a list is used as a key. This fails because the list, being a mutable object, might hold a reference to itself, at which point the copying code would tumble into an infinite loop.

- Permit lists as keys but instruct the user not to alter them. That would open the door to a class of hard-to-trace bugs whenever a program's author overlooked, or by mistake mutated, such a list. It also shatters a key dictionary invariant: that each value present in `d.keys()` can be employed as a dictionary key.

- Flag lists as read-only once they serve as a dictionary key. The trouble is that the changeable value need not be just the top-level object; a tuple wrapping a list could itself act as a key. To enter any such key into a dictionary, one would have to mark every object reachable from it as read-only ? and once more, self-referential objects could trigger an infinite loop.

Should you genuinely need one, there's a workaround, though you adopt it at your own peril: enclose the mutable structure inside a class instance that supplies both a [`__eq__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__eq__) and a [`__hash__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__hash__) method. You must then take care that the hash value for every such wrapper object residing in a dictionary (or other hash based structure) stays fixed throughout the time the object is in the dictionary (or other structure).

```python
class ListWrapper:
    def __init__(self, the_list):
        self.the_list = the_list

    def __eq__(self, other):
        return self.the_list == other.the_list

    def __hash__(self):
        l = self.the_list
        result = 98767 - len(l)*555
        for i, el in enumerate(l):
            try:
                result = result + (hash(el) % 9999999) * 1001 + i
            except Exception:
                result = (result % 7777777) + i * 333
        return result

```

Be aware that the hash computation is made trickier by the chance that some of the list's members are unhashable and likewise by the chance of arithmetic overflow.

Beyond that, it must invariably hold that if `o1 == o2` (ie `o1.__eq__(o2) is True`) then `hash(o1) == hash(o2)` (ie, `o1.__hash__() == o2.__hash__()`), whether or not the object sits in a dictionary. Should you fail to honor these constraints, dictionaries and other hash based structures will misbehave.

For `ListWrapper`, as long as the wrapper object is in a dictionary the wrapped list must stay unchanged to head off anomalies. Don't attempt this unless you're ready to think hard about the requirements and about what follows from not satisfying them correctly. Consider yourself warned.

[Subject index](INDEX.md)
