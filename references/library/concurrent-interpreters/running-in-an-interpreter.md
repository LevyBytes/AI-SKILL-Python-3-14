# concurrent.interpreters - Running in an Interpreter

### Running in an Interpreter

To run inside a different interpreter, you switch over to it within the current thread and then call a function. The runtime carries out that function against the current interpreter’s state. For creating and managing interpreters, plus the switch-and-call step, the `concurrent.interpreters` module offers a basic API.

The operation spins up no additional threads on its own — though a helper exists for that. A separate, purpose-built helper handles calling the builtin [`exec()`](https://docs.python.org/3.14/library/functions.html#exec) within an interpreter.

Should [`exec()`](https://docs.python.org/3.14/library/functions.html#exec) (or [`eval()`](https://docs.python.org/3.14/library/functions.html#eval)) be invoked inside an interpreter, they execute with that interpreter’s `__main__` module serving as the “globals” namespace. Functions tied to no module behave identically. It mirrors the way command-line scripts run in the `__main__` module.

[Subject index](INDEX.md) · [Previous](multiple-interpreters-and-isolation.md) · [Continue](concurrency-and-parallelism.md) · [Owning module, declaration or section: concurrent.interpreters](multiple-interpreters-overview.md)
