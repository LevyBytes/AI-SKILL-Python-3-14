# Python 3.8.0 alpha 1 / library / random

[bpo-30561](https://bugs.python.org/issue?@action=redirect&bpo=30561): random.gammavariate(1.0, beta) now yields the identical result that random.expovariate(1.0 / beta) produces. This aligns the pair of algorithms and removes a few quirks from the previous implementation. The trade-off is that it generates a different stream of random variables compared with before.

[bpo-33144](https://bugs.python.org/issue?@action=redirect&bpo=33144): `random.Random()` plus its subclassing machinery were tuned to verify just a single time at class/subclass instantiation whether the `getrandbits()` method is dependable for other methods, `randrange()` among them, when producing arbitrarily large random integers. Patch by Wolfgang Maier.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
