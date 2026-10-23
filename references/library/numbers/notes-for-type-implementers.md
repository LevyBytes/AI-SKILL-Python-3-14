# numbers - Notes for type implementers

### Notes for type implementers

Whoever implements these types must take care that numbers which are equal compare equal and hash alike. That can get tricky once two separate extensions of the reals are in play. As an illustration, here is how [`fractions.Fraction`](https://docs.python.org/3.14/library/fractions.html#fractions.Fraction) defines [`hash()`](https://docs.python.org/3.14/library/functions.html#hash):

```python
def __hash__(self):
    if self.denominator == 1:
        # Get integers right.
        return hash(self.numerator)
    # Expensive check, but definitely correct.
    if self == float(self):
        return hash(float(self))
    else:
        # Use tuple's hash to avoid a high collision rate on
        # simple fractions.
        return hash((self.numerator, self.denominator))

```

[Subject index](INDEX.md) · [Previous](numbers-integral-class.md) · [Continue](adding-more-numeric-abcs.md) · [Owning module, declaration or section: numbers](numbers-number-class.md)
