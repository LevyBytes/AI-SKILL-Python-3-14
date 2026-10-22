# types: `types.NoneType`, `types.FunctionType`, `types.LambdaType`, `types.GeneratorType`, `types.CoroutineType`, `types.AsyncGeneratorType`

### Standard Interpreter Types

This module furnishes names for a good many of the types that a Python interpreter needs in order to function. It purposely leaves out certain types that crop up only incidentally during processing, such as the `listiterator` type.

The usual reason to reach for these names is in [`isinstance()`](https://docs.python.org/3.14/library/functions.html#isinstance) or [`issubclass()`](https://docs.python.org/3.14/library/functions.html#issubclass) checks.

Should you instantiate any of these types, keep in mind that the signatures can differ from one Python version to another.

Standard names are provided for the types listed below:

 *class *types.NoneType

The type belonging to [`None`](https://docs.python.org/3.14/library/constants.html#None).

Added in version 3.10.

 types.FunctionType

 types.LambdaType

The type of user-defined functions plus functions produced by [`lambda`](https://docs.python.org/3.14/reference/expressions.html#lambda) expressions.

Emits an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `function.__new__` carrying the argument `code`.

That audit event fires solely on direct instantiation of function objects; it is not emitted during ordinary compilation.

 types.GeneratorType

The type of [generator](https://docs.python.org/3.14/glossary.html#term-generator)-iterator objects that generator functions produce.

 types.CoroutineType

The type of [coroutine](https://docs.python.org/3.14/glossary.html#term-coroutine) objects that [`async def`](https://docs.python.org/3.14/reference/compound_stmts.html#async-def) functions produce.

Added in version 3.5.

 types.AsyncGeneratorType

The type of [asynchronous generator](https://docs.python.org/3.14/glossary.html#term-asynchronous-generator)-iterator objects that asynchronous generator functions produce.

Added in version 3.6.

[Subject index](INDEX.md) · [Previous](types-get-original-bases.md) · [Continue](types-codetype-class.md) · [Owning module, declaration or section: types](types-dynamic-type-creation-and-names-for-built-in-types.md)
