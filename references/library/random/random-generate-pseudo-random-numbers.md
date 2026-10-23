# random`random` - Generate pseudo-random numbers

### `random` - Generate pseudo-random numbers

**Source code:** [Lib/random.py](https://github.com/python/cpython/tree/3.14/Lib/random.py)

---

This module supplies pseudo-random number generators covering a range of distributions.

For integers, you can draw uniformly from a range. For sequences, you can draw a random element uniformly, shuffle a list into a random ordering in-place, and sample without replacement.

Over the real numbers, there are routines that produce uniform, normal (Gaussian), lognormal, negative exponential, gamma, and beta distributions. To produce distributions over angles, the von Mises distribution is provided.

Nearly every function in the module builds on the underlying `random()` call, which yields a random float drawn uniformly across the half-open interval `0.0 <= X < 1.0`. The core engine in Python is the Mersenne Twister. It emits floats with 53-bit precision and cycles with a period of 2**19937-1. Its C-level code is quick and threadsafe. Among existing random number generators, the Mersenne Twister has been tested as thoroughly as any. That said, because it is fully deterministic, it does not fit every use case, and it is wholly inappropriate for cryptographic work.

Behind the scenes, the functions this module exposes are bound methods of a concealed instance of the `random.Random` class. By creating your own `Random` instances, you obtain generators whose state is independent.

If you want to swap in a different basic generator that you design yourself, the `Random` class supports subclassing: consult that class's documentation for the specifics.

Additionally, the `random` module offers the `SystemRandom` class, which draws on the system function [`os.urandom()`](https://docs.python.org/3.14/library/os.html#os.urandom) to obtain randomness from sources the operating system makes available.

Warning

Do not rely on this module's pseudo-random generators where security matters. When security or cryptography is involved, refer to the [`secrets`](https://docs.python.org/3.14/library/secrets.html#module-secrets) module.

See also

“Mersenne Twister: A 623-dimensionally equidistributed uniform pseudorandom number generator” — by M. Matsumoto and T. Nishimura; it ran in ACM Transactions on Modeling and Computer Simulation, Vol. 8, No. 1, pp.3–30, January 1998.

The [Complementary-Multiply-with-Carry recipe](https://code.activestate.com/recipes/576707-long-period-random-number-generator/) offers a drop-in substitute generator featuring a lengthy period together with relatively straightforward update steps.

Note

Both the module-level random number generator and `Random` instances are thread-safe. In the free-threaded build, though, simultaneous calls against the global generator or against a single `Random` instance can run into contention and degraded performance. The recommended alternative is a dedicated `Random` instance for each thread.

[Subject index](INDEX.md) · [Continue](random-seed-to-random-setstate.md)
