# functools`partial` Objects

### `partial` Objects

A `partial` object is a callable that `partial()` produces. Three read-only attributes belong to each one:

 partial.func

Either a callable object or a function. Whenever the `partial` object is invoked, the call is passed along to `func` together with fresh arguments and keywords.

 partial.args

The positional arguments sitting furthest to the left, which get placed ahead of whatever positional arguments a `partial` object call supplies.

 partial.keywords

The keyword arguments handed over at the moment the `partial` object gets invoked.

In several respects `partial` objects resemble [function objects](https://docs.python.org/3.14/reference/datamodel.html#user-defined-funcs): they can be called, they support weak references, and they may carry attributes. Yet a few notable distinctions exist. As one example, the [`__name__`](https://docs.python.org/3.14/library/stdtypes.html#definition.__name__) and [`__doc__`](https://docs.python.org/3.14/library/stdtypes.html#definition.__doc__) attributes do not come into being on their own.

[Subject index](INDEX.md) · [Previous](functools-update-wrapper.md) · [Owning module, declaration or section: functools](cached-factorial-and-dataset-examples.md)
