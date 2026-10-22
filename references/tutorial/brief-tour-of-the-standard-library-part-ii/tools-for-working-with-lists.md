# 11.7. Tools for working with lists

### 11.7. Tools for working with lists

The built-in list type covers a great many data-structure requirements. Even so, there are moments when you want a different implementation carrying its own performance trade-offs.

An [`array`](https://docs.python.org/3.14/library/array.html#array.array) object — list-like but holding only uniform data and packing it more tightly — comes from the [`array`](https://docs.python.org/3.14/library/array.html#module-array) module. The next example builds an array whose numbers are kept as two-byte unsigned binary values (typecode `"H"`) in place of the usual 16 bytes per slot that ordinary lists of Python int objects consume:

```python
>>> from array import array
>>> a = array('H', [4000, 10, 700, 22222])
>>> sum(a)
26932
>>> a[1:3]
array('H', [10, 700])

```

A [`deque`](https://docs.python.org/3.14/library/collections.html#collections.deque) object — resembling a list but with quicker appends and pops at the left end, traded against slower mid-sequence lookups — is supplied by the [`collections`](https://docs.python.org/3.14/library/collections.html#module-collections) module. Such objects fit naturally for building queues and for breadth-first tree traversals:

```python
>>> from collections import deque
>>> d = deque(["task1", "task2", "task3"])
>>> d.append("task4")
>>> print("Handling", d.popleft())
Handling task1

```

```python
unsearched = deque([starting_node])
def breadth_first_search(unsearched):
    node = unsearched.popleft()
    for m in gen_moves(node):
        if is_goal(m):
            return m
        unsearched.append(m)

```

Beyond these alternative list implementations, the library carries further utilities — for instance the [`bisect`](https://docs.python.org/3.14/library/bisect.html#module-bisect) module, whose functions operate on sorted lists:

```python
>>> import bisect
>>> scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
>>> bisect.insort(scores, (300, 'ruby'))
>>> scores
[(100, 'perl'), (200, 'tcl'), (300, 'ruby'), (400, 'lua'), (500, 'python')]

```

Functions for building heaps atop plain lists are found in the [`heapq`](https://docs.python.org/3.14/library/heapq.html#module-heapq) module. The smallest-valued item is forever held at index zero. That property pays off for programs that keep reaching for the least element yet would rather avoid sorting the whole list:

```python
>>> from heapq import heapify, heappop, heappush
>>> data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
>>> heapify(data)                      # rearrange the list into heap order
>>> heappush(data, -5)                 # add a new entry
>>> [heappop(data) for i in range(3)]  # fetch the three smallest entries
[-5, 0, 1]

```

[Subject index](INDEX.md) · [Previous source section](weak-references.md) · [Following source section](decimal-floating-point-arithmetic.md)
