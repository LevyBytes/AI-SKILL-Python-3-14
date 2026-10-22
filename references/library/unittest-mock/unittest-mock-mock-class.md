# unittest.mock: `unittest.mock.Mock`

### The Mock Class

`Mock` is an adaptable mock object meant to take the place of stubs and test doubles across your code. Mocks can be called and spin up attributes as fresh mocks once you reach them [1]. Reaching for the same attribute hands back the identical mock every time. Mocks keep track of how you exercise them, so you can assert what your code performed on them.

`MagicMock` extends `Mock`, arriving with all the magic methods already built and ready to go. Non-callable flavors exist too, handy whenever you are mocking out objects that cannot be called: `NonCallableMock` and `NonCallableMagicMock`

With the `patch()` decorators it becomes simple to swap classes in a given module out for a `Mock` object on a temporary basis. Out of the box `patch()` builds a `MagicMock` on your behalf. Through the *new_callable* argument to `patch()` you may name a different class of `Mock`.

 *class *unittest.mock.Mock(*spec=None*, *side_effect=None*, *return_value=DEFAULT*, *wraps=None*, *name=None*, *spec_set=None*, *unsafe=False*, ***kwargs*)

Build a fresh `Mock` object. `Mock` accepts a handful of optional arguments that dictate how the Mock object behaves:

- *spec*: This may be supplied as either a list of strings or an already-existing object (a class or instance) serving as the specification for the mock object. Should you hand over an object, a list of strings gets assembled by invoking dir on it (leaving out unsupported magic attributes and methods). Reaching any attribute absent from this list raises an [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError).

When *spec* is an object (instead of a list of strings) then [`__class__`](https://docs.python.org/3.14/reference/datamodel.html#object.__class__) yields the class of the spec object. That lets mocks satisfy [`isinstance()`](https://docs.python.org/3.14/library/functions.html#isinstance) tests.

- *spec_set*: A tighter form of *spec*. When applied, trying to *set* or read an attribute on the mock that is absent from the object given as *spec_set* raises an [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError).

- *side_effect*: A function invoked each time the Mock is called. Refer to the `side_effect` attribute. Handy for throwing exceptions or shifting return values on the fly. It receives the same arguments as the mock, and so long as it doesn’t return `DEFAULT`, this function’s return value becomes the return value.

As an alternative, *side_effect* may be an exception class or instance. Then that exception gets raised once the mock is called.

Where *side_effect* is an iterable, every call to the mock yields the following value from the iterable.

Clearing a *side_effect* is done by assigning it `None`.

- *return_value*: Whatever value comes back when the mock is called. By default that is a fresh Mock (built on first access). Refer to the `return_value` attribute.

- *unsafe*: By default, reaching any attribute whose name opens with *assert*, *assret*, *asert*, *aseert* or *assrt* raises an [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError). Supplying `unsafe=True` permits reaching these attributes.

Added in version 3.5.

- *wraps*: An item for the mock object to wrap. Where *wraps* is not `None`, calling the Mock forwards the call onward to the wrapped object (handing back the genuine result). Attribute access on the mock yields a Mock object wrapping the matching attribute of the wrapped object (so trying to reach an attribute that is missing raises an [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError)).

When the mock carries an explicit *return_value*, calls bypass the wrapped object and the *return_value* comes back instead.

- *name*: Where the mock has a name, that name shows up in the repr of the mock. This can aid debugging. The name flows down to child mocks.

Mocks may additionally be called using arbitrary keyword arguments. Those serve to assign attributes on the mock once it is built. Refer to the `configure_mock()` method for specifics.

[Subject index](INDEX.md) · [Previous](quick-guide-code-example-foo-key-value.md) · [Continue](mock-call-count-and-argument-assertions.md) · [Owning module, declaration or section: unittest.mock](unittest-mock-mock-object-library.md)
