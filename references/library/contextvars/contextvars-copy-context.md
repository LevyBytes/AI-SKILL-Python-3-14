# contextvars: `contextvars.copy_context()`

### Manual Context Management

 contextvars.copy_context()

Hands back a duplicate of the present `Context` object.

Below, a short snippet grabs a copy of the present context and writes out every variable along with the value it holds:

```python
ctx: Context = copy_context()
print(list(ctx.items()))

```

Its complexity is *O*(1), meaning the speed stays the same whether a context carries just a handful of context variables or a great many.

[Subject index](INDEX.md) · [Previous](contextvars-token-class.md) · [Continue](contextvars-context-class-to-contextvars-context-iter.md) · [Owning module, declaration or section: contextvars](contextvars-context-variables.md)
