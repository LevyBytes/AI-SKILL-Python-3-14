# object.__match_args__

object.__match_args__

This class variable may be assigned a tuple of strings. When this class is used within a class pattern carrying positional arguments, each positional argument is turned into a keyword argument, taking the matching value from *__match_args__* as the keyword. Lacking this attribute is the same as setting it to `()`.

For instance, if `MyClass.__match_args__` is `("left", "center", "right")`, then `case MyClass(x, y)` amounts to `case MyClass(left=x, center=y)`. Note that the count of arguments in the pattern has to be less than or equal to the count of elements in *__match_args__*; should it be greater, the pattern match attempt raises a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError).

Added in version 3.10.

See also

[**PEP 634**](https://peps.python.org/pep-0634/) - Structural Pattern Matching

The specification for the Python `match` statement.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](special-method-names.md) · [Owning language section](customizing-positional-arguments-in-class-pattern-matching.md) · [Previous source section](customizing-positional-arguments-in-class-pattern-matching.md) · [Following source section](emulating-buffer-types.md)
