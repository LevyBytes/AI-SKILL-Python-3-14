# compound statements: With-statement context-manager lifecycle

### 8.5. The `with` statement

A block’s execution is wrapped with methods supplied by a context manager (consult the section [With Statement Context Managers](https://docs.python.org/3.14/reference/datamodel.html#context-managers)) by means of the `with` statement. With it, the usual `try`…`except`…`finally` usage patterns can be bundled up for handy reuse.

```text

with_stmt:          "with" ( "(" with_stmt_contents ","? ")" | with_stmt_contents ) ":" suite
with_stmt_contents: with_item ("," with_item)*
with_item:          expression "as" [target]
```

Running the `with` statement with a single “item” unfolds in this way:

1.

The context expression (that is, the expression supplied in the `with_item`) is evaluated to produce a context manager.

2.

The context manager’s [`__enter__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__enter__) is loaded for later use.

3.

The context manager’s [`__exit__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__exit__) is loaded for later use.

4.

The context manager’s [`__enter__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__enter__) method is invoked.

5.

Should the `with` statement carry a target, the value [`__enter__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__enter__) returns is bound to it.

Note

The `with` statement promises that whenever the [`__enter__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__enter__) method returns error-free, [`__exit__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__exit__) will invariably be called. So, should an error strike while assigning to the target list, it gets handled exactly as an error arising inside the suite would. Refer to step 7 below.

6.

The suite is executed.

7.

The context manager’s [`__exit__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__exit__) method is invoked. Should an exception have forced the suite to exit, its type, value, and traceback get handed to `__exit__()` as arguments. If not, three [`None`](https://docs.python.org/3.14/library/constants.html#None) arguments are supplied.

Should the suite have exited because of an exception, and the value the [`__exit__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__exit__) method returned was false, the exception is reraised. Should the returned value be true, the exception is suppressed, and execution carries on with the statement that follows the `with` statement.

Should the suite have exited for some reason apart from an exception, the value [`__exit__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__exit__) returns is disregarded, and execution resumes at the usual spot for whichever kind of exit occurred.

This code:

```python
with EXPRESSION as TARGET:
    SUITE

```

is, in meaning, the same as:

```python
manager = (EXPRESSION)
enter = manager.__enter__
exit = manager.__exit__
value = enter()
hit_except = False

try:
    TARGET = value
    SUITE
except:
    hit_except = True
    if not exit(*sys.exc_info()):
        raise
finally:
    if not hit_except:
        exit(None, None, None)

```

with the difference that implicit [special method lookup](https://docs.python.org/3.14/reference/datamodel.html#special-lookup) applies for [`__enter__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__enter__) and [`__exit__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__exit__).

When there is more than one item, the context managers get handled as though several `with` statements had been nested:

[Subject index](INDEX.md) · [Owning language section](compound-statements.md) · [Previous source section](finally-clause.md) · [Following source section](the-with-statement-suite-to-suite.md)
