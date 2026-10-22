# Context management

Open when checking Python definitions for context management.

## context management protocol

The [`__enter__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__enter__) and [`__exit__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__exit__) methods that the [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement invokes. See [**PEP 343**](https://peps.python.org/pep-0343/).

## context manager

An object that follows the context management protocol and governs the environment exposed within a [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement. See [**PEP 343**](https://peps.python.org/pep-0343/).

## asynchronous context manager

An object that governs the environment exposed within an [`async with`](https://docs.python.org/3.14/reference/compound_stmts.html#async-with) statement, doing so by implementing [`__aenter__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__aenter__) and [`__aexit__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__aexit__) methods. Introduced by [**PEP 492**](https://peps.python.org/pep-0492/).

## context

The sense of this term shifts according to where and how you apply it. A few frequent senses:

- The transient state or environment that a context manager sets up by way of a [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement.

- The set of key–value bindings tied to a given [`contextvars.Context`](https://docs.python.org/3.14/library/contextvars.html#contextvars.Context) object and reached through [`ContextVar`](https://docs.python.org/3.14/library/contextvars.html#contextvars.ContextVar) objects. Refer as well to context variable.

- A [`contextvars.Context`](https://docs.python.org/3.14/library/contextvars.html#contextvars.Context) object. Refer as well to current context.

## current context

The context (a [`contextvars.Context`](https://docs.python.org/3.14/library/contextvars.html#contextvars.Context) object) that [`ContextVar`](https://docs.python.org/3.14/library/contextvars.html#contextvars.ContextVar) objects are presently using to read or write the values of context variables. Every thread carries its own current context. Frameworks that run asynchronous tasks (see [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio)) tie each task to a context that turns into the current context each time the task begins or continues running.

## context variable

A variable whose value hinges on whichever context happens to be the current context. You reach the values through [`contextvars.ContextVar`](https://docs.python.org/3.14/library/contextvars.html#contextvars.ContextVar) objects. The chief use of context variables is keeping state separate across concurrent asynchronous tasks.

[Glossary context index](INDEX.md).
