# concurrent.interpreters — Exceptions

### Exceptions

`exception concurrent.interpreters.InterpreterError`

A subclass of [`Exception`](https://docs.python.org/3.14/library/exceptions.html#Exception), this one fires whenever an interpreter-related error crops up.

`exception concurrent.interpreters.InterpreterNotFoundError`

A subclass of `InterpreterError`, raised once the interpreter you were aiming at has ceased to exist.

`exception concurrent.interpreters.ExecutionFailed`

A subclass of `InterpreterError`, raised when the code that was running threw an exception nobody caught.

`excinfo`

A bare-bones snapshot of whatever exception was thrown over in the other interpreter.

`exception concurrent.interpreters.NotShareableError`

A subclass of [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError), raised when an object simply can’t be handed off to another interpreter.

[Subject index](INDEX.md) · [Previous](interpreter-running-state-and-calls.md) · [Continue](interpreter-queues-and-capacity-errors.md) · [Owning module, declaration or section: concurrent.interpreters](multiple-interpreters-overview.md)
