# anext

*awaitable *anext(*async_iterator*, */*)

 *awaitable *anext(*async_iterator*, *default*, */*)

Upon being awaited, yield the following element from the supplied [asynchronous iterator](https://docs.python.org/3.14/glossary.html#term-asynchronous-iterator); should *default* be supplied and the iterator be used up, that value comes back instead.

Think of this as the asynchronous counterpart to the `next()` builtin, with comparable behavior.

It invokes the [`__anext__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__anext__) method on *async_iterator* and hands back an [awaitable](https://docs.python.org/3.14/glossary.html#term-awaitable). Awaiting that produces the iterator’s next value. Should *default* be present, it comes back whenever the iterator runs out; otherwise [`StopAsyncIteration`](https://docs.python.org/3.14/library/exceptions.html#StopAsyncIteration) gets raised.

Added in version 3.10.

[Builtin task index](INDEX.md).
