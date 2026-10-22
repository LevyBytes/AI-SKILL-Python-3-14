# Passing values into a generator

### Passing values into a generator

Throughout Python 2.4 and earlier, generators only emitted output. After a generator's code had been invoked to create an iterator, there was no avenue for passing fresh information into the function as its execution resumes. You could cobble this ability together by having the generator consult a global variable or by handing in some mutable object that callers then alter, yet these tactics are messy.

Python 2.5 introduced a clean way to feed values into a generator. [`yield`](https://docs.python.org/3.14/reference/simple_stmts.html#yield) turned into an expression, returning a value you can assign to a variable or otherwise act upon:

```python
val = (yield i)

```

I advise that you **always** wrap a `yield` expression in parentheses whenever you're doing something with the value it returns, as shown in the example above. The parentheses aren't required in every case, but it's simpler to add them consistently than to keep track of when they're called for.

([**PEP 342**](https://peps.python.org/pep-0342/) lays out the precise rules, namely that a `yield`-expression must always be parenthesized except where it appears as the top-level expression on the right-hand side of an assignment. So you can write `val = yield i` but must include parentheses whenever there's an operation, as in `val = (yield i) + 12`.)

[Subject index](INDEX.md) · [Following source continuation](passing-values-into-a-generator-continuation.md) · [Previous source context](generators.md)
