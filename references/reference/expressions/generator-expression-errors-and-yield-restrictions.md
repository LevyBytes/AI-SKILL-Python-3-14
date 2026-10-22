# expressions: Generator expression restrictions and asynchronous evaluation

```python
>>> iterator = (x * y for x in range(10) for y in nonexistent_iterable)
>>> iterator
<generator object <genexpr> at ...>
>>> list(iterator)
Traceback (most recent call last):
  ...
NameError: name 'nonexistent_iterable' is not defined

```

So as not to disturb the generator expression's intended workings, `yield` and `yield from` expressions are barred inside the implicitly nested scope.

When a generator expression holds either `async for` clauses or `await` expressions, it is termed an *asynchronous generator expression*. Such an expression hands back a new asynchronous generator object, which is itself an asynchronous iterator (refer to [Asynchronous Iterators](https://docs.python.org/3.14/reference/datamodel.html#async-iterators)).

Here is the formal grammar covering generator expressions:

```text

generator_expression: "(" expression comp_for ")"
```

Added in version 3.6: Asynchronous generator expressions were introduced.

Changed in version 3.7: Before Python 3.7, an asynchronous generator expression was confined to [`async def`](https://docs.python.org/3.14/reference/compound_stmts.html#async-def) coroutines; from 3.7 on, such expressions are available to any function.

Changed in version 3.8: Within the implicitly nested scope, `yield` and `yield from` alike became disallowed.

[Subject index](INDEX.md) · [Owning language section](expressions.md) · [Owning language section](atoms.md) · [Owning language section](generator-expressions.md) · [Contract or procedure setup](generator-expressions.md) · [Previous source section](generator-expressions.md) · [Following source section](yield-expressions.md)
