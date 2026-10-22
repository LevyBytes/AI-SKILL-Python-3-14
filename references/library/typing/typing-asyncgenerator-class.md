# typing: `typing.AsyncGenerator`

*class *typing.AsyncGenerator(*AsyncIterator[YieldType], Generic[YieldType, SendType]*)

Deprecated alias to [`collections.abc.AsyncGenerator`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.AsyncGenerator).

For guidance on applying [`collections.abc.AsyncGenerator`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.AsyncGenerator) and `typing.AsyncGenerator` within type annotations, refer to Annotating generators and coroutines.

Added in version 3.6.1.

Deprecated since version 3.9: [`collections.abc.AsyncGenerator`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.AsyncGenerator) now supports subscripting (`[]`). See [**PEP 585**](https://peps.python.org/pep-0585/) and [Generic Alias Type](https://docs.python.org/3.14/library/stdtypes.html#types-genericalias).

Changed in version 3.13: The `SendType` parameter now has a default.

[Subject index](INDEX.md) · [Previous](typing-coroutine-class.md) · [Continue](typing-asynciterable-class.md) · [Owning module, declaration or section: typing](typing-support-for-type-hints.md) · [Owning module, declaration or section: Aliases to asynchronous ABCs in `collections.abc`](typing-coroutine-class.md)
