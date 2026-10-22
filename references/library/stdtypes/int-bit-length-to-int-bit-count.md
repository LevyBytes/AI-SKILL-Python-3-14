# stdtypes: `int.bit_length()`, `int.bit_count()`

### Additional Methods on Integer Types

The int type implements the [`numbers.Integral`](https://docs.python.org/3.14/library/numbers.html#numbers.Integral) [abstract base class](https://docs.python.org/3.14/glossary.html#term-abstract-base-class). Beyond that, it offers a handful more methods:

 int.bit_length()

Return how many bits are needed to express an integer in binary, leaving out the sign and any leading zeros:

```python
>>> n = -37
>>> bin(n)
'-0b100101'
>>> n.bit_length()
6

```

To be exact, when `x` is nonzero, `x.bit_length()` equals the one positive integer `k` for which `2**(k-1) <= abs(x) < 2**k`. The same way, whenever `abs(x)` is small enough that its logarithm rounds correctly, `k = 1 + int(log(abs(x), 2))`. When `x` is zero, `x.bit_length()` gives back `0`.

Equivalent to:

```python
def bit_length(self):
    s = bin(self)       # binary representation:  bin(-37) --> '-0b100101'
    s = s.lstrip('-0b') # remove leading zeros and minus sign
    return len(s)       # len('100101') --> 6

```

Added in version 3.1.

 int.bit_count()

Return how many ones appear in the binary representation of the integer's absolute value. The population count is another name for this. Example:

```python
>>> n = 19
>>> bin(n)
'0b10011'
>>> n.bit_count()
3
>>> (-n).bit_count()
3

```

Equivalent to:

```python
def bit_count(self):
    return bin(self).count("1")

```

Added in version 3.10.

[Subject index](INDEX.md) · [Previous](bitwise-operations-on-integer-types.md) · [Continue](int-to-bytes.md)
