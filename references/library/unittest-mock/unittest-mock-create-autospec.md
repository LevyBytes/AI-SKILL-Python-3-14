# unittest.mock - create_autospec

### create_autospec

 unittest.mock.create_autospec(*spec*, *spec_set=False*, *instance=False*, ***kwargs*)

Build a mock object that takes another object as its spec. Each attribute on the mock adopts the matching attribute of the *spec* object as its own spec.

When functions or methods are mocked, their arguments get verified so that calls must match the right signature.

When *spec_set* is `True`, trying to assign attributes absent from the spec object triggers an [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError).

Should a class serve as the spec, the mock's return value (that is, the class instance) carries the identical spec. To make a class the spec for an instance object, supply `instance=True`. The resulting mock is callable only when instances of the mock are themselves callable.

Any extra keyword arguments handed to `create_autospec()` are forwarded into the constructor of the mock it builds.

For worked examples of applying auto-speccing via `create_autospec()` together with the *autospec* argument of `patch()`, consult Autospeccing.

Changed in version 3.8: when the target is an async function, `create_autospec()` now hands back an `AsyncMock`.

[Subject index](INDEX.md) · [Previous](unittest-mock-call-to-call-call-list.md) · [Continue](unittest-mock-any.md) · [Owning module, declaration or section: unittest.mock](unittest-mock-mock-object-library.md)
