# generator.send(*value*)

generator.send(*value*)

Continues execution and "sends" a value into the generator function. That *value* argument turns into the outcome of the active yield expression. What `send()` hands back is whatever value the generator yields next, or it raises [`StopIteration`](https://docs.python.org/3.14/library/exceptions.html#StopIteration) should the generator finish without producing another value. If you use `send()` to kick off the generator, you have to pass [`None`](https://docs.python.org/3.14/library/constants.html#None) as its argument, since no yield expression yet exists that could accept the value.

[Subject index](INDEX.md) · [Owning language section](expressions.md) · [Owning language section](atoms.md) · [Owning language section](yield-expressions.md) · [Owning language section](generator-iterator-methods.md) · [Previous source section](generator-next.md) · [Following source section](generator-exception-injection.md)
