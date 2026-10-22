# Mutable Sequence Types

### Mutable Sequence Types

Mutable sequence types define the operations shown in the table below. The [`collections.abc.MutableSequence`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.MutableSequence) ABC is supplied to ease correct implementation of these operations on your own sequence types.

Throughout the table, an instance of a mutable sequence type is denoted *s*, any iterable object is denoted *t*, and *x* denotes any object meeting whatever type and value limits *s* imposes (for instance, `bytearray` admits only integers obeying the value limit `0 <= x <= 255`).

| Operation | Result | Notes |
| --- | --- | --- |
| `s[i] = x` | item *i* of *s* is replaced by *x* |  |
| `del s[i]` | removes item *i* of *s* |  |
| `s[i:j] = t` | the iterable *t*'s contents replace the slice of *s* running from *i* to *j* |  |
| `del s[i:j]` | removes the elements of `s[i:j]` from the list (same as `s[i:j] = []`) |  |
| `s[i:j:k] = t` | the elements of `s[i:j:k]` are replaced by those of *t* | (1) |
| `del s[i:j:k]` | removes the elements of `s[i:j:k]` from the list |  |
| `s += t` | grows *s* using *t*'s contents (in most respects matching `s[len(s):len(s)] = t`) |  |
| `s *= n` | updates *s* with its contents repeated *n* times | (2) |

Notes:

1.

Where *k* differs from `1`, *t* has to match the length of the slice it stands in for.

2.

The value *n* is an integer, or some object that implements [`__index__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__index__). A zero or negative *n* empties the sequence. The items within the sequence are not duplicated; they get referenced repeatedly, just as described for `s * n` under Common Sequence Operations.

Mutable Sequence Methods

Mutable sequence types furthermore support the methods below:

 sequence.append(*value*, */*)

Append *value* onto the tail of the sequence. This matches writing `seq[len(seq):len(seq)] = [value]`.

 sequence.clear()

Added in version 3.3.

Strip every item out of *sequence*. This matches writing `del sequence[:]`.

 sequence.copy()

Added in version 3.3.

Produce a shallow copy of *sequence*. This matches writing `sequence[:]`.

Hint

While the `copy()` method is not part of the [`MutableSequence`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.MutableSequence) [`ABC`](https://docs.python.org/3.14/library/abc.html#abc.ABC), the bulk of concrete mutable sequence types supply it.

 sequence.extend(*iterable*, */*)

Grow *sequence* with the contents of *iterable*. For the most part this matches writing `seq[len(seq):len(seq)] = iterable`.

 sequence.insert(*index*, *value*, */*)

Place *value* into *sequence* at the supplied *index*. This matches writing `sequence[index:index] = [value]`.

 sequence.pop(*index=-1*, */*)

Fetch the item at *index* and drop it from *sequence* as well. The default removes and returns the final item in *sequence*.

 sequence.remove(*value*, */*)

Drop the first item from *sequence* where `sequence[i] == value`.

Raises [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) when *value* is absent from *sequence*.

 sequence.reverse()

Flip the order of *sequence*'s items in place. To stay frugal with space when flipping a large sequence, this method works by side-effect; as a reminder of that, it returns `None`.

[Subject index](INDEX.md) · [Previous](immutable-sequence-types.md) · [Continue](list-class.md)
