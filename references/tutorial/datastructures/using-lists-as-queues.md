# 5.1.2. Using Lists as Queues

### 5.1.2. Using Lists as Queues

You can likewise treat a list as a queue, where whatever was added first is the first thing taken back out ("first-in, first-out"); lists, however, perform poorly in this role. Although appending and popping at the tail of a list run quickly, inserting or popping at the head of a list is sluggish (since every other element must shift over by one).

For a queue, reach for [`collections.deque`](https://docs.python.org/3.14/library/collections.html#collections.deque), which was built so that appends and pops at either end stay fast. As an illustration:

```python
>>> from collections import deque
>>> queue = deque(["Eric", "John", "Michael"])
>>> queue.append("Terry")           # Terry arrives
>>> queue.append("Graham")          # Graham arrives
>>> queue.popleft()                 # The first to arrive now leaves
'Eric'
>>> queue.popleft()                 # The second to arrive now leaves
'John'
>>> queue                           # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])

```

[Subject index](INDEX.md) · [Previous source section](using-lists-as-stacks.md) · [Following source section](list-comprehension-construction-and-equivalent-nested-loops.md)
