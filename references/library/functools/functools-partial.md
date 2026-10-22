# functools: `functools.partial()`

functools.partial(*func*, */*, **args*, ***keywords*)

Produce a fresh partial object that, on being called, acts like *func* invoked with the positional arguments *args* and keyword arguments *keywords*. Should the call supply further arguments, they get tacked onto *args*. Should extra keyword arguments arrive, they augment and supersede *keywords*. Roughly equivalent to:

```python
def partial(func, /, *args, **keywords):
    def newfunc(*more_args, **more_keywords):
        return func(*args, *more_args, **(keywords | more_keywords))
    newfunc.func = func
    newfunc.args = args
    newfunc.keywords = keywords
    return newfunc

```

You use the `partial()` function for partial function application, which "freezes" a slice of a function's arguments and/or keywords to yield a new object sporting a simplified signature. As one example, `partial()` lets you build a callable that acts like the [`int()`](https://docs.python.org/3.14/library/functions.html#int) function but with the *base* argument defaulting to `2`:

```pycon
>>> basetwo = partial(int, base=2)
>>> basetwo.__doc__ = 'Convert base 2 string to an int.'
>>> basetwo('10010')
18

```

Should `Placeholder` sentinels appear within *args*, they get populated first once `partial()` is invoked. That lets you pre-fill any positional argument through a `partial()` call; lacking `Placeholder`, you could only pre-fill some count of the leading positional arguments.

Should any `Placeholder` sentinels appear, every one of them has to be supplied at call time:

```pycon
>>> say_to_world = partial(print, Placeholder, Placeholder, "world!")
>>> say_to_world('Hello', 'dear')
Hello dear world!

```

Invoking `say_to_world('Hello')` triggers a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError), since just one positional argument is given while two placeholders still require filling.

Should `partial()` be applied atop an existing `partial()` object, the input object's `Placeholder` sentinels get populated using new positional arguments. You can preserve a placeholder by dropping a new `Placeholder` sentinel into the spot a prior `Placeholder` occupied:

```pycon
>>> from functools import partial, Placeholder as _
>>> remove = partial(str.replace, _, _, '')
>>> message = 'Hello, dear dear world!'
>>> remove(message, ' dear')
'Hello, world!'
>>> remove_dear = partial(remove, _, ' dear')
>>> remove_dear(message)
'Hello, world!'
>>> remove_first_dear = partial(remove_dear, _, 1)
>>> remove_first_dear(message)
'Hello, dear world!'

```

`Placeholder` cannot be passed to `partial()` as a keyword argument.

Changed in version 3.14: Added support for `Placeholder` in positional arguments.

[Subject index](INDEX.md) · [Previous](functools-placeholder.md) · [Continue](functools-partialmethod-class.md) · [Owning module, declaration or section: functools](cached-factorial-and-dataset-examples.md)
