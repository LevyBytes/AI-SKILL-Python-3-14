# Built-in Functions

sum(*iterable*, */*, *start=0*)

Add *start* together with the items of an *iterable*, working left to right, and hand back the total. Typically those items are numbers, and the start value can't be a string.

Certain situations have solid alternatives to `sum()`. To stitch a sequence of strings together, the favored, quick route is `''.join(sequence)`. For adding floating-point values at extended precision, look to [`math.fsum()`](https://docs.python.org/3.14/library/math.html#math.fsum). And to join a run of iterables end to end, give [`itertools.chain()`](https://docs.python.org/3.14/library/itertools.html#itertools.chain) a thought.

Changed in version 3.8: You may now hand *start* over by keyword.

Changed in version 3.12: Adding floats moved to an algorithm delivering greater accuracy plus improved commutativity across most builds.

Changed in version 3.14: A specialization for adding complexes was introduced, reusing the very algorithm employed when adding floats.

[Subject index](INDEX.md) · [Previous](str-class-to-str-class.md) · [Continue](super-class-to-super-class.md) · [Owning module, declaration or section: Built-in Functions](INDEX.md)
