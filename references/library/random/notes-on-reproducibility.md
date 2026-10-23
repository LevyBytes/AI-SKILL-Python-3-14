# random - Notes on Reproducibility

### Notes on Reproducibility

There are times when reproducing the sequences a pseudo-random number generator emits is helpful. Reusing the same seed value should reproduce the identical sequence from one run to the next, provided no more than one thread is active.

While most of the random module's algorithms and seeding routines may shift between Python versions, two guarantees hold firm:

- Should a fresh seeding method be introduced, it will arrive alongside a backward compatible seeder.

- Feed the compatible seeder an identical seed and the generator's `random()` method will go on producing that same sequence.

[Subject index](INDEX.md) · [Previous](random-systemrandom-class.md) · [Continue](examples-section-introduction-and-initial-examples.md) · [Owning module, declaration or section: random](random-generate-pseudo-random-numbers.md)
