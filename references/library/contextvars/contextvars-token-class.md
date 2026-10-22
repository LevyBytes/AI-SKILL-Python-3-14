# contextvars: `contextvars.Token`

*class *contextvars.Token

The `ContextVar.set()` method is what produces *Token* objects. Feeding one to `ContextVar.reset()` rewinds the variable's value to what it held ahead of the matching *set*. No individual token may reset a context variable beyond a single time.

By honoring the [context manager protocol](https://docs.python.org/3.14/reference/datamodel.html#context-managers), tokens can reset context variables on their own. Refer to `ContextVar.set()`.

A token is [generic](https://docs.python.org/3.14/library/typing.html#generics) over the very type carried by the `ContextVar` that produced it.

Added in version 3.14: Use as a context manager is now possible.

 var

A read-only property that refers to the `ContextVar` object responsible for the token.

 old_value

A read-only property holding the value the variable carried just before the `ContextVar.set()` call that produced the token. Should the variable have been unset prior to that call, it refers to `Token.MISSING`.

 MISSING

A sentinel object that `Token.old_value` relies on.

[Subject index](INDEX.md) · [Previous](contextvars-contextvar-get-to-contextvars-contextvar-reset.md) · [Continue](contextvars-copy-context.md) · [Owning module, declaration or section: contextvars](contextvars-context-variables.md) · [Owning module, declaration or section: Context Variables](contextvars-contextvar-class.md)
