# unittest.mock — Sealing mocks

### Sealing mocks

 unittest.mock.seal(*mock*)

Sealing turns off the automatic minting of mocks when you reach for an attribute on the sealed mock or, recursively, on any of its attributes that are themselves already mocks.

A mock instance that carries a name or a spec, once assigned to an attribute, stays out of the sealing chain. That lets you keep seal from locking down a portion of the mock object.

```python
>>> mock = Mock()
>>> mock.submock.attribute1 = 2
>>> mock.not_submock = mock.Mock(name="sample_name")
>>> seal(mock)
>>> mock.new_attribute  # This will raise AttributeError.
>>> mock.submock.attribute2  # This will raise AttributeError.
>>> mock.not_submock.attribute2  # This won't raise.

```

Added in version 3.7.

[Subject index](INDEX.md) · [Previous](autospeccing-code-example-class-something.md) · [Continue](mock-side-effect-return-and-wraps-precedence.md) · [Owning module, declaration or section: unittest.mock](unittest-mock-mock-object-library.md)
