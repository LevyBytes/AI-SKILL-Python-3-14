# How can I evaluate an arbitrary Python expression from C?

### How can I evaluate an arbitrary Python expression from C?

Invoke the [`PyRun_String()`](https://docs.python.org/3.14/c-api/veryhigh.html#c.PyRun_String) function mentioned in the prior answer, handing it the start symbol [`Py_eval_input`](https://docs.python.org/3.14/c-api/veryhigh.html#c.Py_eval_input); it reads an expression, computes it, and yields the result.

[Subject index](INDEX.md)
