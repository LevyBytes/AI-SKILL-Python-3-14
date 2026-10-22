# stdtypes: Range start, stop and step attributes

start

Whatever was passed as *start* (or `0` when that parameter went unsupplied)

 stop

Whatever was passed as *stop*

 step

Whatever was passed as *step* (or `1` when that parameter went unsupplied)

What makes the `range` type preferable to an ordinary `list` or `tuple` is that any `range` object occupies a fixed (and tiny) footprint, however large the range it stands for happens to be (since it merely keeps the `start`, `stop` and `step` values and works out individual elements and subranges on demand).

The [`collections.abc.Sequence`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.Sequence) ABC is implemented by range objects, which therefore offer capabilities like membership checks, locating an element's index, slicing, and handling of negative indices (refer to Sequence Types — list, tuple, range):

```python
>>> r = range(0, 20, 2)
>>> r
range(0, 20, 2)
>>> 11 in r
False
>>> 10 in r
True
>>> r.index(10)
5
>>> r[5]
10
>>> r[:5]
range(0, 10, 2)
>>> r[-1]
18

```

Comparing range objects via `==` and `!=` treats them as sequences. Put another way, a pair of range objects counts as equal when both stand for an identical sequence of values. (Be aware that two range objects deemed equal can still carry distinct `start`, `stop` and `step` attributes, as in `range(0) == range(2, 1, 3)` or `range(0, 3, 2) == range(0, 4, 2)`.)

Changed in version 3.2: The Sequence ABC is now implemented. Slicing plus negative indices became supported. Membership checks for [`int`](https://docs.python.org/3.14/library/functions.html#int) objects now run in constant time, no longer walking through each item.

Changed in version 3.3: The ‘==’ and ‘!=’ operators were redefined so that range objects are compared by the value sequence each one describes, rather than by object identity.

Added the `start`, `stop` and `step` attributes.

See also

- The [linspace recipe](https://code.activestate.com/recipes/579000-equally-spaced-numbers-linspace/) demonstrates building a lazy range variant fit for floating-point work.

[Subject index](INDEX.md) · [Previous](range-class-to-range-class.md) · [Continue](text-and-binary-sequence-type-methods-summary.md) · [Owning module, declaration or section: range; range](range-class-to-range-class.md) · [Owning module, declaration or section: Ranges](range-class-to-range-class.md)
