# Code Object Flags

### Code Object Flags

A code object carries a bit-field of flags that you can read off through the [`co_flags`](https://docs.python.org/3.14/reference/datamodel.html#codeobject.co_flags) Python attribute (with [`PyObject_GetAttrString()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_GetAttrString), say), and that you set by way of a *flags* argument to `PyUnstable_Code_New()` and kindred functions.

Any flag beginning with `CO_FUTURE_` maps to a feature you would ordinarily turn on through [future statements](https://docs.python.org/3.14/reference/simple_stmts.html#future). Such flags are usable within [`PyCompilerFlags.cf_flags`](https://docs.python.org/3.14/c-api/veryhigh.html#c.PyCompilerFlags.cf_flags). Bear in mind that in today's Python a good many `CO_FUTURE_` flags are obligatory, so setting them accomplishes nothing.

Listed below are the flags on offer. To learn what each means, consult the linked documentation for its Python equivalent.

| Flag | Meaning |
| --- | --- |
| CO_OPTIMIZED | `inspect.CO_OPTIMIZED` |
| CO_NEWLOCALS | `inspect.CO_NEWLOCALS` |
| CO_VARARGS | `inspect.CO_VARARGS` |
| CO_VARKEYWORDS | `inspect.CO_VARKEYWORDS` |
| CO_NESTED | `inspect.CO_NESTED` |
| CO_GENERATOR | `inspect.CO_GENERATOR` |
| CO_COROUTINE | `inspect.CO_COROUTINE` |
| CO_ITERABLE_COROUTINE | `inspect.CO_ITERABLE_COROUTINE` |
| CO_ASYNC_GENERATOR | `inspect.CO_ASYNC_GENERATOR` |
| CO_HAS_DOCSTRING | `inspect.CO_HAS_DOCSTRING` |
| CO_METHOD | `inspect.CO_METHOD` |
| CO_FUTURE_DIVISION | no effect (`__future__.division`) |
| CO_FUTURE_ABSOLUTE_IMPORT | no effect (`__future__.absolute_import`) |
| CO_FUTURE_WITH_STATEMENT | no effect (`__future__.with_statement`) |
| CO_FUTURE_PRINT_FUNCTION | no effect (`__future__.print_function`) |
| CO_FUTURE_UNICODE_LITERALS | no effect (`__future__.unicode_literals`) |
| CO_FUTURE_GENERATOR_STOP | no effect (`__future__.generator_stop`) |
| CO_FUTURE_ANNOTATIONS | `__future__.annotations` |

[Subject index](INDEX.md) · [Previous source contract](pycodeevent-to-pycode-optimize.md) · [Following source contract](code-object-extra-data.md)
