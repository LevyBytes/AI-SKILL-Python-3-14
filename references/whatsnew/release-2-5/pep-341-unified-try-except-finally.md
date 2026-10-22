# What's New in Python 2.5 / PEP 341: Unified try/except/finally

### PEP 341: Unified try/except/finally

Prior to Python 2.5, the [`try`](https://docs.python.org/3.14/reference/compound_stmts.html#try) statement existed in two forms. A [`finally`](https://docs.python.org/3.14/reference/compound_stmts.html#finally) block let you guarantee that some code always runs, while one or more [`except`](https://docs.python.org/3.14/reference/compound_stmts.html#except) blocks let you trap particular exceptions. Mixing `except` blocks together with a `finally` block wasn't allowed, because emitting the correct bytecode for that combination was tricky and the semantics the combined statement ought to carry weren't obvious.

Guido van Rossum put in some time working with Java, which does permit the equivalent of joining [`except`](https://docs.python.org/3.14/reference/compound_stmts.html#except) blocks with a [`finally`](https://docs.python.org/3.14/reference/compound_stmts.html#finally) block, and that experience made plain what the statement ought to signify. Under Python 2.5, you can now write:

```python
try:
    block-1 ...
except Exception1:
    handler-1 ...
except Exception2:
    handler-2 ...
else:
    else-block
finally:
    final-block

```

The code in *block-1* runs first. Should that code throw an exception, each of the [`except`](https://docs.python.org/3.14/reference/compound_stmts.html#except) blocks gets checked: when the exception belongs to class `Exception1`, *handler-1* runs; otherwise, if it belongs to class `Exception2`, *handler-2* runs, and on down the line. When no exception gets raised, the *else-block* runs.

Whatever took place beforehand, the *final-block* runs once the code block finishes and any exceptions that were raised have been dealt with. Even when something goes wrong inside an exception handler or the *else-block* and a fresh exception arises, the code in the *final-block* still runs.

See also

[**PEP 341**](https://peps.python.org/pep-0341/) - Unifying try-except and try-finally

PEP written by Georg Brandl; implementation by Thomas Lee.

[Subject index](INDEX.md) · [Previous source section](pep-338-executing-modules-as-scripts.md) · [Next source section](pep-342-new-generator-features.md) · [Release/subject declaration](pep-308-conditional-expressions.md)
