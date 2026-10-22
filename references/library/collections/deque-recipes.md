# collections — `deque` Recipes

### `deque` Recipes

Here are several techniques for handling deques.

Length-bounded deques deliver behavior akin to the `tail` filter in Unix:

```python
def tail(filename, n=10):
    'Return the last n lines of a file'
    with open(filename) as f:
        return deque(f, n)

```

A further way to use deques is to keep a run of recently added elements by appending on the right and popping on the left:

```python
def moving_average(iterable, n=3):
    # moving_average([40, 30, 50, 46, 39, 44]) --> 40.0 42.0 45.0 43.0
    # https://en.wikipedia.org/wiki/Moving_average
    it = iter(iterable)
    d = deque(itertools.islice(it, n-1))
    d.appendleft(0)
    s = sum(d)
    for elem in it:
        s += elem - d.popleft()
        d.append(elem)
        yield s / n

```

You can build a [round-robin scheduler](https://en.wikipedia.org/wiki/Round-robin_scheduling) by holding input iterators inside a `deque`. The iterator currently sitting at index zero supplies each value. Once it runs dry, drop it via `popleft()`; if it still has items, send it to the back of the queue using the `rotate()` method:

```python
def roundrobin(*iterables):
    "roundrobin('ABC', 'D', 'EF') --> A D E B F C"
    iterators = deque(map(iter, iterables))
    while iterators:
        try:
            while True:
                yield next(iterators[0])
                iterators.rotate(-1)
        except StopIteration:
            # Remove an exhausted iterator.
            iterators.popleft()

```

Both slicing and deletion on a `deque` can be built on top of `rotate()`. As an illustration, a pure Python equivalent of `del d[n]` leans on `rotate()` to shift the element into place before popping it:

```python
def delete_nth(d, n):
    d.rotate(-n)
    d.popleft()
    d.rotate(n)

```

A comparable strategy yields `deque` slicing: apply `rotate()` so the element you care about lands at the left edge of the deque. Strip out the stale items with `popleft()`, append fresh ones with `extend()`, and undo the earlier rotation. Slight tweaks to this pattern make it straightforward to build Forth style stack moves like `dup`, `drop`, `swap`, `over`, `pick`, `rot`, and `roll`.

[Subject index](INDEX.md) · [Previous](deque-objects.md) · [Owning module, declaration or section: collections](collections-container-datatypes.md) · [Continue](defaultdict-class-contract.md)
