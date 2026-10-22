# contextvars.ContextVar: `get()`, `set()`, `reset()`

name

The variable's name, exposed as a read-only property.

Added in version 3.7.1.

 get([*default*])

Give back a value of the context variable as seen by the current context.

When the current context holds no value for that variable, this method does one of the following:

- hands back whatever was passed as the method's *default* argument, when one was given; or

- hands back the variable's own default, supposing it was declared with one; or

- raise a [`LookupError`](https://docs.python.org/3.14/library/exceptions.html#LookupError).

 set(*value*)

Invoke this to assign a fresh value to the context variable within the current context.

That mandatory *value* argument supplies the context variable's new value.

Yields a `Token` object, which the `ContextVar.reset()` method can later use to roll the variable back to its earlier value.

As a convenience, that token can act as a context manager so you need not call `ContextVar.reset()` yourself:

```python
var = ContextVar('var', default='default value')

with var.set('new value'):
    assert var.get() == 'new value'

assert var.get() == 'default value'

```

This stands in as shorthand for:

```python
var = ContextVar('var', default='default value')

token = var.set('new value')
try:
    assert var.get() == 'new value'
finally:
    var.reset(token)

assert var.get() == 'default value'

```

Added in version 3.14: Tokens may now be employed in the role of context managers.

 reset(*token*)

Restore the context variable to whatever value it carried prior to the `ContextVar.set()` call that produced the *token*.

For example:

```python
var = ContextVar('var')

token = var.set('new value')
# code that uses 'var'; var.get() returns 'new value'.
var.reset(token)

# After the reset call the var has no value again, so
# var.get() would raise a LookupError.

```

The same *token* cannot be used twice.

[Subject index](INDEX.md) · [Previous](contextvars-contextvar-class.md) · [Continue](contextvars-token-class.md) · [Owning module, declaration or section: contextvars](contextvars-context-variables.md) · [Owning module, declaration or section: contextvars.ContextVar](contextvars-contextvar-class.md) · [Owning module, declaration or section: Context Variables](contextvars-contextvar-class.md)
