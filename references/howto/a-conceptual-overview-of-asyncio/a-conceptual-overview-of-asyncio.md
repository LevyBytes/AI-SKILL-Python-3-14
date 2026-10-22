# A Conceptual Overview of `asyncio`

# A Conceptual Overview Of Asyncio

### A Conceptual Overview of `asyncio`

The aim of this [HOWTO](https://docs.python.org/3.14/howto/index.html#how-tos) piece is to give you a solid mental picture of the way [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio) operates at its core, so that the reasoning behind the patterns people recommend becomes clear.

A handful of central `asyncio` ideas may be on your mind. Once you reach the end here, the following questions should be easy for you to answer:

- When some object gets awaited, what is really going on under the hood?

- In what way does `asyncio` tell apart a job that requires no CPU time (think of a network request or file read) from one that does (think of working out n-factorial)?

- How would you author an asynchronous form of an operation, like an async sleep or a database query.

See also

- The [guide](https://github.com/anordin95/a-conceptual-overview-of-asyncio/tree/main) that inspired this HOWTO article, by Alexander Nordin.

- This in-depth [YouTube tutorial series](https://www.youtube.com/watch?v=Xbl7XjFYsN4&list=PLhNSoGM2ik6SIkVGXWBwerucXjgP1rHmB) on `asyncio` created by Python core team member, ?ukasz Langa.

- [500 Lines or Less: A Web Crawler With asyncio Coroutines](https://aosabook.org/en/500L/a-web-crawler-with-asyncio-coroutines.html) by A. Jesse Jiryu Davis and Guido van Rossum.

[Subject index](INDEX.md) · [Following source context](a-conceptual-overview-part-1-the-high-level.md)
