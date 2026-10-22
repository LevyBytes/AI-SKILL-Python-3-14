# concurrent.interpreters: `concurrent.interpreters.Interpreter`

### Interpreter objects

`class concurrent.interpreters.Interpreter(*id*)`

One interpreter within the current process.

As a rule, don’t call `Interpreter` straight off. Reach for `create()` or another of the module’s functions instead.

`id`

(read-only)

The ID of the interpreter underneath.

`whence`

(read-only)

A string telling you where the interpreter originated.

[Subject index](INDEX.md) · [Previous](interpreter-discovery-and-queue-creation.md) · [Continue](interpreter-running-state-and-calls.md) · [Owning module, declaration or section: concurrent.interpreters](multiple-interpreters-overview.md)
