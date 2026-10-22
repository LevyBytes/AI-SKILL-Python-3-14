# unittest.mock — Magic Mock

### Magic Mock

`MagicMock` comes in two flavours: `MagicMock` and `NonCallableMagicMock`.

 *class *unittest.mock.MagicMock(**args*, ***kw*)

`MagicMock` subclasses `Mock` and ships default implementations for most of the [magic methods](https://docs.python.org/3.14/glossary.html#term-magic-method). With `MagicMock` you needn't configure the magic methods on your own.

The constructor parameters carry the same meaning they do for `Mock`.

When you supply the *spec* or *spec_set* arguments, then *only* the magic methods present in the spec get created.

[Subject index](INDEX.md) · [Previous](mock-unary-numeric-magic-methods.md) · [Continue](unittest-mock-noncallablemagicmock-class.md) · [Owning module, declaration or section: unittest.mock](unittest-mock-mock-object-library.md)
