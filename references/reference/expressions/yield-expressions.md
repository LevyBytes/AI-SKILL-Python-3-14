# 6.2.10. Yield expressions

### 6.2.10. Yield expressions

```text

yield_atom:       "(" yield_expression ")"
yield_from:       "yield" "from" expression
yield_expression: "yield" yield_list | yield_from
```

A yield expression comes into play when you define a [generator](https://docs.python.org/3.14/glossary.html#term-generator) function or an [asynchronous generator](https://docs.python.org/3.14/glossary.html#term-asynchronous-generator) function, which is why it may appear only within a function definition's body. Placing a yield expression in a function's body turns that function into a generator function, and placing it in the body of an [`async def`](https://docs.python.org/3.14/reference/compound_stmts.html#async-def) function turns that coroutine function into an asynchronous generator function. For instance:

```python
def gen():  # defines a generator function
    yield 123

async def agen(): # defines an asynchronous generator function
    yield 123

```

Because of the effects they have on the surrounding scope, `yield` expressions cannot appear inside the implicitly defined scopes that implement comprehensions and generator expressions.

Changed in version 3.8: Within the implicitly nested scopes that back comprehensions and generator expressions, yield expressions became disallowed.

Generator functions get their treatment below; asynchronous generator functions are handled on their own in the Asynchronous generator functions section.

Calling a generator function gives back an iterator called a generator, and that generator then drives how the generator function runs. Execution kicks off the moment one of the generator's methods is invoked. From there it advances to the first yield expression, where it pauses once more, handing the value of `yield_list` back to the generator's caller ? or `None` when `yield_list` is left out. Pausing here means the whole of the local state is held onto: each local variable's current binding, where the instruction pointer sits, the internal evaluation stack, plus the status of any exception handling underway. Once execution is picked back up by calling one of the generator's methods, the function carries on just as though the yield expression had merely been another outside call. Which value the yield expression takes on after resumption hinges on the method that resumed execution. When `__next__()` is the one used (commonly by way of a [`for`](https://docs.python.org/3.14/reference/compound_stmts.html#for) loop or the [`next()`](https://docs.python.org/3.14/library/functions.html#next) builtin), the outcome is [`None`](https://docs.python.org/3.14/library/constants.html#None). When instead `send()` is used, the outcome is whatever value was handed to that method.

Taken together, all this leaves generator functions a great deal like coroutines: they yield more than once, they have several entry points, and their execution can be paused. The sole distinction is that a generator function has no say over where execution should pick up after a yield; control invariably passes back to the generator's caller.

A yield expression may appear at any location inside a [`try`](https://docs.python.org/3.14/reference/compound_stmts.html#try) construct. Should the generator never be resumed prior to its finalization (either because its reference count drops to zero or because the garbage collector reclaims it), the runtime invokes the generator-iterator's `close()` method, which lets any outstanding [`finally`](https://docs.python.org/3.14/reference/compound_stmts.html#finally) clauses run.

With `yield from <expr>`, the expression you provide has to be an iterable. Iterating over it yields values that flow straight back to whoever calls the methods of the enclosing generator. Anything handed in through `send()`, along with exceptions delivered through `throw()`, gets forwarded to the inner iterator provided it exposes the matching methods. When those methods are absent, `send()` raises [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError) or [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError), whereas `throw()` simply re-raises the supplied exception right away.

Once the inner iterator finishes, the [`value`](https://docs.python.org/3.14/library/exceptions.html#StopIteration.value) attribute carried by the raised [`StopIteration`](https://docs.python.org/3.14/library/exceptions.html#StopIteration) object turns into the result of the yield expression. You can assign that value directly while raising `StopIteration`, or let it be filled in automatically whenever the subiterator happens to be a generator (which returns the value from the subgenerator).

Changed in version 3.3: `yield from <expr>` was introduced so that flow of control can be handed off to a subiterator.

You can drop the surrounding parentheses whenever the yield expression stands alone as the right-hand side of an assignment statement.

See also

[**PEP 255**](https://peps.python.org/pep-0255/) - Simple Generators

The proposal for adding generators and the [`yield`](https://docs.python.org/3.14/reference/simple_stmts.html#yield) statement to Python.

[**PEP 342**](https://peps.python.org/pep-0342/) - Coroutines via Enhanced Generators

The proposal that improved the generator API and syntax so they could serve as straightforward coroutines.

[**PEP 380**](https://peps.python.org/pep-0380/) - Syntax for Delegating to a Subgenerator

The proposal to introduce the `yield_from` syntax, making delegation to subgenerators easy.

[**PEP 525**](https://peps.python.org/pep-0525/) - Asynchronous Generators

The proposal that expanded on [**PEP 492**](https://peps.python.org/pep-0492/) by adding generator capabilities to coroutine functions.

[Subject index](INDEX.md) · [Owning language section](expressions.md) · [Owning language section](atoms.md) · [Previous source section](generator-expression-errors-and-yield-restrictions.md) · [Following source section](generator-iterator-methods.md)
