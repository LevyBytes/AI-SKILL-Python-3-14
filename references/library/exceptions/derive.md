# exceptions: `derive()`

derive(*excs*)

Returns an exception group carrying the same `message` but bundling the exceptions in `excs` instead.

`subgroup()` and `split()` rely on this method, and those two are used across various situations to split an exception group apart. A subclass has to override it so that `subgroup()` and `split()` yield instances of the subclass rather than `ExceptionGroup`.

`subgroup()` and `split()` copy the `__traceback__`, `__cause__`, `__context__` and `__notes__` fields from the original exception group onto the one `derive()` returns, so `derive()` itself has no need to update those fields.

```pycon
>>> class MyGroup(ExceptionGroup):
...     def derive(self, excs):
...         return MyGroup(self.message, excs)
...
>>> e = MyGroup("eg", [ValueError(1), TypeError(2)])
>>> e.add_note("a note")
>>> e.__context__ = Exception("context")
>>> e.__cause__ = Exception("cause")
>>> try:
...    raise e
... except Exception as e:
...    exc = e
...
>>> match, rest = exc.split(ValueError)
>>> exc, exc.__context__, exc.__cause__, exc.__notes__
(MyGroup('eg', [ValueError(1), TypeError(2)]), Exception('context'), Exception('cause'), ['a note'])
>>> match, match.__context__, match.__cause__, match.__notes__
(MyGroup('eg', [ValueError(1)]), Exception('context'), Exception('cause'), ['a note'])
>>> rest, rest.__context__, rest.__cause__, rest.__notes__
(MyGroup('eg', [TypeError(2)]), Exception('context'), Exception('cause'), ['a note'])
>>> exc.__traceback__ is match.__traceback__ is rest.__traceback__
True

```

Bear in mind that `BaseExceptionGroup` defines [`__new__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__new__), so a subclass wanting a different constructor signature must override that rather than [`__init__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__init__). As an illustration, the code below defines an exception group subclass that takes an exit_code and builds the group’s message out of it.

```python
class Errors(ExceptionGroup):
   def __new__(cls, errors, exit_code):
      self = super().__new__(Errors, f"exit code: {exit_code}", errors)
      self.exit_code = exit_code
      return self

   def derive(self, excs):
      return Errors(excs, self.exit_code)

```

As with `ExceptionGroup`, any `BaseExceptionGroup` subclass that is at the same time a subclass of `Exception` is limited to bundling `Exception` instances.

Added in version 3.11.

[Subject index](INDEX.md) · [Previous](exceptiongroup-to-split.md) · [Continue](exception-hierarchy.md) · [Owning module, declaration or section: Exception groups](exceptiongroup-to-split.md)
