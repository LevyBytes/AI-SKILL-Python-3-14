# generator.close()

generator.close()

Throws a [`GeneratorExit`](https://docs.python.org/3.14/library/exceptions.html#GeneratorExit) exception at the spot where the generator function had paused (the same as invoking `throw(GeneratorExit)`). That exception surfaces at the yield expression where the generator was suspended. Should the generator function trap the exception and then return a value, `close()` hands that value back. When the generator function has already been closed, or it raises `GeneratorExit` (by leaving the exception uncaught), `close()` yields [`None`](https://docs.python.org/3.14/library/constants.html#None). If instead the generator produces a value, a [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError) gets raised. Any other exception the generator throws is forwarded to the caller. When the generator has already terminated, whether through an exception or by finishing normally, `close()` returns `None` and does nothing further.

Changed in version 3.13: When a generator hands back a value as it is closed, that value becomes what `close()` returns.

[Subject index](INDEX.md) · [Owning language section](expressions.md) · [Owning language section](atoms.md) · [Owning language section](yield-expressions.md) · [Owning language section](generator-iterator-methods.md) · [Previous source section](generator-exception-injection.md) · [Following source section](examples.md)
