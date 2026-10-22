# 3.2.8.3. Generator functions

#### 3.2.8.3. Generator functions

Any function or method that contains the [`yield`](https://docs.python.org/3.14/reference/simple_stmts.html#yield) statement (refer to the section [The yield statement](https://docs.python.org/3.14/reference/simple_stmts.html#yield)) is termed a *generator function*. Whenever such a function is called, it consistently hands back an [iterator](https://docs.python.org/3.14/glossary.html#term-iterator) object that drives the execution of the function's body: invoking that iterator's [`iterator.__next__()`](https://docs.python.org/3.14/library/stdtypes.html#iterator.__next__) method drives the function forward until it yields a value through the `yield` statement. Once the function runs a [`return`](https://docs.python.org/3.14/reference/simple_stmts.html#return) statement or simply reaches its end, a [`StopIteration`](https://docs.python.org/3.14/library/exceptions.html#StopIteration) exception fires and the iterator has exhausted the collection of values it was meant to produce.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](the-standard-type-hierarchy.md) · [Owning language section](callable-types.md) · [Previous source section](instance-methods.md) · [Following source section](coroutine-functions.md)
