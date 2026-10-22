# stdtypes: Tuple commas, parentheses and construction rules

Keep in mind that what truly builds a tuple is the comma rather than the surrounding parentheses. You may drop the parentheses in most situations, the exceptions being an empty tuple and any place where they resolve syntactic ambiguity. To illustrate, `f(a, b, c)` invokes a function on three separate arguments, whereas `f((a, b, c))` invokes it on a single argument that happens to be a 3-tuple.

Every common sequence operation is available on tuples.

With respect to the types they hold, tuples are [generic](https://docs.python.org/3.14/library/typing.html#generics). Additional detail lives in [the typing documentation on annotating tuples](https://docs.python.org/3.14/library/typing.html#annotating-tuples).

When you have a mixed bag of data and labeling each item reads better than positional lookup, reaching for [`collections.namedtuple()`](https://docs.python.org/3.14/library/collections.html#collections.namedtuple) often beats a plain tuple object.

[Subject index](INDEX.md) · [Continue](range-class-to-range-class.md) · [Owning module, declaration or section: tuple](tuple-class.md) · [Owning module, declaration or section: Tuples](tuple-class.md) · [Preceding source contract and version conditions](tuple-class.md)
