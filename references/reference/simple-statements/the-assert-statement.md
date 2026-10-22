# 7.3. The `assert` statement

### 7.3. The `assert` statement

Assert statements offer a handy way to drop debugging assertions into a program:

```text

assert_stmt: "assert" expression "," [expression]
```

The basic form, `assert expression`, is the same as

```python
if __debug__:
    if not expression: raise AssertionError

```

The longer form, `assert expression1, expression2`, is the same as

```python
if __debug__:
    if not expression1: raise AssertionError(expression2)

```

These equivalences rest on the premise that [`__debug__`](https://docs.python.org/3.14/library/constants.html#debug__) and [`AssertionError`](https://docs.python.org/3.14/library/exceptions.html#AssertionError) point at the built-in variables carrying those names. As things stand in the current implementation, the built-in variable `__debug__` is `True` ordinarily, and `False` once optimization is asked for (the command line option [`-O`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-O)). The present code generator produces no code for an `assert` statement whenever optimization is requested at compile time. Observe that there is no need to bundle the source code for the failing expression into the error message; it gets shown as part of the stack trace.

Assignments to [`__debug__`](https://docs.python.org/3.14/library/constants.html#debug__) are illegal. The value of the built-in variable is fixed at the time the interpreter starts.

[Subject index](INDEX.md) · [Owning language section](simple-statements.md) · [Previous source section](annotated-assignment-statements.md) · [Following source section](the-pass-statement.md)
