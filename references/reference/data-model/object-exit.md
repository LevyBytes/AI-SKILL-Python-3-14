# object.__exit__(*self*, *exc_type*, *exc_value*, *traceback*)

object.__exit__(*self*, *exc_type*, *exc_value*, *traceback*)

Exit the runtime context tied to this object. The parameters convey the exception that triggered the context to be exited. If the context exited without an exception, all three arguments will be [`None`](https://docs.python.org/3.14/library/constants.html#None).

If an exception is supplied and the method intends to suppress it (that is, stop it from propagating), it should return a true value. Otherwise, the exception is handled as usual when this method exits.

Note that `__exit__()` methods should not reraise the exception they were passed; doing so is the caller's responsibility.

See also

[**PEP 343**](https://peps.python.org/pep-0343/) - The "with" statement

The specification, background, and examples for the Python [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](special-method-names.md) · [Owning language section](with-statement-context-managers.md) · [Previous source section](object-enter.md) · [Following source section](customizing-positional-arguments-in-class-pattern-matching.md)
