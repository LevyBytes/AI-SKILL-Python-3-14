# 5.1. More on Lists

### 5.1. More on Lists

Beyond what you've seen so far, the [list](https://docs.python.org/3.14/library/stdtypes.html#typesseq-list) data type offers additional methods. The complete set of methods available on list objects follows:

 list.append(*value*, */*)

Append a single item onto the tail of the list. Behaves like `a[len(a):] = [x]`.

 list.extend(*iterable*, */*)

Grow the list by tacking on every item drawn from the iterable. Behaves like `a[len(a):] = iterable`.

 list.insert(*index*, *value*, */*)

Place an item at a chosen position. Its first argument names the index of the element ahead of which the new one goes, so `a.insert(0, x)` puts the item at the start of the list, while `a.insert(len(a), x)` matches `a.append(x)`.

 list.remove(*value*, */*)

Delete the earliest item in the list whose value equals *value*. A [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised when no matching item exists.

 list.pop(*index=-1*, */*)

Take out the item sitting at the supplied position in the list and hand it back. When you give no index, `a.pop()` strips off and returns the final item in the list. An [`IndexError`](https://docs.python.org/3.14/library/exceptions.html#IndexError) results when the list holds nothing or the index falls beyond the list range.

 list.clear()

Discard every item from the list. Behaves like `del a[:]`.

 list.index(*value*[, *start*[, *stop*]])

Hand back the zero-based index marking where *value* first shows up in the list. A [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised when no matching item exists.

The optional *start* and *end* arguments follow the same meaning they carry in slice notation, narrowing the search to a chosen slice of the list. Keep in mind the index that comes back counts from the head of the entire sequence and not from the *start* argument.

 list.count(*value*, */*)

Report how many times *value* shows up within the list.

 list.sort(***, *key=None*, *reverse=False*)

Order the items of the list in place (the arguments allow you to tailor the sort; consult [`sorted()`](https://docs.python.org/3.14/library/functions.html#sorted) for what they mean).

 list.reverse()

Flip the order of the list's elements in place.

 list.copy()

Hand back a shallow copy of the list. Behaves like `a[:]`.

Here is an example exercising most of the list methods:

```python
>>> fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
>>> fruits.count('apple')
2
>>> fruits.count('tangerine')
0
>>> fruits.index('banana')
3
>>> fruits.index('banana', 4)  # Find next banana starting at position 4
6
>>> fruits.reverse()
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
>>> fruits.append('grape')
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
>>> fruits.sort()
>>> fruits
['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
>>> fruits.pop()
'pear'

```

Perhaps you've observed that methods such as `insert`, `remove` or `sort`, which merely alter the list, print no return value — they hand back the default `None`. [1] Every mutable data structure in Python follows this same design principle.

A further point worth noticing is that some data resists sorting or comparison. Take `[None, 'hello', 10]`: it won't sort, since integers have no comparison against strings and `None` cannot be compared against other types. On top of that, certain types simply lack any defined ordering relation. As an illustration, `3+4j < 5+7j` is not a legal comparison.

[Subject index](INDEX.md) · [Previous source section](data-structures.md) · [Following source section](using-lists-as-stacks.md)
