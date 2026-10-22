# contextvars / Manual Context Management: `contextvars.Context`, `run()`, `copy()`, `get()`, `iter()`

*class *contextvars.Context

A mapping of `ContextVars` to their values.

Calling `Context()` builds an empty context containing no values whatsoever. For a duplicate of the present context, turn to the `copy_context()` function.

Every thread keeps a distinct stack of `Context` objects of its own. Whatever `Context` object sits atop that thread's stack counts as the [current context](https://docs.python.org/3.14/glossary.html#term-current-context). Each `Context` object held in these stacks is regarded as *entered*.

*Entering* a context — accomplished by invoking its `run()` method — turns it into the current context, since it gets pushed onto the top of the thread's context stack.

*Exiting* the current context — done by returning out of the callback handed to `run()` — pops that context off the top of the stack and thereby brings the current context back to what it was before entry.

Because every thread owns a separate context stack, assigning values across different threads makes `ContextVar` objects act much like [`threading.local()`](https://docs.python.org/3.14/library/threading.html#threading.local).

Trying to enter a context that has already been entered — even one entered over in another thread — throws a [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError).

Once a context has been exited, any thread is free to enter it again afterward.

Every modification to `ContextVar` values done through `ContextVar.set()` is logged against the current context, and `ContextVar.get()` reports back the value tied to that current context. Leaving a context essentially undoes whatever changes were applied to context variables during the time it was entered; re-entering the context restores those values should you need them again.

The [`collections.abc.Mapping`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.Mapping) interface is implemented by Context.

 run(*callable*, **args*, ***kwargs*)

Steps into the Context, runs `callable(*args, **kwargs)`, and then steps back out of the Context. The result of *callable* is handed back, or any exception that arose is propagated.

Example:

```python
import contextvars

var = contextvars.ContextVar('var')
var.set('spam')
print(var.get())  # 'spam'

ctx = contextvars.copy_context()

def main():
    # 'var' was set to 'spam' before
    # calling 'copy_context()' and 'ctx.run(main)', so:
    print(var.get())  # 'spam'
    print(ctx[var])  # 'spam'

    var.set('ham')

    # Now, after setting 'var' to 'ham':
    print(var.get())  # 'ham'
    print(ctx[var])  # 'ham'

# Any changes that the 'main' function makes to 'var'
# will be contained in 'ctx'.
ctx.run(main)

# The 'main()' function was run in the 'ctx' context,
# so changes to 'var' are contained in it:
print(ctx[var])  # 'ham'

# However, outside of 'ctx', 'var' is still set to 'spam':
print(var.get())  # 'spam'

```

 copy()

Hand back a shallow duplicate of the context object.

 var in context

Yield `True` when *context* carries a value set for *var*, and `False` if it does not.

 context[var]

Give back the value of the *var* `ContextVar`. Where that variable has no setting in the context object, a [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError) gets thrown.

 get(*var*[, *default*])

Provide the value for *var* whenever *var* is present in the context object; otherwise provide *default*. With no *default* supplied, `None` comes back.

 iter(context)

Produce an iterator that walks the variables kept in the context object.

[Subject index](INDEX.md) · [Previous](contextvars-copy-context.md) · [Continue](contextvars-context-len-to-contextvars-context-items.md) · [Owning module, declaration or section: contextvars](contextvars-context-variables.md) · [Owning module, declaration or section: Manual Context Management](contextvars-copy-context.md)
