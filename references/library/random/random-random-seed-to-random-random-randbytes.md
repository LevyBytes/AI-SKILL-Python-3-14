# random.Random: `seed()`, `getstate()`, `setstate()`, `random()`, `getrandbits()`, `randbytes()`

seed(*a=None*, *version=2*)

In a subclass, redefine this method to tailor how `seed()` behaves for `Random` instances.

 getstate()

In a subclass, redefine this method to tailor how `getstate()` behaves for `Random` instances.

 setstate(*state*)

In a subclass, redefine this method to tailor how `setstate()` behaves for `Random` instances.

 random()

In a subclass, redefine this method to tailor how `random()` behaves for `Random` instances.

A custom generator subclass may additionally supply the method below:

 getrandbits(*k*)

In a subclass, redefine this method to tailor how `getrandbits()` behaves for `Random` instances.

 randbytes(*n*)

In a subclass, redefine this method to tailor how `randbytes()` behaves for `Random` instances.

[Subject index](INDEX.md) · [Previous](random-random-class.md) · [Continue](random-systemrandom-class.md) · [Owning module, declaration or section: random](random-generate-pseudo-random-numbers.md) · [Owning module, declaration or section: random.Random](random-random-class.md) · [Owning module, declaration or section: Alternative Generator](random-random-class.md)
