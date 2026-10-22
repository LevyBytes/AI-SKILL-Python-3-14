# Asynchronous execution

Open when checking Python definitions for asynchronous execution.

## coroutine

Coroutines extend subroutines into a more general form. A subroutine is entered at a single point and left at a single point. A coroutine, however, can be entered, left, and continued at numerous points. The [`async def`](https://docs.python.org/3.14/reference/compound_stmts.html#async-def) statement is one way to realize them. Refer as well to [**PEP 492**](https://peps.python.org/pep-0492/).

## coroutine function

A function that yields a coroutine object. You may write a coroutine function with the [`async def`](https://docs.python.org/3.14/reference/compound_stmts.html#async-def) statement, and it may carry [`await`](https://docs.python.org/3.14/reference/expressions.html#await), [`async for`](https://docs.python.org/3.14/reference/compound_stmts.html#async-for), and [`async with`](https://docs.python.org/3.14/reference/compound_stmts.html#async-with) keywords. [**PEP 492**](https://peps.python.org/pep-0492/) brought these in.

## awaitable

An object usable inside an [`await`](https://docs.python.org/3.14/reference/expressions.html#await) expression. It may be a coroutine or an object carrying an [`__await__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__await__) method. Refer as well to [**PEP 492**](https://peps.python.org/pep-0492/).

## asynchronous iterable

An object usable within an [`async for`](https://docs.python.org/3.14/reference/compound_stmts.html#async-for) statement. Its [`__aiter__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__aiter__) method has to return an asynchronous iterator. Introduced by [**PEP 492**](https://peps.python.org/pep-0492/).

## asynchronous iterator

An object furnishing the [`__aiter__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__aiter__) and [`__anext__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__anext__) methods. The `__anext__()` method has to give back an awaitable object. An [`async for`](https://docs.python.org/3.14/reference/compound_stmts.html#async-for) keeps resolving the awaitables produced by an asynchronous iterator's `__anext__()` method until that method raises a [`StopAsyncIteration`](https://docs.python.org/3.14/library/exceptions.html#StopAsyncIteration) exception. Introduced by [**PEP 492**](https://peps.python.org/pep-0492/).

## asynchronous generator

A function that yields an asynchronous generator iterator. It resembles a coroutine function written with [`async def`](https://docs.python.org/3.14/reference/compound_stmts.html#async-def), the difference being that it holds [`yield`](https://docs.python.org/3.14/reference/simple_stmts.html#yield) expressions that emit a sequence of values for consumption inside an [`async for`](https://docs.python.org/3.14/reference/compound_stmts.html#async-for) loop.

The phrase normally points to an asynchronous generator function, though in certain settings it may instead denote an *asynchronous generator iterator*. Whenever the meaning could be misread, spelling out the full terms removes the ambiguity.

Within an asynchronous generator function you may also place [`await`](https://docs.python.org/3.14/reference/expressions.html#await) expressions along with [`async for`](https://docs.python.org/3.14/reference/compound_stmts.html#async-for) and [`async with`](https://docs.python.org/3.14/reference/compound_stmts.html#async-with) statements.

## asynchronous generator iterator

An object produced by an asynchronous generator function.

It is an asynchronous iterator that, when driven via the [`__anext__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__anext__) method, hands back an awaitable object that runs the body of the asynchronous generator function up to the following [`yield`](https://docs.python.org/3.14/reference/simple_stmts.html#yield) expression.

Every [`yield`](https://docs.python.org/3.14/reference/simple_stmts.html#yield) briefly halts execution while preserving the run state (local variables and outstanding try-statements included). Once the *asynchronous generator iterator* genuinely continues by way of a further awaitable handed back from [`__anext__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__anext__), it carries on from the point where it stopped. Consult [**PEP 492**](https://peps.python.org/pep-0492/) and [**PEP 525**](https://peps.python.org/pep-0525/).

[Glossary context index](INDEX.md).
