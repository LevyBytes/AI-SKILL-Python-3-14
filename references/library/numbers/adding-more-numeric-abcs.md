# numbers - Adding More Numeric ABCs

### Adding More Numeric ABCs

Naturally, further numeric ABCs are conceivable, and the hierarchy would be a weak one if it shut the door on adding them. Slotting `MyFoo` in between `Complex` and `Real` looks like this:

```python
class MyFoo(Complex): ...
MyFoo.register(Real)

```

[Subject index](INDEX.md) · [Previous](notes-for-type-implementers.md) · [Continue](numeric-arithmetic-implementation-overview.md) · [Owning module, declaration or section: numbers](numbers-number-class.md)
