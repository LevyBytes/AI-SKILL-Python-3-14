# 3.2.4. `numbers.Number`

### 3.2.4. [`numbers.Number`](https://docs.python.org/3.14/library/numbers.html#numbers.Number)

Numeric literals create these, and arithmetic operators along with arithmetic built-in functions hand them back as results. Numeric objects are immutable; after creation their value never shifts. Naturally, Python numbers map closely onto mathematical numbers, though they remain bound by the constraints of representing numbers on computers.

Each numeric class has a string form, produced by `__repr__()` and `__str__()`, that exhibits these traits:

- Each is itself a valid numeric literal that, handed to the relevant class constructor, yields an object whose value equals that of the numeric it came from.

- Wherever it can be, the form is rendered in base 10.

- A leading zero is omitted, except that a lone zero ahead of a decimal point may remain.

- A trailing zero is omitted, except that a lone zero following a decimal point may remain.

- Only for a negative number does a sign appear.

Python separates numbers into three kinds: integers, floating-point numbers, and complex numbers:

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](the-standard-type-hierarchy.md) · [Previous source section](ellipsis.md) · [Following source section](numbers-integral.md)
