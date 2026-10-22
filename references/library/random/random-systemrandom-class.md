# random: `random.SystemRandom`

*class *random.SystemRandom([*seed*])

Class that leans on the [`os.urandom()`](https://docs.python.org/3.14/library/os.html#os.urandom) function to draw random numbers from the sources the operating system exposes. It is not present on every platform. Since it keeps no software state, its sequences cannot be reproduced. As a result, the `seed()` method does nothing and is disregarded. Calling the `getstate()` or `setstate()` methods raises [`NotImplementedError`](https://docs.python.org/3.14/library/exceptions.html#NotImplementedError).

[Subject index](INDEX.md) · [Previous](random-random-seed-to-random-random-randbytes.md) · [Continue](notes-on-reproducibility.md) · [Owning module, declaration or section: random](random-generate-pseudo-random-numbers.md) · [Owning module, declaration or section: Alternative Generator](random-random-class.md)
