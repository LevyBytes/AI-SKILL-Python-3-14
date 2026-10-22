# What's New In Python 3.2 / random — random

### random

Inside the [`random`](https://docs.python.org/3.14/library/random.html#module-random) module, the integer methods now generate uniform distributions more reliably. Their earlier approach derived choices from `int(n*random())`, which skewed slightly any time *n* was not a power of two. The new scheme draws repeatedly from a range running up to the next power of two, retaining a draw only once it lands within `0 <= x < n`. Touched by this change are [`randrange()`](https://docs.python.org/3.14/library/random.html#random.randrange), [`randint()`](https://docs.python.org/3.14/library/random.html#random.randint), [`choice()`](https://docs.python.org/3.14/library/random.html#random.choice), [`shuffle()`](https://docs.python.org/3.14/library/random.html#random.shuffle) and [`sample()`](https://docs.python.org/3.14/library/random.html#random.sample).

(Contributed by Raymond Hettinger; [bpo-9025](https://bugs.python.org/issue?@action=redirect&bpo=9025).)

[Subject index](INDEX.md) · [Previous source section](unittest.md) · [Next source section](poplib.md) · [Release/subject declaration](pep-384-defining-a-stable-abi.md)
