# The Ellipsis Object

### The Ellipsis Object

This object is most often used to signal that something has been left out. It offers no special operations. There is precisely one ellipsis object, called [`Ellipsis`](https://docs.python.org/3.14/library/constants.html#Ellipsis) (a built-in name). `type(Ellipsis)()` yields the `Ellipsis` singleton.

It is shown as `Ellipsis` or `...`.

When used normally, `...` standing for the `Ellipsis` object turns up in several spots, among them:

- Within type annotations, for instance [callable arguments](https://docs.python.org/3.14/library/typing.html#annotating-callables) or [tuple elements](https://docs.python.org/3.14/library/typing.html#annotating-tuples).

- Serving as a function’s body in place of a [pass statement](https://docs.python.org/3.14/tutorial/controlflow.html#tut-pass).

- Within third-party libraries, for instance [Numpy’s slicing and striding](https://numpy.org/doc/stable/user/basics.indexing.html#slicing-and-striding).

There are also places where Python employs three dots that are not `Ellipsis` objects, among them:

- Doctest’s [`ELLIPSIS`](https://docs.python.org/3.14/library/doctest.html#doctest.ELLIPSIS), serving as a pattern for content that is missing.

- The standard Python prompt of the [interactive](https://docs.python.org/3.14/glossary.html#term-interactive) shell whenever partial input remains unfinished.

Finally, throughout the Python documentation three dots are frequently used in ordinary English to denote omitted content, even within code examples that also wield them as the `Ellipsis`.

[Subject index](INDEX.md) · [Previous](the-null-object.md) · [Continue](the-notimplemented-object.md)
