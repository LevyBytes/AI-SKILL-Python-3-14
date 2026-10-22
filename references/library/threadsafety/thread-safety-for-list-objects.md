# Thread safety for list objects

### Thread safety for list objects

Fetching one element out of a [`list`](https://docs.python.org/3.14/library/stdtypes.html#list) is [atomic](https://docs.python.org/3.14/glossary.html#term-atomic-operation):

```python
lst[i]   # list.__getitem__

```

The methods below walk the list and rely on [atomic](https://docs.python.org/3.14/glossary.html#term-atomic-operation) reads of each item to carry out their work. As a result, the results they hand back can reflect concurrent edits:

```python
item in lst
lst.index(item)
lst.count(item)

```

Every operation listed above skips taking any [per-object locks](https://docs.python.org/3.14/glossary.html#term-per-object-lock). They place no block on concurrent edits. Operations that do take a lock will not stop these from seeing intermediate states.

From this point onward, all remaining operations block by taking the [per-object lock](https://docs.python.org/3.14/glossary.html#term-per-object-lock).

Storing one item through `lst[i] = x` is fine to invoke across several threads and leaves the list uncorrupted.

The operations below build new objects and look [atomic](https://docs.python.org/3.14/glossary.html#term-atomic-operation) to other threads:

```python
lst1 + lst2    # concatenates two lists into a new list
x * lst        # repeats lst x times into a new list
lst.copy()     # returns a shallow copy of the list

```

The methods below that touch just one element without any shifting are [atomic](https://docs.python.org/3.14/glossary.html#term-atomic-operation):

```python
lst.append(x)  # append to the end of the list, no shifting required
lst.pop()      # pop element from the end of the list, no shifting required

```

The [`clear()`](https://docs.python.org/3.14/library/stdtypes.html#list.clear) method counts as [atomic](https://docs.python.org/3.14/glossary.html#term-atomic-operation) too. No other thread can witness elements while they are being dropped.

The [`sort()`](https://docs.python.org/3.14/library/stdtypes.html#list.sort) method is not [atomic](https://docs.python.org/3.14/glossary.html#term-atomic-operation). No other thread can witness intermediate states during the sort, though the list reads as empty while the sort runs.

The operations below can let [lock-free](https://docs.python.org/3.14/glossary.html#term-lock-free) operations witness intermediate states, because they edit several elements at once in place:

```python
lst.insert(idx, item)  # shifts elements
lst.pop(idx)           # idx not at the end of the list, shifts elements
lst *= x               # copies elements in place

```

The [`remove()`](https://docs.python.org/3.14/library/stdtypes.html#list.remove) method can permit concurrent edits, since comparing elements may run arbitrary Python code (by way of [`__eq__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__eq__)).

[`extend()`](https://docs.python.org/3.14/library/stdtypes.html#list.extend) is fine to invoke across several threads. Its promises, though, hinge on the iterable handed to it. Should that be a [`list`](https://docs.python.org/3.14/library/stdtypes.html#list), a [`tuple`](https://docs.python.org/3.14/library/stdtypes.html#tuple), a [`set`](https://docs.python.org/3.14/library/stdtypes.html#set), a [`frozenset`](https://docs.python.org/3.14/library/stdtypes.html#frozenset), a [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict) or a [dictionary view object](https://docs.python.org/3.14/library/stdtypes.html#dict-views) (subclasses excluded), then the `extend` operation is shielded from concurrent edits to the iterable. If not, an iterator gets created that another thread can edit concurrently. The very same holds for inplace concatenation of a list against other iterables via `lst += iterable`.

In the same way, assigning into a list slice through `lst[i:j] = iterable` is fine to invoke across several threads, but `iterable` gets locked only when it too is a [`list`](https://docs.python.org/3.14/library/stdtypes.html#list) (subclasses excluded).

Operations spanning multiple accesses, iteration included, are never atomic. As an illustration:

```python
# NOT atomic: read-modify-write
lst[i] = lst[i] + 1

# NOT atomic: check-then-act
if lst:
    item = lst.pop()

# NOT thread-safe: iteration while modifying
for item in lst:
    process(item)  # another thread may modify lst

```

Reach for external synchronization whenever [`list`](https://docs.python.org/3.14/library/stdtypes.html#list) instances are shared between threads.

[Subject index](INDEX.md) · [Previous](atomic.md) · [Continue](dictionary-thread-safety-overview.md)
