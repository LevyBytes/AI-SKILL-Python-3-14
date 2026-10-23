# typing - typing.Annotated

```pycon
>>> from typing import Annotated, get_type_hints
>>> def func(x: Annotated[int, "metadata"]) -> None: pass
...
>>> get_type_hints(func)
{'x': <class 'int'>, 'return': <class 'NoneType'>}
>>> get_type_hints(func, include_extras=True)
{'x': typing.Annotated[int, 'metadata'], 'return': <class 'NoneType'>}

```

While a program runs, you can read back the metadata attached to an `Annotated` type through the `__metadata__` attribute:

>

```pycon
>>> from typing import Annotated
>>> X = Annotated[int, "very", "important", "metadata"]
>>> X
typing.Annotated[int, 'very', 'important', 'metadata']
>>> X.__metadata__
('very', 'important', 'metadata')

```

To get back the underlying type that `Annotated` wraps, reach for the `__origin__` attribute:

>

```pycon
>>> from typing import Annotated, get_origin
>>> Password = Annotated[str, "secret"]
>>> Password.__origin__
<class 'str'>

```

Be aware that a call to `get_origin()` yields `Annotated` on its own:

>

```pycon
>>> get_origin(Password)
typing.Annotated

```

See also

[**PEP 593**](https://peps.python.org/pep-0593/) - Flexible function and variable annotations

The PEP that brought `Annotated` into the standard library.

Added in version 3.9.

[Subject index](INDEX.md) · [Continue](typing-typeis.md) · [Owning module, declaration or section: typing](typing-support-for-type-hints.md) · [Owning module, declaration or section: typing.Annotated](typing-readonly-to-typing-annotated.md) · [Preceding source contract and version conditions](special-forms.md)
