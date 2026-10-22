# object.__call__(*self*[, *args...*])

### 3.3.6. Emulating callable objects

 object.__call__(*self*[, *args...*])

Invoked when the instance is "called" the way a function is; given this method is defined, `x(arg1, arg2, ...)` is roughly equivalent to `type(x).__call__(x, arg1, ...)`. The [`object`](https://docs.python.org/3.14/library/functions.html#object) class on its own does not supply this method.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](special-method-names.md) · [Previous source section](class-getitem-versus-getitem.md) · [Following source section](emulating-container-types.md)
