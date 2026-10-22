# contextvars: `contextvars.ContextVar`

### Context Variables

 *class *contextvars.ContextVar(*name*[, ***, *default*])

Use this class to declare a fresh Context Variable, for instance:

```python
var: ContextVar[int] = ContextVar('var', default=42)

```

That mandatory *name* parameter serves introspection and debugging.

Whenever the current context holds no value for the variable, `ContextVar.get()` falls back to the optional keyword-only *default* parameter.

**Important:** Always create Context Variables at the top level of a module, never within closures. Because `Context` objects keep strong references to context variables, defining them in closures stops those variables from being garbage collected as they should.

Each `ContextVar` is [generic](https://docs.python.org/3.14/library/typing.html#generics) with respect to the type of value it carries.

[Subject index](INDEX.md) · [Previous](contextvars-context-variables.md) · [Continue](contextvars-contextvar-get-to-contextvars-contextvar-reset.md) · [Owning module, declaration or section: contextvars](contextvars-context-variables.md)
