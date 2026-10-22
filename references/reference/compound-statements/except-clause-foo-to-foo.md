# 8.4.1. `except` clause

### 8.4.1. `except` clause

One or more exception handlers are named by the `except` clause(s). Should no exception arise in the `try` clause, none of the exception handlers run. Should an exception arise in the `try` suite, a hunt for an exception handler begins. That hunt examines each `except` clause in order until it locates one that fits the exception. An `except` clause lacking an expression, if it appears, has to come last; it fits any exception whatsoever.

When an `except` clause carries an expression, that expression must resolve to an exception type or a tuple of exception types. The parentheses may be omitted when several exception types are listed and the `as` clause is left out. A raised exception fits an `except` clause when that clause’s expression resolves to the exception object’s class or one of its [non-virtual base class](https://docs.python.org/3.14/glossary.html#term-abstract-base-class)es, or to a tuple holding such a class.

Should none of the `except` clauses fit the exception, the hunt for an exception handler carries on in the enclosing code and up the invocation stack. [1]

Should evaluating an expression in the header of an `except` clause itself raise an exception, the original handler hunt is abandoned and a fresh hunt starts for the new exception in the enclosing code and up the call stack (it behaves as though the whole `try` statement had raised the exception).

Once a fitting `except` clause is located, the exception is bound to the target named after the `as` keyword in that `except` clause, if one is given, and the `except` clause’s suite runs. Every `except` clause must contain an executable block. After execution reaches the end of that block, control resumes normally past the whole `try` statement. (Consequently, if two nested handlers cover the same exception, and the exception arises in the `try` clause of the inner handler, the outer handler does not deal with the exception.)

After an exception gets bound via `as target`, it is cleared once the `except` clause ends. The effect is as though

```python
except E as N:
    foo

```

had been rewritten as

```python
except E as N:
    try:
        foo
    finally:
        del N

```

This implies you have to bind the exception to a separate name in order to reference it past the `except` clause. Clearing happens because exceptions, carrying their attached traceback, form a reference cycle together with the stack frame, which keeps every local in that frame alive right up until the next garbage collection runs.

Just before an `except` clause’s suite runs, the exception is placed in the [`sys`](https://docs.python.org/3.14/library/sys.html#module-sys) module, where code inside the `except` clause body can reach it by calling [`sys.exception()`](https://docs.python.org/3.14/library/sys.html#sys.exception). Upon exit from an exception handler, the exception kept in the `sys` module reverts to its earlier value:

```python
>>> print(sys.exception())
None
>>> try:
...     raise TypeError
... except:
...     print(repr(sys.exception()))
...     try:
...          raise ValueError
...     except:
...         print(repr(sys.exception()))
...     print(repr(sys.exception()))
...
TypeError()
ValueError()
TypeError()
>>> print(sys.exception())
None

```

[Subject index](INDEX.md) · [Owning language section](compound-statements.md) · [Owning language section](the-try-statement.md) · [Previous source section](the-try-statement.md) · [Following source section](exception-group-handlers.md)
