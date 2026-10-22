# concurrent.interpreters — Reference

### Reference

The functions this module defines are:

`concurrent.interpreters.list_all()`

Hand back a [`list`](https://docs.python.org/3.14/library/stdtypes.html#list) of `Interpreter` objects, one per interpreter that currently exists.

`concurrent.interpreters.get_current()`

Hand back an `Interpreter` object for whichever interpreter is running right now.

`concurrent.interpreters.get_main()`

Hand back an `Interpreter` object for the main interpreter — the one the runtime built to drive the [REPL](https://docs.python.org/3.14/glossary.html#term-REPL) or the script handed in at the command line. Ordinarily it’s the only interpreter around.

`concurrent.interpreters.create()`

Spin up a fresh (idle) Python interpreter and give back an `Interpreter` object for it.

`concurrent.interpreters.create_queue()`

Spin up a fresh cross-interpreter queue and give back a `Queue` object for it.

[Subject index](INDEX.md) · [Previous](sharing-objects.md) · [Continue](concurrent-interpreters-interpreter-class.md) · [Owning module, declaration or section: concurrent.interpreters](multiple-interpreters-overview.md)
