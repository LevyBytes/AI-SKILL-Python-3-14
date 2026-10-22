# Thread safety for bytearray objects

### Thread safety for bytearray objects

>

The [`len()`](https://docs.python.org/3.14/library/functions.html#len) function is lock-free and [atomic](https://docs.python.org/3.14/glossary.html#term-atomic-operation).

Concatenation and comparisons go through the buffer protocol, which blocks resizing yet does not keep the per-object lock held. Such operations can witness intermediate states left by concurrent edits:

```python
ba + other    # may observe concurrent writes
ba == other   # may observe concurrent writes
ba < other    # may observe concurrent writes

```

From this point onward, all remaining operations hold the per-object lock.

Fetching one element or one slice is fine to invoke across several threads:

```python
ba[i]        # bytearray.__getitem__
ba[i:j]      # slice

```

The operations below are fine to invoke across several threads and leave the bytearray uncorrupted:

```python
ba[i] = x         # write single byte
ba[i:j] = values  # write slice
ba.append(x)      # append single byte
ba.extend(other)  # extend with iterable
ba.insert(i, x)   # insert single byte
ba.pop()          # remove and return last byte
ba.pop(i)         # remove and return byte at index
ba.remove(x)      # remove first occurrence
ba.reverse()      # reverse in place
ba.clear()        # remove all bytes

```

Slice assignment locks the pair of objects where *values* is a [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray):

```python
ba[i:j] = other_bytearray  # both locked

```

The operations below build new objects and keep the per-object lock held throughout:

```python
ba.copy()     # returns a shallow copy
ba * n        # repeat into new bytearray

```

The membership test keeps the lock held throughout:

```python
x in ba       # bytearray.__contains__

```

Every other bytearray method (for instance [`find()`](https://docs.python.org/3.14/library/stdtypes.html#bytearray.find), [`replace()`](https://docs.python.org/3.14/library/stdtypes.html#bytearray.replace), [`split()`](https://docs.python.org/3.14/library/stdtypes.html#bytearray.split), [`decode()`](https://docs.python.org/3.14/library/stdtypes.html#bytearray.decode), and so on) keeps the per-object lock held throughout.

Operations spanning multiple accesses, iteration included, are never atomic:

```python
# NOT atomic: check-then-act
if x in ba:
    ba.remove(x)

# NOT thread-safe: iteration while modifying
for byte in ba:
    process(byte)  # another thread may modify ba

```

To iterate safely over a bytearray that another thread might edit, walk a copy instead:

```python
# Make a copy to iterate safely
for byte in ba.copy():
    process(byte)

```

Reach for external synchronization whenever [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) instances are shared between threads. Refer to [Python support for free threading](https://docs.python.org/3.14/howto/free-threading-python.html#freethreading-python-howto) for further detail.

[Subject index](INDEX.md) · [Previous](set-disjoint-operation-locking-example.md) · [Continue](thread-safety-for-memoryview-objects.md)
