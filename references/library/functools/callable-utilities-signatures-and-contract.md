# functools — `functools` — Higher-order functions and operations on callable objects — Signature and initial contract

@functools.singledispatch

Turn a function into a [single-dispatch](https://docs.python.org/3.14/glossary.html#term-single-dispatch) [generic function](https://docs.python.org/3.14/glossary.html#term-generic-function).

You define a generic function by decorating it with the `@singledispatch` decorator. Bear in mind when defining a function via `@singledispatch` that dispatch keys off the type of the first argument:

```python
>>> from functools import singledispatch
>>> @singledispatch
... def fun(arg, verbose=False):
...     if verbose:
...         print("Let me just say,", end=" ")
...     print(arg)

```

To register overloaded implementations on the function, employ the generic function's `register()` attribute, which doubles as a decorator. For functions carrying type annotations, the decorator deduces the first argument's type for you:

```python
>>> @fun.register
... def _(arg: int, verbose=False):
...     if verbose:
...         print("Strength in numbers, eh?", end=" ")
...     print(arg)
...
>>> @fun.register
... def _(arg: list, verbose=False):
...     if verbose:
...         print("Enumerate this:")
...     for i, elem in enumerate(arg):
...         print(i, elem)

```

[`typing.Union`](https://docs.python.org/3.14/library/typing.html#typing.Union) is another option:

```python
>>> @fun.register
... def _(arg: int | float, verbose=False):
...     if verbose:
...         print("Strength in numbers, eh?", end=" ")
...     print(arg)
...
>>> from typing import Union
>>> @fun.register
... def _(arg: Union[list, set], verbose=False):
...     if verbose:
...         print("Enumerate this:")
...     for i, elem in enumerate(arg):
...         print(i, elem)
...

```

When code skips type annotations, you can hand the right type argument straight to the decorator:

```python
>>> @fun.register(complex)
... def _(arg, verbose=False):
...     if verbose:
...         print("Better than complicated.", end=" ")
...     print(arg.real, arg.imag)
...

```

When code dispatches on a collections type (such as `list`) yet wants to typehint the collection's items (such as `list[int]`), pass the dispatch type explicitly to the decorator while the typehint lands in the function definition:

```python
>>> @fun.register(list)
... def _(arg: list[int], verbose=False):
...     if verbose:
...         print("Enumerate this:")
...     for i, elem in enumerate(arg):
...         print(i, elem)

```

Note

When it runs, the function dispatches on an instance of a list no matter what type sits inside the list — that is, `[1,2,3]` dispatches identically to `["foo", "bar", "baz"]`. The annotation shown in this example serves static type checkers alone and carries no runtime effect.

So that you can register [lambdas](https://docs.python.org/3.14/glossary.html#term-lambda) along with already-existing functions, the `register()` attribute is also usable in a functional form:

[Subject index](INDEX.md) · [Previous](functools-reduce.md) · [Continue](functools-and-verbose-false.md) · [Owning module, declaration or section: functools](cached-factorial-and-dataset-examples.md)
