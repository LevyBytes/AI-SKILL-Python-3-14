# inspect / Introspecting callables with the Signature object: `inspect.BoundArguments`, `apply_defaults()`

*class *inspect.BoundArguments

The outcome of a `Signature.bind()` or `Signature.bind_partial()` call. It carries the mapping of arguments onto the function's parameters.

 arguments

A mutable mapping that ties each parameter's name to its argument's value. It holds only the arguments that were explicitly bound. Edits to `arguments` propagate into `args` and `kwargs`.

Should be used in conjunction with `Signature.parameters` for any argument processing purposes.

Note

Any arguments for which `Signature.bind()` or `Signature.bind_partial()` fell back on a default value are left out. If you need them, though, call `BoundArguments.apply_defaults()` to fill them in.

Changed in version 3.9: `arguments` now has type [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict). Previously its type was [`collections.OrderedDict`](https://docs.python.org/3.14/library/collections.html#collections.OrderedDict).

 args

A tuple holding the positional argument values. It is computed on the fly from the `arguments` attribute.

 kwargs

A dict holding the keyword argument values. It is computed on the fly from the `arguments` attribute. Whatever arguments can be passed positionally end up in `args` instead.

 signature

A back-reference to the owning `Signature` object.

 apply_defaults()

Fill in default values for any missing arguments.

When it comes to variable-positional arguments (`*args`), the default is an empty tuple.

When it comes to variable-keyword arguments (`**kwargs`), the default is an empty dict.

```pycon
>>> def foo(a, b='ham', *args): pass
>>> ba = inspect.signature(foo).bind('spam')
>>> ba.apply_defaults()
>>> ba.arguments
{'a': 'spam', 'b': 'ham', 'args': ()}

```

Added in version 3.5.

You can rely on the `args` and `kwargs` properties to call functions:

```python
def test(a, *, b):
    ...

sig = signature(test)
ba = sig.bind(10, b=20)
test(*ba.args, **ba.kwargs)

```

See also

[**PEP 362**](https://peps.python.org/pep-0362/) - Function Signature Object.

The detailed specification, implementation details and examples.

[Subject index](INDEX.md) · [Previous](inspect-parameter-replace.md) · [Continue](inspect-getclasstree-to-inspect-unwrap.md) · [Owning module, declaration or section: inspect](inspect-inspect-live-objects.md) · [Owning module, declaration or section: Introspecting callables with the Signature object](inspect-signature.md)
