# unittest.mock: `unittest.mock.sentinel`

### Helpers

### sentinel

 unittest.mock.sentinel

The `sentinel` object gives you a handy means of supplying unique objects for your tests.

Its attributes spring into being on demand the moment you access them by name. Reaching for the same attribute always yields the identical object. The objects you get back have a sensible repr, keeping test failure messages legible.

Changed in version 3.7: whenever they get [`copied`](https://docs.python.org/3.14/library/copy.html#module-copy) or [`pickled`](https://docs.python.org/3.14/library/pickle.html#module-pickle), the `sentinel` attributes now hold on to their identity.

Testing sometimes calls for verifying that one particular object is handed to another method as an argument, or returned from it. Creating named sentinel objects to check this is a frequent tactic. `sentinel` offers a tidy means of producing such objects and testing their identity.

In this example we monkey patch `method` to return `sentinel.some_object`:

[Subject index](INDEX.md) · [Owning module, declaration or section: unittest.mock](unittest-mock-mock-object-library.md) · [Required continuation of the source contract](sentinel.md)
