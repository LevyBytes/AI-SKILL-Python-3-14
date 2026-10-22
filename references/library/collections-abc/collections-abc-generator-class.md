# collections.abc: `collections.abc.Generator`

*class *collections.abc.Generator

ABC for [generator](https://docs.python.org/3.14/glossary.html#term-generator) classes realizing the protocol laid out in [**PEP 342**](https://peps.python.org/pep-0342/), which augments [iterators](https://docs.python.org/3.14/glossary.html#term-iterator) by adding the [`send()`](https://docs.python.org/3.14/reference/expressions.html#generator.send), [`throw()`](https://docs.python.org/3.14/reference/expressions.html#generator.throw) and [`close()`](https://docs.python.org/3.14/reference/expressions.html#generator.close) methods.

See [Annotating generators and coroutines](https://docs.python.org/3.14/library/typing.html#annotating-generators-and-coroutines) for details on using `Generator` in type annotations.

Added in version 3.5.

[Subject index](INDEX.md) · [Previous](collections-abc-reversible-class.md) · [Continue](sequence-mixins-and-index-methods.md) · [Owning module, declaration or section: collections.abc](collections-abc-abstract-base-classes-for-containers.md) · [Owning module, declaration or section: Collections Abstract Base Classes ??? Detailed Descriptions](collections-abc-container-class.md)
