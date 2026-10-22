# next

next(*iterator*, */*)

 next(*iterator*, *default*, */*)

Fetch the upcoming item out of the [iterator](https://docs.python.org/3.14/glossary.html#term-iterator) by invoking its [`__next__()`](https://docs.python.org/3.14/library/stdtypes.html#iterator.__next__) method. When *default* is supplied, it comes back if the iterator has run out, and otherwise [`StopIteration`](https://docs.python.org/3.14/library/exceptions.html#StopIteration) gets raised.

[Builtin task index](INDEX.md).
