# 6.2.5. Displays for lists, sets and dictionaries

### 6.2.5. Displays for lists, sets and dictionaries

To build a list, a set, or a dictionary, Python offers dedicated syntax known as ?displays?, and each comes in two varieties:

- either every member of the container is written out one by one, or

- they are generated through a series of looping and filtering steps, known as a *comprehension*.

The syntax pieces shared across comprehensions are:

```text

comprehension: assignment_expression comp_for
comp_for:      ["async"] "for" target_list "in" or_test [comp_iter]
comp_iter:     comp_for | comp_if
comp_if:       "if" or_test [comp_iter]
```

A comprehension is made up of one expression trailed by one or more `for` clauses plus any number of further `for` or `if` clauses. Here, the members of the freshly built container are exactly those you would get by treating each `for` or `if` clause as a block, nesting them from left to right, and evaluating the expression to yield one element every time control reaches the innermost block.

Apart from the iterable expression in the leftmost `for` clause, though, the comprehension runs inside its own separate, implicitly nested scope. That keeps names bound within the target list from ?leaking? out into the surrounding scope.

The iterable expression of the leftmost `for` clause gets evaluated straight away in the enclosing scope, then handed in as an argument to the implicitly nested scope. The remaining `for` clauses, along with any filter condition belonging to the leftmost `for` clause, cannot run in the enclosing scope because they might rely on values drawn from the leftmost iterable. Consider, for example: `[x*y for x in range(10) for y in range(x, x+10)]`.

So that a comprehension always yields a container of the right type, `yield` and `yield from` expressions are forbidden within the implicitly nested scope.

Starting in Python 3.6, code inside an [`async def`](https://docs.python.org/3.14/reference/compound_stmts.html#async-def) function can use an `async for` clause to step through an [asynchronous iterator](https://docs.python.org/3.14/glossary.html#term-asynchronous-iterator). Within an `async def` function, a comprehension may follow its leading expression with either a `for` or an `async for` clause, may include extra `for` or `async for` clauses, and may additionally employ `await` expressions.

A comprehension is termed an *asynchronous comprehension* if it has `async for` clauses, or if `await` expressions or other asynchronous comprehensions appear anywhere within it other than the iterable expression of the leftmost `for` clause. Running an asynchronous comprehension can pause the coroutine function it lives in. See also [**PEP 530**](https://peps.python.org/pep-0530/).

Added in version 3.6: Asynchronous comprehensions were introduced.

Changed in version 3.8: Inside the implicitly nested scope, both `yield` and `yield from` became forbidden.

Changed in version 3.11: Within asynchronous functions, asynchronous comprehensions may now be nested inside other comprehensions, and the enclosing comprehensions turn asynchronous of their own accord.

[Subject index](INDEX.md) · [Owning language section](expressions.md) · [Owning language section](atoms.md) · [Previous source section](parenthesized-forms.md) · [Following source section](list-displays.md)
