# How do I generate random numbers in Python?

### Mathematics and Numerics

### How do I generate random numbers in Python?

A random number generator comes built into the standard [`random`](https://docs.python.org/3.14/library/random.html#module-random) module, and using it is straightforward:

```python
import random
random.random()

```

That call gives back a random floating-point value somewhere in [0, 1).

This module additionally bundles plenty of more specialized generators, among them:

- `randrange(a, b)` picks a whole number drawn from [a, b).

- `uniform(a, b)` picks a floating-point value drawn from [a, b).

- `normalvariate(mean, sdev)` draws a sample from the normal (Gaussian) distribution.

A handful of higher-level helpers work straight on sequences, for instance:

- `choice(S)` returns one element selected at random out of the supplied sequence.

- `shuffle(L)` rearranges a list in place, scrambling its order at random.

On top of that, a `Random` class is available; instantiate it whenever you need several independent random number generators.

[Subject index](INDEX.md)
