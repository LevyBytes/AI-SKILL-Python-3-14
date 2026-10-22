# collections.deque: `append()`, `appendleft()`, `clear()`, `copy()`, `count()`, `extend()`, `extendleft()`, `index()`, `insert()`, `pop()`, `popleft()`, `remove()`, `reverse()`, `rotate()`

append(*item*, */*)

Add *item* to the right side of the deque.

 appendleft(*item*, */*)

Add *item* to the left side of the deque.

 clear()

Remove all elements from the deque leaving it with length 0.

 copy()

Create a shallow copy of the deque.

Added in version 3.5.

 count(*value*, */*)

Count the number of deque elements equal to *value*.

Added in version 3.2.

 extend(*iterable*, */*)

Grow the deque on its right side by tacking on elements taken from the iterable argument.

 extendleft(*iterable*, */*)

Grow the deque on its left side by tacking on elements drawn from *iterable*. Bear in mind that this run of left appends flips the ordering of the elements supplied in the iterable argument.

 index(*value*[, *start*[, *stop*]])

Give back where *value* sits in the deque (at or past index *start* yet ahead of index *stop*). It yields the earliest match, or else raises [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) when nothing matches.

Added in version 3.5.

 insert(*index*, *value*, */*)

Insert *value* into the deque at position *index*.

Should that insertion push a bounded deque past *maxlen*, an [`IndexError`](https://docs.python.org/3.14/library/exceptions.html#IndexError) gets raised.

Added in version 3.5.

 pop()

Take off and hand back an element from the deque's right side. Where the deque holds nothing, an [`IndexError`](https://docs.python.org/3.14/library/exceptions.html#IndexError) is raised.

 popleft()

Take off and hand back an element from the deque's left side. Where the deque holds nothing, an [`IndexError`](https://docs.python.org/3.14/library/exceptions.html#IndexError) is raised.

 remove(*value*, */*)

Remove the first occurrence of *value*. If not found, raises a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError).

 reverse()

Reverse the elements of the deque in-place and then return `None`.

Added in version 3.2.

 rotate(*n=1*, */*)

Turn the deque *n* steps toward the right. Should *n* be negative, the turn goes leftward instead.

For a non-empty deque, a single rightward step matches `d.appendleft(d.pop())`, whereas a single leftward step matches `d.append(d.popleft())`.

Deque objects also provide one read-only attribute:

[Subject index](INDEX.md) · [Previous](collections-deque-class.md) · [Continue](deque-objects.md) · [Owning module, declaration or section: collections](collections-container-datatypes.md) · [Owning module, declaration or section: collections.deque](collections-deque-class.md) · [Owning module, declaration or section: `deque` objects](collections-deque-class.md)
