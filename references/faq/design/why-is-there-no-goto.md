# Why is there no goto?

### Why is there no goto?

During the 1970s it became clear that an unconstrained goto tends to breed tangled “spaghetti” code that resists comprehension and editing. A high-level language has no need for it either, provided the language offers ways to branch (in Python, via [`if`](https://docs.python.org/3.14/reference/compound_stmts.html#if) statements together with [`or`](https://docs.python.org/3.14/reference/expressions.html#or), [`and`](https://docs.python.org/3.14/reference/expressions.html#and), and `if`/[`else`](https://docs.python.org/3.14/reference/compound_stmts.html#else) expressions) and to loop (via [`while`](https://docs.python.org/3.14/reference/compound_stmts.html#while) and [`for`](https://docs.python.org/3.14/reference/compound_stmts.html#for) statements, which may hold [`continue`](https://docs.python.org/3.14/reference/simple_stmts.html#continue) and [`break`](https://docs.python.org/3.14/reference/simple_stmts.html#break)).

Exceptions, too, can stand in for a “structured goto,” one that even reaches across function-call boundaries. A widely held opinion is that exceptions neatly reproduce every sensible application of the `go` or `goto` constructs found in C, Fortran, and similar languages. Here is an example:

```python
class label(Exception): pass  # declare a label

try:
    ...
    if condition: raise label()  # goto label
    ...
except label:  # where to goto
    pass
...

```

It won’t let you leap into the interior of a loop, though landing there is generally regarded as misusing `goto` in the first place. Reach for it only rarely.

[Subject index](INDEX.md)
